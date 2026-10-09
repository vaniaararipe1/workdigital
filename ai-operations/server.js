'use strict';
const http=require('node:http'), fs=require('node:fs/promises'), path=require('node:path');
const snapshot=require('./snapshot.json');
const {planQueue}=require('./runtime/queue');
const capabilities=require('./runtime/control-plane-capabilities.json');
const {evaluateRuntimeReadiness}=require('./runtime/readiness');
const root=path.join(__dirname,'public');
function json(res,status,data){res.writeHead(status,{'content-type':'application/json; charset=utf-8','cache-control':'no-store'});res.end(JSON.stringify(data))}
function normalize(data){
  if(!data || ['agents','tasks','operations','work_packets'].some(k=>!Array.isArray(data[k])))throw Error('Invalid Control Plane snapshot');
  return {...data,agents:data.agents.map(a=>({...a,key:a.agent_key||a.key})),
    tasks:data.tasks.map(t=>({...t,key:t.task_key||t.key,owner:t.owner_agent||t.owner})),
    operations:data.operations.map(o=>({...o,key:o.operation_key||o.key})),
    work_packets:data.work_packets.map(p=>({...p,key:p.packet_key||p.key,destination:p.destination_agent||p.destination}))};
}
async function readState(){
  const base=process.env.CONTROL_PLANE_API_URL;
  if(base)try{
    const response=await fetch(base.replace(/\/$/,'')+'/snapshot',{headers:process.env.CONTROL_PLANE_API_TOKEN?{authorization:'Bearer '+process.env.CONTROL_PLANE_API_TOKEN}:{},signal:AbortSignal.timeout(5000)});
    if(!response.ok)throw Error('Unavailable');
    return {...normalize(await response.json()),source:'control-plane-api',live:true,fetched_at:new Date().toISOString()};
  }catch{return {...normalize(snapshot),source:snapshot.source||'historical-snapshot',live:false,connection_status:'unavailable'};}
  return {...normalize(snapshot),source:snapshot.source||'historical-snapshot',live:false,connection_status:'not-configured'};
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
    res.writeHead(200,{'content-type':types[path.extname(real)]||'application/octet-stream'});res.end(req.method==='HEAD'?undefined:bytes);
  }catch{json(res,404,{error:'not-found'});}
});}
if(require.main===module)createServer().listen(process.env.PORT||10000);
module.exports={createServer,normalize};
