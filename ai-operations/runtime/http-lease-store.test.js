'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const {createHttpLeaseStore}=require('./http-lease-store');

test('reads the durable lease endpoint with bearer auth',async()=>{
  let request;
  const store=createHttpLeaseStore({baseUrl:'https://control.example',token:'secret',fetchImpl:async(url,options)=>{request={url,options};return new Response(JSON.stringify({version:2,owner:null}),{status:200,headers:{'content-type':'application/json'}});}});
  assert.equal((await store.read()).version,2);assert.equal(request.url,'https://control.example/runtime/lease');assert.equal(request.options.headers.authorization,'Bearer secret');
});
test('sends expected version as If-Match and maps conflicts to false',async()=>{
  let request;
  const store=createHttpLeaseStore({baseUrl:'https://control.example',fetchImpl:async(url,options)=>{request={url,options};return new Response(null,{status:412});}});
  assert.equal(await store.compareAndSwap(7,{version:8,owner:'run-a'}),false);assert.equal(request.options.headers['if-match'],'"lease-v7"');
});
test('rejects insecure endpoints and malformed lease responses',async()=>{
  assert.throws(()=>createHttpLeaseStore({baseUrl:'http://control.example'}),/HTTPS/);
  const store=createHttpLeaseStore({baseUrl:'https://control.example',fetchImpl:async()=>new Response('{}',{status:200,headers:{'content-type':'application/json'}})});
  await assert.rejects(()=>store.read(),/integer version/);
});
