'use strict';

function evaluateRuntimeReadiness(state,{capabilities={},runtimeIdentity=null,lease=null}={}){
  const checks={
    live_state:state?.live===true,
    runtime_verified:state?.runtime_verified===true,
    atomic_compare_and_swap:capabilities.atomic_compare_and_swap===true,
    lease_backend:capabilities.lease_backend===true,
    runtime_identity:typeof runtimeIdentity==='string'&&runtimeIdentity.length>0,
    active_lease:Boolean(lease?.owner)&&lease.owner===runtimeIdentity&&Date.parse(lease.expires_at)>Date.now()
  };
  const reasons=Object.entries(checks).filter(([,ok])=>!ok).map(([name])=>name.replaceAll('_','-')+'-required');
  return {ready:reasons.length===0,dispatcher_enabled:reasons.length===0,checks,reasons};
}

module.exports={evaluateRuntimeReadiness};
