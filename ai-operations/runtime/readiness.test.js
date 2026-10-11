'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const {evaluateRuntimeReadiness}=require('./readiness');

test('missing durable backend capabilities keep dispatcher disabled',()=>{
  const result=evaluateRuntimeReadiness({live:true,runtime_verified:true},{capabilities:{atomic_compare_and_swap:false,lease_backend:false},runtimeIdentity:'run-a'});
  assert.equal(result.ready,false);assert.equal(result.dispatcher_enabled,false);
  assert.ok(result.reasons.includes('expected-version-required'));
  assert.ok(result.reasons.includes('atomic-compare-and-swap-required'));
  assert.ok(result.reasons.includes('lease-backend-required'));
  assert.ok(result.reasons.includes('fenced-work-packet-persistence-required'));
  assert.ok(result.reasons.includes('legacy-delivery-writes-blocked-required'));
});
test('historical projection fails readiness independently of transport',()=>{
  const result=evaluateRuntimeReadiness({live:false,runtime_verified:false});
  assert.ok(result.reasons.includes('live-state-required'));
  assert.ok(result.reasons.includes('runtime-verified-required'));
});
test('all runtime proofs are required together',()=>{
  const originalNow=Date.now;Date.now=()=>Date.parse('2026-10-09T05:31:00Z');
  try{
    const result=evaluateRuntimeReadiness({live:true,runtime_verified:true},{capabilities:{expected_version:true,atomic_compare_and_swap:true,lease_backend:true,fenced_work_packet_persistence:true,legacy_delivery_writes_blocked:true},runtimeIdentity:'run-a',lease:{owner:'run-a',expires_at:'2026-10-09T05:32:00Z'}});
    assert.equal(result.ready,true);assert.deepEqual(result.reasons,[]);
  }finally{Date.now=originalNow;}
});
test('delivery safety proofs cannot be bypassed by a verified runtime and active lease',()=>{
  const originalNow=Date.now;Date.now=()=>Date.parse('2026-10-09T05:31:00Z');
  try{
    const base={expected_version:true,atomic_compare_and_swap:true,lease_backend:true,fenced_work_packet_persistence:true,legacy_delivery_writes_blocked:true};
    for(const missing of ['expected_version','fenced_work_packet_persistence','legacy_delivery_writes_blocked']){
      const capabilities={...base,[missing]:false};
      const result=evaluateRuntimeReadiness({live:true,runtime_verified:true},{capabilities,runtimeIdentity:'run-a',lease:{owner:'run-a',expires_at:'2026-10-09T05:32:00Z'}});
      assert.equal(result.ready,false,missing);assert.equal(result.dispatcher_enabled,false,missing);
      assert.ok(result.reasons.includes(missing.replaceAll('_','-')+'-required'),missing);
    }
  }finally{Date.now=originalNow;}
});
