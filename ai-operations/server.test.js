'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),http=require('node:http'),snapshot=require('./snapshot.json'),{createServer,normalize,validateLiveState,historicalState,controlPlaneEndpoint}=require('./server');
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
test('historical fallback cannot certify live state or runtime execution',()=>{
  const poisoned={...snapshot,live:true,runtime_verified:true,source:''};
  const state=historicalState('unavailable',poisoned);
  assert.equal(state.live,false);assert.equal(state.runtime_verified,false);
  assert.equal(state.source,'historical-snapshot');assert.equal(state.connection_status,'unavailable');
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
test('rejects duplicate, technical and relationally inconsistent live records',()=>{
  const now=Date.parse('2026-10-09T20:00:00Z');
  const live=()=>structuredClone({...snapshot,live:true,captured_at:'2026-10-09T19:59:00Z',control_plane:{status:'online',database:'connected',version:'2.8.1'}});
  const duplicate=live();duplicate.tasks.push({...duplicate.tasks[0]});
  assert.throws(()=>validateLiveState(duplicate,{now}),/Duplicate task identity/);
  const technical=live();technical.operations[0].operation_key=technical.operations[0].key='OP-TEST-001';
  assert.throws(()=>validateLiveState(technical,{now}),/Technical operation record/);
  const orphanTask=live();orphanTask.tasks[0].operation_id='missing-operation';
  assert.throws(()=>validateLiveState(orphanTask,{now}),/Orphan task/);
  const mismatchedPacket=live();mismatchedPacket.work_packets[0].operation_id=mismatchedPacket.operations[0].id;
  assert.throws(()=>validateLiveState(mismatchedPacket,{now}),/Orphan work packet/);
});
test('rejects incompatible schemas and unknown agent references',()=>{
  const now=Date.parse('2026-10-09T20:00:00Z');
  const live=()=>structuredClone({...snapshot,live:true,captured_at:'2026-10-09T19:59:00Z',control_plane:{status:'online',database:'connected',version:'2.8.1'}});
  const incompatible=live();incompatible.schema_version=3;
  assert.throws(()=>validateLiveState(incompatible,{now}),/snapshot schema version/);
  const duplicateAgentId=live();duplicateAgentId.agents[1].id=duplicateAgentId.agents[0].id;
  assert.throws(()=>validateLiveState(duplicateAgentId,{now}),/Duplicate agent identity/);
  const unknownOwner=live();unknownOwner.tasks[0].owner_agent=unknownOwner.tasks[0].owner='unknown-agent';
  assert.throws(()=>validateLiveState(unknownOwner,{now}),/Unknown task owner/);
  const unknownDestination=live();unknownDestination.work_packets[0].destination_agent=unknownDestination.work_packets[0].destination='unknown-agent';
  assert.throws(()=>validateLiveState(unknownDestination,{now}),/Unknown work packet destination/);
});
test('rejects agent identity or permission drift from the versioned contracts',()=>{
  const now=Date.parse('2026-10-09T20:00:00Z');
  const live=()=>structuredClone({...snapshot,live:true,captured_at:'2026-10-09T19:59:00Z',control_plane:{status:'online',database:'connected',version:'2.8.1'}});
  const changedRole=live();changedRole.agents.find(agent=>agent.key==='gabriel').role='Direção de Arte';
  assert.throws(()=>validateLiveState(changedRole,{now}),/Unexpected agent contract/);
  const escalated=live();escalated.agents.find(agent=>agent.key==='felipe').permissions.external_contact=true;
  assert.throws(()=>validateLiveState(escalated,{now}),/Unexpected agent permissions/);
});
test('rejects invalid, cross-operation and cyclic task relationships',()=>{
  const now=Date.parse('2026-10-09T20:00:00Z');
  const live=()=>structuredClone({...snapshot,live:true,captured_at:'2026-10-09T19:59:00Z',control_plane:{status:'online',database:'connected',version:'2.8.1'}});
  const missing=live();missing.tasks[0].dependencies=[{task_key:'TASK-MISSING'}];
  assert.throws(()=>validateLiveState(missing,{now}),/Invalid task dependency/);
  const mismatch=live();mismatch.tasks[0].dependencies=[{task_id:mismatch.tasks[1].id,task_key:mismatch.tasks[2].key}];
  assert.throws(()=>validateLiveState(mismatch,{now}),/Mismatched task dependency/);
  const crossOperation=live();crossOperation.tasks[0].operation_id=crossOperation.operations[0].id;crossOperation.tasks[0].dependencies=[{task_id:crossOperation.tasks[1].id}];
  assert.throws(()=>validateLiveState(crossOperation,{now}),/Invalid task dependency/);
  const cyclic=live();cyclic.tasks[0].dependencies=[{task_id:cyclic.tasks[1].id}];cyclic.tasks[1].dependencies=[{task_id:cyclic.tasks[0].id}];
  assert.throws(()=>validateLiveState(cyclic,{now}),/Cyclic task dependencies/);
  const parentCycle=live();parentCycle.tasks[0].parent_task_id=parentCycle.tasks[1].id;parentCycle.tasks[1].parent_task_id=parentCycle.tasks[0].id;
  assert.throws(()=>validateLiveState(parentCycle,{now}),/Cyclic task parents/);
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
test('live API rejects redirects and non-JSON responses without following the token',async()=>{
  const oldUrl=process.env.CONTROL_PLANE_API_URL,oldToken=process.env.CONTROL_PLANE_API_TOKEN;
  let mode='redirect',redirected=false;
  const upstream=http.createServer((req,res)=>{
    if(req.url==='/redirected'){redirected=true;res.writeHead(200,{'content-type':'application/json'});return res.end('{}');}
    if(mode==='redirect'){res.writeHead(302,{location:'/redirected'});return res.end();}
    res.writeHead(200,{'content-type':'text/html'});res.end(JSON.stringify(snapshot));
  });
  await new Promise(resolve=>upstream.listen(0,'127.0.0.1',resolve));
  process.env.CONTROL_PLANE_API_URL='http://127.0.0.1:'+upstream.address().port;
  process.env.CONTROL_PLANE_API_TOKEN='test-token';
  const server=createServer();await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const base='http://127.0.0.1:'+server.address().port;
  try{
    const redirectedState=await(await fetch(base+'/api/control-plane')).json();
    assert.equal(redirectedState.live,false);assert.equal(redirectedState.connection_status,'unavailable');assert.equal(redirected,false);
    mode='html';const htmlState=await(await fetch(base+'/api/control-plane')).json();
    assert.equal(htmlState.live,false);assert.equal(htmlState.connection_status,'unavailable');
  }finally{
    await new Promise(resolve=>server.close(resolve));await new Promise(resolve=>upstream.close(resolve));
    if(oldUrl===undefined)delete process.env.CONTROL_PLANE_API_URL;else process.env.CONTROL_PLANE_API_URL=oldUrl;
    if(oldToken===undefined)delete process.env.CONTROL_PLANE_API_TOKEN;else process.env.CONTROL_PLANE_API_TOKEN=oldToken;
  }
});
