'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),http=require('node:http'),snapshot=require('./snapshot.json'),{createServer,normalize,validateLiveState,controlPlaneEndpoint}=require('./server');
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
test('accepts only fresh, healthy live state with the complete agent registry',()=>{
  const now=Date.parse('2026-10-09T20:00:00Z');
  const live={...snapshot,live:true,runtime_verified:false,captured_at:'2026-10-09T19:59:00Z',control_plane:{status:'online',database:'connected',version:'2.7.1'}};
  const state=validateLiveState(live,{now});
  assert.equal(state.live,true);assert.equal(state.source,'control-plane-api');
  assert.throws(()=>validateLiveState({...live,captured_at:'2026-10-09T19:57:59Z'},{now}),/stale/);
  assert.throws(()=>validateLiveState({...live,live:false},{now}),/not live/);
  assert.throws(()=>validateLiveState({...live,agents:live.agents.slice(1)},{now}),/agent registry/);
  assert.throws(()=>validateLiveState({...live,control_plane:{status:'offline',database:'connected'}},{now}),/unhealthy/);
  assert.throws(()=>controlPlaneEndpoint('http://control-plane.example'),/HTTPS/);
});
test('live API requires bearer auth and stale upstream data falls back closed',async()=>{
  const oldUrl=process.env.CONTROL_PLANE_API_URL,oldToken=process.env.CONTROL_PLANE_API_TOKEN;
  let authorization;
  const upstream=http.createServer((req,res)=>{authorization=req.headers.authorization;res.writeHead(200,{'content-type':'application/json'});res.end(JSON.stringify({...snapshot,live:true,captured_at:'2026-10-09T00:00:00Z',control_plane:{status:'online',database:'connected',version:'2.7.1'}}));});
  await new Promise(resolve=>upstream.listen(0,'127.0.0.1',resolve));
  process.env.CONTROL_PLANE_API_URL='http://127.0.0.1:'+upstream.address().port;
  process.env.CONTROL_PLANE_API_TOKEN='test-token';
  const server=createServer();await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  try{
    const state=await(await fetch('http://127.0.0.1:'+server.address().port+'/api/control-plane')).json();
    assert.equal(authorization,'Bearer test-token');assert.equal(state.live,false);assert.equal(state.connection_status,'unavailable');
    delete process.env.CONTROL_PLANE_API_TOKEN;
    const missing=await(await fetch('http://127.0.0.1:'+server.address().port+'/api/control-plane')).json();
    assert.equal(missing.connection_status,'missing-token');
  }finally{
    await new Promise(resolve=>server.close(resolve));await new Promise(resolve=>upstream.close(resolve));
    if(oldUrl===undefined)delete process.env.CONTROL_PLANE_API_URL;else process.env.CONTROL_PLANE_API_URL=oldUrl;
    if(oldToken===undefined)delete process.env.CONTROL_PLANE_API_TOKEN;else process.env.CONTROL_PLANE_API_TOKEN=oldToken;
  }
});
