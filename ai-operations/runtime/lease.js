'use strict';

const {planQueue}=require('./queue');

const iso=value=>new Date(value).toISOString();
const validTime=value=>typeof value==='string'&&!Number.isNaN(Date.parse(value));

function validateStore(store){
  if(!store||typeof store.read!=='function'||typeof store.compareAndSwap!=='function'){
    throw TypeError('Atomic lease store with read and compareAndSwap is required');
  }
}

function normalizeLease(value){
  if(value==null)return {version:0,owner:null,acquired_at:null,expires_at:null};
  if(!Number.isInteger(value.version)||value.version<0)throw TypeError('Invalid lease version');
  if(value.owner!==null&&typeof value.owner!=='string')throw TypeError('Invalid lease owner');
  if(value.owner&&(!validTime(value.acquired_at)||!validTime(value.expires_at)))throw TypeError('Invalid lease timestamps');
  return {...value};
}

function leaseIsActive(lease,now){
  return Boolean(lease.owner)&&Date.parse(lease.expires_at)>new Date(now).getTime();
}

async function claimLease(store,{owner,ttlMs=60_000,now=new Date(),maxAttempts=3}={}){
  validateStore(store);
  if(typeof owner!=='string'||!owner.trim())throw TypeError('Runtime owner is required');
  if(!Number.isInteger(ttlMs)||ttlMs<1_000)throw RangeError('Lease ttlMs must be at least 1000');
  const acquiredAt=new Date(now);
  if(Number.isNaN(acquiredAt.getTime()))throw TypeError('Invalid lease clock');
  for(let attempt=0;attempt<maxAttempts;attempt+=1){
    const current=normalizeLease(await store.read());
    if(leaseIsActive(current,acquiredAt)&&current.owner!==owner){
      return {acquired:false,reason:'lease-held',lease:current};
    }
    const next={version:current.version+1,owner,acquired_at:iso(acquiredAt),expires_at:iso(acquiredAt.getTime()+ttlMs)};
    if(await store.compareAndSwap(current.version,next,{owner}))return {acquired:true,lease:next};
  }
  return {acquired:false,reason:'lease-contention',lease:null};
}

async function releaseLease(store,{owner,now=new Date()}={}){
  validateStore(store);
  const current=normalizeLease(await store.read());
  if(!leaseIsActive(current,now)||current.owner!==owner)return {released:false,reason:'not-owner',lease:current};
  const next={version:current.version+1,owner:null,acquired_at:null,expires_at:null,released_at:iso(now)};
  return await store.compareAndSwap(current.version,next,{owner})
    ?{released:true,lease:next}
    :{released:false,reason:'lease-contention',lease:null};
}

async function heartbeatLease(store,{owner,lease,ttlMs=60_000,now=new Date()}={}){
  validateStore(store);
  if(typeof owner!=='string'||!owner.trim())throw TypeError('Runtime owner is required');
  if(!Number.isInteger(ttlMs)||ttlMs<1_000)throw RangeError('Lease ttlMs must be at least 1000');
  const beatAt=new Date(now);
  if(Number.isNaN(beatAt.getTime()))throw TypeError('Invalid lease clock');
  const expected=normalizeLease(lease);
  if(expected.owner!==owner)return {renewed:false,reason:'not-owner',lease:expected};
  if(!leaseIsActive(expected,beatAt))return {renewed:false,reason:'lease-expired',lease:expected};
  const current=normalizeLease(await store.read());
  if(current.version!==expected.version||current.owner!==owner){
    return {renewed:false,reason:'stale-fence',lease:current};
  }
  if(!leaseIsActive(current,beatAt))return {renewed:false,reason:'lease-expired',lease:current};
  const next={version:current.version+1,owner,acquired_at:iso(beatAt),expires_at:iso(beatAt.getTime()+ttlMs)};
  return await store.compareAndSwap(current.version,next,{owner})
    ?{renewed:true,lease:next,fence:{owner,version:next.version}}
    :{renewed:false,reason:'lease-contention',lease:null};
}

async function verifyLeaseFence(store,{owner,version,now=new Date()}={}){
  validateStore(store);
  if(typeof owner!=='string'||!owner.trim()||!Number.isSafeInteger(version)||version<1){
    throw TypeError('Valid runtime owner and fence version are required');
  }
  const current=normalizeLease(await store.read());
  if(current.owner!==owner)return {valid:false,reason:'not-owner',lease:current};
  if(current.version!==version)return {valid:false,reason:'stale-fence',lease:current};
  if(!leaseIsActive(current,now))return {valid:false,reason:'lease-expired',lease:current};
  return {valid:true,fence:{owner,version},lease:current};
}

function planLeasedDispatch(state,{lease,owner,now=new Date()}={}){
  const reasons=[];
  if(state?.live!==true)reasons.push('live-state-required');
  if(state?.runtime_verified!==true)reasons.push('runtime-verification-required');
  let current;
  try{current=normalizeLease(lease);}catch{reasons.push('valid-lease-required');}
  if(current&&(!leaseIsActive(current,now)||current.owner!==owner))reasons.push('active-owned-lease-required');
  if(reasons.length)return {mode:'dispatch-blocked',executable:false,reasons:[...new Set(reasons)],packet:null};
  const queue=planQueue(state);
  return {mode:'leased-dispatch-plan',executable:queue.ready.length>0,reasons:[],packet:queue.ready[0]||null,queue};
}

module.exports={claimLease,heartbeatLease,releaseLease,verifyLeaseFence,planLeasedDispatch,leaseIsActive};
