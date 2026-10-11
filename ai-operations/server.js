'use strict';
const http=require('node:http'), fs=require('node:fs/promises'), path=require('node:path');
const {isDeepStrictEqual}=require('node:util');
const snapshot=require('./snapshot.json');
const agentConfiguration=require('./runtime/agents.json');
const {planQueue}=require('./runtime/queue');
const capabilities=require('./runtime/control-plane-capabilities.json');
const {evaluateRuntimeReadiness}=require('./runtime/readiness');
const root=path.join(__dirname,'public');
const agentContracts=new Map(agentConfiguration.agents.map(agent=>[agent.key,agent]));
const expectedAgents=[...agentContracts.keys()].sort();
const expectedSnapshotSchemaVersion=2;
const maxLiveStateAgeMs=2*60*1000;
const maxSnapshotBytes=1024*1024;
const technicalKey=/(^|-)TEST(?:-|$)/i;
const securityHeaders=Object.freeze({
  'content-security-policy':"default-src 'self'; base-uri 'none'; object-src 'none'; frame-ancestors 'none'; form-action 'none'; script-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self'",
  'cross-origin-opener-policy':'same-origin',
  'permissions-policy':'camera=(), geolocation=(), microphone=(), payment=()',
  'referrer-policy':'no-referrer',
  'x-content-type-options':'nosniff',
  'x-frame-options':'DENY'
});
function json(res,status,data){res.writeHead(status,{...securityHeaders,'content-type':'application/json; charset=utf-8','cache-control':'no-store'});res.end(JSON.stringify(data))}
function normalize(data){
  if(!data || ['agents','tasks','operations','work_packets'].some(k=>!Array.isArray(data[k])))throw Error('Invalid Control Plane snapshot');
  return {...data,agents:data.agents.map(a=>({...a,key:a.agent_key||a.key})),
    tasks:data.tasks.map(t=>({...t,key:t.task_key||t.key,owner:t.owner_agent||t.owner})),
    operations:data.operations.map(o=>({...o,key:o.operation_key||o.key})),
    work_packets:data.work_packets.map(p=>({...p,key:p.packet_key||p.key,destination:p.destination_agent||p.destination}))};
}
function indexLiveRecords(records,label){
  const ids=new Set(),keys=new Set();
  for(const record of records){
    if(typeof record?.id!=='string'||!record.id.trim()||typeof record?.key!=='string'||!record.key.trim())throw Error(`Invalid ${label} identity`);
    if(technicalKey.test(record.key))throw Error(`Technical ${label} record is not allowed`);
    if(ids.has(record.id)||keys.has(record.key))throw Error(`Duplicate ${label} identity`);
    ids.add(record.id);keys.add(record.key);
  }
  return ids;
}
function validateLiveGraph(state){
  indexLiveRecords(state.agents,'agent');
  const agentKeys=new Set(state.agents.map(agent=>agent.key));
  for(const agent of state.agents){
    const contract=agentContracts.get(agent.key);
    if(!contract||agent.name!==contract.name||agent.role!==contract.role||agent.specialty!==contract.specialty)throw Error('Unexpected agent contract');
    if(!isDeepStrictEqual(agent.permissions,contract.permissions))throw Error('Unexpected agent permissions');
  }
  const operationIds=indexLiveRecords(state.operations,'operation');
  const taskIds=indexLiveRecords(state.tasks,'task');
  indexLiveRecords(state.work_packets,'work packet');
  const tasksById=new Map(state.tasks.map(task=>[task.id,task]));
  for(const operation of state.operations)if(operation.coordinator_agent&&!agentKeys.has(operation.coordinator_agent))throw Error('Unknown operation coordinator in Control Plane snapshot');
  for(const task of state.tasks){
    if(!operationIds.has(task.operation_id))throw Error('Orphan task in Control Plane snapshot');
    if(task.owner&&!agentKeys.has(task.owner))throw Error('Unknown task owner in Control Plane snapshot');
  }
  for(const packet of state.work_packets){
    const task=tasksById.get(packet.task_id);
    if(!operationIds.has(packet.operation_id)||!task||task.operation_id!==packet.operation_id)throw Error('Orphan work packet in Control Plane snapshot');
    if(packet.source_agent&&!agentKeys.has(packet.source_agent))throw Error('Unknown work packet source in Control Plane snapshot');
    if(packet.destination&&!agentKeys.has(packet.destination))throw Error('Unknown work packet destination in Control Plane snapshot');
  }
  return state;
}
function validateLiveState(data,{now=Date.now()}={}){
  const state=normalize(data);
  const capturedAt=Date.parse(state.captured_at);
  const agentKeys=state.agents.map(agent=>agent.key),agents=[...new Set(agentKeys)].sort();
  if(state.live!==true)throw Error('Control Plane snapshot is not live');
  if(state.schema_version!==expectedSnapshotSchemaVersion)throw Error('Unexpected snapshot schema version');
  if(!Number.isFinite(capturedAt)||capturedAt>now+30_000||now-capturedAt>maxLiveStateAgeMs)throw Error('Control Plane snapshot is stale');
  if(state.control_plane?.status!=='online'||state.control_plane?.database!=='connected')throw Error('Control Plane is unhealthy');
  if(state.control_plane?.version!==capabilities.control_plane_version)throw Error('Unexpected Control Plane version');
  if(agentKeys.length!==expectedAgents.length||agents.length!==expectedAgents.length||agents.some((agent,index)=>agent!==expectedAgents[index]))throw Error('Unexpected agent registry');
  validateLiveGraph(state);
  return {...state,source:'control-plane-api',runtime_verified:false,fetched_at:new Date(now).toISOString()};
}
function controlPlaneEndpoint(base){
  const endpoint=new URL(base);
  if(endpoint.protocol!=='https:'&&!['127.0.0.1','localhost','::1'].includes(endpoint.hostname))throw Error('Control Plane API must use HTTPS');
  if(endpoint.username||endpoint.password)throw Error('Control Plane API URL cannot contain credentials');
  endpoint.hash='';endpoint.search='';
  const path=endpoint.pathname.replace(/\/+$/,'');
  endpoint.pathname=path.endsWith('/snapshot')?path:path+'/snapshot';
  return endpoint;
}
async function readJsonResponse(response){
  const type=(response.headers.get('content-type')||'').split(';',1)[0].trim().toLowerCase();
  if(type!=='application/json'&&!type.endsWith('+json'))throw Error('Control Plane response must be JSON');
  const declared=Number(response.headers.get('content-length'));
  if(Number.isFinite(declared)&&declared>maxSnapshotBytes)throw Error('Control Plane response is too large');
  const reader=response.body?.getReader();
  if(!reader)return response.json();
  const chunks=[];let total=0;
  for(;;){
    const {done,value}=await reader.read();if(done)break;
    total+=value.byteLength;if(total>maxSnapshotBytes){await reader.cancel();throw Error('Control Plane response is too large');}
    chunks.push(Buffer.from(value));
  }
  return JSON.parse(Buffer.concat(chunks,total).toString('utf8'));
}
function historicalState(connectionStatus,data=snapshot){
  const state=normalize(data);
  return {...state,source:state.source||'historical-snapshot',live:false,runtime_verified:false,connection_status:connectionStatus};
}
async function readState(){
  const base=process.env.CONTROL_PLANE_API_URL;
  const token=process.env.CONTROL_PLANE_API_TOKEN;
  if(base&&token)try{
    const response=await fetch(controlPlaneEndpoint(base),{headers:{authorization:'Bearer '+token,accept:'application/json'},redirect:'error',signal:AbortSignal.timeout(5000)});
    if(!response.ok)throw Error('Unavailable');
    return validateLiveState(await readJsonResponse(response));
  }catch{return historicalState('unavailable');}
  if(base&&!token)return historicalState('missing-token');
  return historicalState('not-configured');
}
function createServer(){return http.createServer(async(req,res)=>{
  if(!['GET','HEAD'].includes(req.method))return json(res,405,{error:'method-not-allowed'});
  const route=req.url.split('?')[0];
  if(route==='/health')return json(res,200,{ok:true,service:'ai-operations-interface',runtime:'not-connected'});
  if(route==='/api/control-plane')return json(res,200,await readState());
  if(route==='/api/runtime-readiness'){
    const state=await readState();
    return json(res,200,{source:state.source,capabilities,readiness:evaluateRuntimeReadiness(state,{capabilities})});
  }
  if(route==='/api/queue'){
    const state=await readState();
    const readiness=evaluateRuntimeReadiness(state,{capabilities});
    if(!readiness.ready)return json(res,503,{error:'runtime-not-ready',source:state.source,readiness});
    return json(res,200,{source:state.source,executable:false,plan:planQueue(state)});
  }
  let relative;try{relative=decodeURIComponent(route).replace(/^\/+/, '')||'index.html';}catch{return json(res,400,{error:'invalid-path'});}
  const file=path.resolve(root,relative);
  if(!file.startsWith(root+path.sep))return json(res,403,{error:'forbidden'});
  try{
    const real=await fs.realpath(file);
    if(!real.startsWith(root+path.sep))return json(res,403,{error:'forbidden'});
    const bytes=await fs.readFile(real),types={'.html':'text/html; charset=utf-8','.js':'application/javascript','.css':'text/css'};
    res.writeHead(200,{...securityHeaders,'content-type':types[path.extname(real)]||'application/octet-stream','cache-control':'no-cache'});res.end(req.method==='HEAD'?undefined:bytes);
  }catch{json(res,404,{error:'not-found'});}
});}
if(require.main===module)createServer().listen(process.env.PORT||10000);
module.exports={createServer,normalize,validateLiveState,validateLiveGraph,historicalState,controlPlaneEndpoint,readJsonResponse,securityHeaders};
