'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),http=require('node:http'),snapshot=require('./snapshot.json'),{createServer,normalize,validateLiveState,controlPlaneEndpoint}=require('./server');
const capabilities=require('./runtime/control-plane-capabilities.json');
const {evaluateRuntimeReadiness}=require('./runtime/readiness');
test('serves a restrictive browser security boundary on UI and API responses',async()=>{
  const server=createServer();await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const base='http://127.0.0.1:'+server.address().port;
  try{
    for(const route of ['/','/api/control-plane']){
      const response=await fetch(base+route),csp=response.headers.get('content-security-policy');
      assert.equal(response.headers.get('x-content-type-options'),'nosniff');
      assert.equal(response.headers.get('x-frame-options'),'DENY');
      assert.equal(response.headers.get('referrer-policy'),'no-referrer');
      assert.equal(response.headers.get('cross-origin-opener-policy'),'same-origin');
      assert.match(response.headers.get('permissions-policy'),/camera=\(\)/);
      assert.match(csp,/default-src 'self'/);assert.match(csp,/frame-ancestors 'none'/);assert.match(csp,/object-src 'none'/);assert.match(csp,/connect-src 'self'/);
    }
  }finally{await new Promise(resolve=>server.close(resolve));}
});
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
test('bundled historical projection matches the deployed Control Plane and excludes test records',()=>{
  assert.equal(snapshot.control_plane.version,capabilities.control_plane_version);
  assert.equal(snapshot.live,false);assert.equal(snapshot.runtime_verified,false);
  assert.deepEqual(snapshot.agents.map(agent=>agent.key).sort(),['bruno','clara','felipe','gabriel','larissa','marcelo','patricia']);
  const records=[...snapshot.operations,...snapshot.tasks,...snapshot.work_packets];
  assert.equal(records.filter(item=>/(^|-)TEST(-|$)/i.test(item.key||'')).length,0);
});
test('accepts only fresh, healthy live state with the complete agent registry',()=>{
  const now=Date.parse('2026-10-09T20:00:00Z');
  const live={...snapshot,live:true,runtime_verified:false,captured_at:'2026-10-09T19:59:00Z',control_plane:{status:'online',database:'connected',version:'2.8.1'}};
  const state=validateLiveState(live,{now});
  assert.equal(state.live,true);assert.equal(state.source,'control-plane-api');
  assert.throws(()=>validateLiveState({...live,captured_at:'2026-10-09T19:57:59Z'},{now}),/stale/);
  assert.throws(()=>validateLiveState({...live,live:false},{now}),/not live/);
  assert.throws(()=>validateLiveState({...live,agents:live.agents.slice(1)},{now}),/agent registry/);
  assert.throws(()=>validateLiveState({...live,agents:[...live.agents,live.agents[0]]},{now}),/agent registry/);
  assert.throws(()=>validateLiveState({...live,control_plane:{status:'offline',database:'connected'}},{now}),/unhealthy/);
  assert.throws(()=>validateLiveState({...live,control_plane:{status:'online',database:'connected',version:'2.8.0'}},{now}),/Control Plane version/);
  assert.throws(()=>controlPlaneEndpoint('http://control-plane.example'),/HTTPS/);
});
test('a live snapshot cannot certify the autonomous runtime',()=>{
  const now=Date.parse('2026-10-09T20:00:00Z');
  const claimed={...snapshot,live:true,runtime_verified:true,captured_at:'2026-10-09T19:59:00Z',control_plane:{status:'online',database:'connected',version:'2.8.1'}};
  const state=validateLiveState(claimed,{now});
  assert.equal(state.live,true);assert.equal(state.runtime_verified,false);
  const readiness=evaluateRuntimeReadiness(state,{capabilities,runtimeIdentity:'run-a',lease:{owner:'run-a',expires_at:'2026-10-09T20:01:00Z'}});
  assert.equal(readiness.ready,false);assert.ok(readiness.reasons.includes('runtime-verified-required'));
});
test('snapshot endpoint preserves the nested Supabase Edge Function path',()=>{
  const base='https://example.supabase.co/functions/v1/work-digital-mcp-v2';
  assert.equal(controlPlaneEndpoint(base).href,base+'/snapshot');
  assert.equal(controlPlaneEndpoint(base+'/snapshot?ignored=true#fragment').href,base+'/snapshot');
  assert.throws(()=>controlPlaneEndpoint('https://user:secret@example.supabase.co/functions/v1/work-digital-mcp-v2'),/credentials/);
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
