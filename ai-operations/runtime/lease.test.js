'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const {claimLease,releaseLease,planLeasedDispatch}=require('./lease');

function memoryStore(initial=null){
  let value=initial;
  return {
    async read(){return value&&structuredClone(value)},
    async compareAndSwap(version,next){
      const current=value?.version||0;
      if(current!==version)return false;
      value=structuredClone(next);return true;
    }
  };
}
function state(overrides={}){return {live:true,runtime_verified:true,agents:[{agent_key:'larissa',status:'active'}],operations:[{id:'op',status:'IN_PROGRESS'}],tasks:[{id:'t',task_key:'TASK-1',status:'READY',priority:90,dependencies:[]}],work_packets:[{packet_key:'WP-1',task_id:'t',operation_id:'op',destination_agent:'larissa',status:'SENT'}],...overrides};}

test('atomic store admits one owner and rejects a concurrent owner',async()=>{
  const store=memoryStore(),now='2026-10-09T02:00:00.000Z';
  const first=await claimLease(store,{owner:'run-a',now});
  const second=await claimLease(store,{owner:'run-b',now});
  assert.equal(first.acquired,true);assert.equal(second.acquired,false);assert.equal(second.reason,'lease-held');
});
test('expired lease can be claimed by another owner',async()=>{
  const store=memoryStore({version:4,owner:'run-a',acquired_at:'2026-10-09T01:00:00.000Z',expires_at:'2026-10-09T01:01:00.000Z'});
  const result=await claimLease(store,{owner:'run-b',now:'2026-10-09T02:00:00.000Z'});
  assert.equal(result.acquired,true);assert.equal(result.lease.version,5);assert.equal(result.lease.owner,'run-b');
});
test('only the active owner can release a lease',async()=>{
  const store=memoryStore(),now='2026-10-09T02:00:00.000Z';
  await claimLease(store,{owner:'run-a',now});
  assert.equal((await releaseLease(store,{owner:'run-b',now})).released,false);
  assert.equal((await releaseLease(store,{owner:'run-a',now})).released,true);
});
test('dispatch fails closed without live verified state and an owned active lease',()=>{
  const now='2026-10-09T02:00:00.000Z',lease={version:1,owner:'run-a',acquired_at:now,expires_at:'2026-10-09T02:01:00.000Z'};
  const result=planLeasedDispatch(state({live:false,runtime_verified:false}),{lease,owner:'run-b',now});
  assert.deepEqual(result.reasons,['live-state-required','runtime-verification-required','active-owned-lease-required']);
  assert.equal(result.executable,false);assert.equal(result.packet,null);
});
test('verified live state with owned lease selects one packet without executing it',()=>{
  const now='2026-10-09T02:00:00.000Z',lease={version:1,owner:'run-a',acquired_at:now,expires_at:'2026-10-09T02:01:00.000Z'};
  const result=planLeasedDispatch(state(),{lease,owner:'run-a',now});
  assert.equal(result.mode,'leased-dispatch-plan');assert.equal(result.executable,true);assert.equal(result.packet.packet_key,'WP-1');
});
test('non-atomic stores are rejected',async()=>{
  await assert.rejects(()=>claimLease({read:async()=>null},{owner:'run-a'}),/Atomic lease store/);
});
test('simultaneous acquisitions admit one winner even after CAS retries',async()=>{
  const store=memoryStore(),now='2026-10-09T12:00:00.000Z';
  const results=await Promise.all(['a','b','c'].map(owner=>claimLease(store,{owner,now})));
  assert.equal(results.filter(result=>result.acquired).length,1);
  assert.equal((await store.read()).version,1);
});

