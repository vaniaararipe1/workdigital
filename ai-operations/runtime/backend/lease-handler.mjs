// Mount inside the existing OAuth-protected Control Plane, never in the public UI.
// authenticate(req) must return a Supabase client bound to the verified caller.
export function createLeaseHandler({authenticate, maxBodyBytes=4096}={}) {
  if(typeof authenticate!=='function') throw TypeError('Existing authentication middleware is required');
  const json=(status,value,headers={})=>new Response(JSON.stringify(value),{
    status,headers:{'content-type':'application/json','cache-control':'no-store',...headers}
  });
  return async function handle(req) {
    if(!new URL(req.url).pathname.endsWith('/runtime/lease')) return json(404,{error:'not-found'});
    if(!['GET','PUT'].includes(req.method)) return json(405,{error:'method-not-allowed'},{allow:'GET, PUT'});
    let client;
    try { client=await authenticate(req); } catch { return json(401,{error:'unauthorized'}); }
    if(!client||typeof client.rpc!=='function') return json(401,{error:'unauthorized'});
    let name='wd_read_runtime_lease',args={};
    if(req.method==='PUT') {
      const match=/^"lease-v(0|[1-9][0-9]*)"$/.exec(req.headers.get('if-match')||'');
      if(!match) return json(428,{error:'valid-if-match-required'});
      const expected=Number(match[1]),owner=req.headers.get('x-lease-owner');
      if(!Number.isSafeInteger(expected)||!owner?.trim()||owner.length>200) return json(400,{error:'invalid-lease-write'});
      const reader=req.body?.getReader();
      if(!reader) return json(400,{error:'invalid-json'});
      let bytes=0,chunks=[];
      try {
        while(true) {
          const {done,value}=await reader.read(); if(done)break;
          bytes+=value.byteLength;
          if(bytes>maxBodyBytes){await reader.cancel();return json(413,{error:'body-too-large'});}
          chunks.push(value);
        }
        const all=new Uint8Array(bytes);let offset=0;
        for(const chunk of chunks){all.set(chunk,offset);offset+=chunk.byteLength;}
        const next=JSON.parse(new TextDecoder().decode(all));
        const validTime=value=>typeof value==='string'&&!Number.isNaN(Date.parse(value))&&new Date(value).toISOString()===value;
        if(!next||Array.isArray(next)||typeof next!=='object'||!Number.isSafeInteger(next.version)||next.version!==expected+1||
          !(next.owner===null||(typeof next.owner==='string'&&next.owner===owner))) {
          return json(400,{error:'invalid-lease-document'});
        }
        if(next.owner===null ? (next.acquired_at!==null||next.expires_at!==null) :
          (!validTime(next.acquired_at)||!validTime(next.expires_at)||Date.parse(next.expires_at)<=Date.parse(next.acquired_at))) {
          return json(400,{error:'invalid-lease-document'});
        }
        name='wd_cas_runtime_lease';args={p_expected_version:expected,p_request_owner:owner,p_next:next};
      } catch {return json(400,{error:'invalid-json'});}
    }
    try {
      const {data,error}=await client.rpc(name,args);
      if(error) {
        if(error.code==='42501') return json(403,{error:'forbidden'});
        if(['22023','22007','22008','22P02'].includes(error.code)) return json(400,{error:'invalid-lease-document'});
        return json(503,{error:'lease-backend-unavailable'});
      }
      if(req.method==='PUT') {
        if(data?.applied===false) return json(412,{error:'lease-conflict'});
        if(data?.applied!==true) return json(503,{error:'invalid-backend-response'});
        return json(200,data.lease);
      }
      if(!Number.isSafeInteger(data?.version)) return json(503,{error:'invalid-backend-response'});
      return json(200,data,{etag:'"lease-v'+data.version+'"'});
    } catch { return json(503,{error:'lease-backend-unavailable'}); }
  };
}
