'use strict';

function createHttpLeaseStore({baseUrl,token,fetchImpl=globalThis.fetch,timeoutMs=5_000}={}){
  if(typeof baseUrl!=='string'||!/^https:\/\//.test(baseUrl))throw TypeError('HTTPS Control Plane URL is required');
  if(typeof fetchImpl!=='function')throw TypeError('fetch implementation is required');
  const url=baseUrl.replace(/\/$/,'')+'/runtime/lease';
  const headers=()=>({accept:'application/json',...(token?{authorization:'Bearer '+token}:{})});
  async function request(method,extra={}){
    return fetchImpl(url,{method,headers:{...headers(),...extra.headers},body:extra.body,signal:AbortSignal.timeout(timeoutMs)});
  }
  return {
    async read(){
      const response=await request('GET');
      if(response.status===404)return null;
      if(!response.ok)throw Error('Lease read failed with '+response.status);
      const value=await response.json();
      if(!Number.isInteger(value?.version))throw Error('Lease response has no integer version');
      return value;
    },
    async compareAndSwap(expectedVersion,next){
      const response=await request('PUT',{headers:{'content-type':'application/json','if-match':'"lease-v'+expectedVersion+'"'},body:JSON.stringify(next)});
      if(response.status===409||response.status===412)return false;
      if(!response.ok)throw Error('Lease compare-and-swap failed with '+response.status);
      return true;
    }
  };
}

module.exports={createHttpLeaseStore};
