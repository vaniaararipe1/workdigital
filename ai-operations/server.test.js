'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),{createServer,normalize}=require('./server');
test('serves UI, labels history, refuses traversal and writes',async()=>{
  const previous=process.env.CONTROL_PLANE_API_URL;delete process.env.CONTROL_PLANE_API_URL;
  const server=createServer();await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const base='http://127.0.0.1:'+server.address().port;
  try{
    const home=await fetch(base+'/');assert.equal(home.status,200);const markup=await home.text();assert.match(markup,/Work Digital/);assert.match(markup,/Execução autônoma não verificada/);assert.match(markup,/role="dialog"/);assert.match(markup,/aria-live="polite"/);assert.doesNotMatch(markup,/>AGORA</);
    const state=await(await fetch(base+'/api/control-plane')).json();assert.equal(state.live,false);assert.equal(state.source,'chatgpt-control-plane-projection');
    const readiness=await(await fetch(base+'/api/runtime-readiness')).json();assert.equal(readiness.readiness.ready,false);assert.equal(readiness.capabilities.atomic_compare_and_swap,true);assert.equal(readiness.capabilities.fenced_work_packet_persistence,true);
    const queue=await fetch(base+'/api/queue');assert.equal(queue.status,503);const queueBody=await queue.json();assert.equal(queueBody.error,'runtime-not-ready');assert.ok(queueBody.readiness.reasons.includes('live-state-required'));assert.ok(queueBody.readiness.reasons.includes('runtime-verified-required'));
    assert.equal((await fetch(base+'/%2e%2e%2fserver.js')).status,403);
    assert.equal((await fetch(base+'/%ZZ')).status,400);
    assert.equal((await fetch(base+'/api/control-plane',{method:'POST'})).status,405);
  }finally{await new Promise(resolve=>server.close(resolve));if(previous!==undefined)process.env.CONTROL_PLANE_API_URL=previous;}
});
test('normalizes MCP keys and rejects malformed snapshots',()=>{
  assert.throws(()=>normalize({agents:[]}));
  assert.equal(normalize({agents:[{agent_key:'patricia'}],tasks:[],operations:[],work_packets:[]}).agents[0].key,'patricia');
});
