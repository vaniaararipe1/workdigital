import {test} from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {createLeaseHandler} from './lease-handler.mjs';
const require=createRequire(import.meta.url);
const {createHttpLeaseStore}=require('../http-lease-store');
const {claimLease,releaseLease}=require('../lease');
const document={version:1,owner:'run-a',acquired_at:'2026-10-09T12:00:00.000Z',expires_at:'2026-10-09T12:01:00.000Z'};
function request(method='GET',headers={},body) {
  return new Request('https://control.example/runtime/lease',{method,headers,body});
}
const writeHeaders={'if-match':'"lease-v0"','x-lease-owner':'run-a'};
test('backend requires authentication before exposing any lease data',async()=>{
  assert.throws(()=>createLeaseHandler(),/authentication/);
  const handler=createLeaseHandler({authenticate:async()=>null});
  assert.equal((await handler(request())).status,401);
  assert.equal((await handler(request('PUT'))).status,401);
});
test('GET uses the caller-bound RPC client and never caches state',async()=>{
  let call;
  const handler=createLeaseHandler({authenticate:async()=>({rpc:async(...args)=>{call=args;return {data:{version:0,owner:null}};}})});
  const response=await handler(request());
  assert.equal(response.status,200);assert.equal(response.headers.get('etag'),'"lease-v0"');
  assert.equal(response.headers.get('cache-control'),'no-store');
  assert.deepEqual(call,['wd_read_runtime_lease',{}]);
});
test('PUT preserves the version fence and caller runtime identity',async()=>{
  let call;
  const handler=createLeaseHandler({authenticate:async()=>({rpc:async(...args)=>{call=args;return {data:{applied:true,lease:document}};}})});
  const response=await handler(request('PUT',writeHeaders,JSON.stringify(document)));
  assert.equal(response.status,200);
  assert.deepEqual(call,['wd_cas_runtime_lease',{p_expected_version:0,p_request_owner:'run-a',p_next:document}]);
});
test('malformed versions, clocks and owners are rejected before RPC',async()=>{
  let calls=0;
  const handler=createLeaseHandler({authenticate:async()=>({rpc:async()=>{calls++;return {};}})});
  assert.equal((await handler(request('PUT',{},'{}'))).status,428);
  for(const value of [
    {...document,version:2},{...document,owner:'run-b'},
    {...document,expires_at:'infinity'},{...document,owner:null},
    {...document,acquired_at:'2026-02-30T12:00:00.000Z'},[],
  ]) assert.equal((await handler(request('PUT',writeHeaders,JSON.stringify(value)))).status,400);
  assert.equal(calls,0);
});
test('bounded request body and unsupported methods fail closed',async()=>{
  let calls=0;
  const handler=createLeaseHandler({maxBodyBytes:16,authenticate:async()=>({rpc:async()=>{calls++;return {};}})});
  assert.equal((await handler(request('PUT',writeHeaders,JSON.stringify(document)))).status,413);
  assert.equal((await handler(request('DELETE'))).status,405);
  assert.equal(calls,0);
});
test('database conflicts, access denial and failure are distinguished without leaking errors',async()=>{
  for(const [result,status] of [
    [{data:{applied:false}},412],
    [{error:{code:'42501',message:'private detail'}},403],
    [{error:{code:'22023'}},400],
    [{error:{code:'unknown',message:'private detail'}},503],
    [{data:{}},503]
  ]) {
    const handler=createLeaseHandler({authenticate:async()=>({rpc:async()=>result})});
    const response=await handler(request('PUT',writeHeaders,JSON.stringify(document)));
    assert.equal(response.status,status);
    assert.ok(!(await response.text()).includes('private detail'));
  }
});
test('HTTP adapter completes acquire/contention/release against handler with an RPC double',async()=>{
  // This validates transport integration, NOT the PostgreSQL migration.
  let value={version:0,owner:null,acquired_at:null,expires_at:null};
  const writes=[];
  const handler=createLeaseHandler({authenticate:async req=>req.headers.get('authorization')==='Bearer test-token'?{
    rpc:async(name,args)=>{
      if(name==='wd_read_runtime_lease')return {data:structuredClone(value)};
      writes.push(args);
      if(args.p_expected_version!==value.version)return {data:{applied:false}};
      value=structuredClone(args.p_next);return {data:{applied:true,lease:value}};
    }
  }:null});
  const store=createHttpLeaseStore({
    baseUrl:'https://control.example',token:'test-token',
    fetchImpl:async(url,options)=>handler(new Request(url,options))
  });
  const now='2026-10-09T12:00:00.000Z';
  const acquired=await claimLease(store,{owner:'run-a',now});
  assert.equal(acquired.acquired,true);
  assert.equal((await claimLease(store,{owner:'run-b',now})).acquired,false);
  assert.equal((await releaseLease(store,{owner:'run-b',now})).released,false);
  assert.equal((await releaseLease(store,{owner:'run-a',now})).released,true);
  assert.equal(writes.at(-1).p_request_owner,'run-a');
  assert.equal(value.owner,null);assert.equal(value.version,2);
});
