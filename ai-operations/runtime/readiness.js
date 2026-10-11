'use strict';

function evaluateRuntimeReadiness(state,{capabilities={},runtimeIdentity=null,lease=null,now=Date.now()}={}){
  const nowMs=new Date(now).getTime();
  const checks={
    live_state:state?.live===true,
    runtime_verified:state?.runtime_verified===true,
    expected_version:capabilities.expected_version===true,
    atomic_compare_and_swap:capabilities.atomic_compare_and_swap===true,
    lease_backend:capabilities.lease_backend===true,
    fenced_work_packet_persistence:capabilities.fenced_work_packet_persistence===true,
    legacy_delivery_writes_blocked:capabilities.legacy_delivery_writes_blocked===true,
    runtime_identity:typeof runtimeIdentity==='string'&&runtimeIdentity.trim().length>0,
    active_lease:Number.isFinite(nowMs)&&Boolean(lease?.owner)&&lease.owner===runtimeIdentity&&Date.parse(lease.expires_at)>nowMs
  };
  const reasons=Object.entries(checks).filter(([,ok])=>!ok).map(([name])=>name.replaceAll('_','-')+'-required');
  return {ready:reasons.length===0,dispatcher_enabled:reasons.length===0,checks,reasons};
}

module.exports={evaluateRuntimeReadiness};
