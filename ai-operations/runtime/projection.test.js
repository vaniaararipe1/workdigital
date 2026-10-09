'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),{buildProjection,agentKeys}=require('./projection');

function fixture(){
  const operation={id:'op',operation_key:'OP-1',status:'IN_PROGRESS',coordinator_agent:'patricia'};
  const task={id:'task',operation_id:'op',task_key:'TASK-1',owner_agent:'clara',status:'READY'};
  return {health:{ok:true,status:'online',database:'connected',version:'2.6.0'},agents:agentKeys.map(agent_key=>({agent_key,status:'active',permissions:{}})),operations:[operation,{id:'test-op',operation_key:'OP-TEST-1'}],tasks:[task,{id:'test-task',operation_id:'test-op',task_key:'TASK-TEST-1'}],work_packets:[{packet_key:'WP-1',operation_id:'op',task_id:'task',destination_agent:'clara'},{packet_key:'WP-TEST-1',operation_id:'test-op',task_id:'test-task'}]};
}

test('builds a safe scheduled projection and excludes test records',()=>{
  const out=buildProjection(fixture(),{capturedAt:'2026-10-09T00:30:00Z'});
  assert.equal(out.source,'chatgpt-control-plane-projection');
  assert.equal(out.live,false);
  assert.equal(out.runtime_verified,false);
  assert.deepEqual(out.operations.map(x=>x.key),['OP-1']);
  assert.deepEqual(out.tasks.map(x=>x.key),['TASK-1']);
  assert.deepEqual(out.work_packets.map(x=>x.key),['WP-1']);
  assert.equal(out.agents.find(x=>x.key==='clara').status,'active');
});

test('fails closed on unhealthy state or an unexpected agent registry',()=>{
  const unhealthy=fixture();unhealthy.health.database='offline';
  assert.throws(()=>buildProjection(unhealthy),/not healthy/);
  const missing=fixture();missing.agents.pop();
  assert.throws(()=>buildProjection(missing),/Unexpected agent registry/);
});
