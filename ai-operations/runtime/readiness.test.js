'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const {evaluateRuntimeReadiness}=require('./readiness');

test('current MCP capabilities keep dispatcher disabled',()=>{
  const result=evaluateRuntimeReadiness({live:true,runtime_verified:true},{capabilities:{atomic_compare_and_swap:false,lease_backend:false},runtimeIdentity:'run-a'});
  assert.equal(result.ready,false);assert.equal(result.dispatcher_enabled,false);
  assert.ok(result.reasons.includes('atomic-compare-and-swap-required'));
  assert.ok(result.reasons.includes('lease-backend-required'));
});
test('historical projection fails readiness independently of transport',()=>{
  const result=evaluateRuntimeReadiness({live:false,runtime_verified:false});
  assert.ok(result.reasons.includes('live-state-required'));
  assert.ok(result.reasons.includes('runtime-verified-required'));
});
test('all runtime proofs are required together',()=>{
  const originalNow=Date.now;Date.now=()=>Date.parse('2026-10-09T05:31:00Z');
  try{
    const result=evaluateRuntimeReadiness({live:true,runtime_verified:true},{capabilities:{atomic_compare_and_swap:true,lease_backend:true},runtimeIdentity:'run-a',lease:{owner:'run-a',expires_at:'2026-10-09T05:32:00Z'}});
    assert.equal(result.ready,true);assert.deepEqual(result.reasons,[]);
  }finally{Date.now=originalNow;}
});
