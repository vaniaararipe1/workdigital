'use strict';
const fs=require('node:fs'),path=require('node:path'),{buildProjection}=require('../runtime/projection');

const chunks=[];
process.stdin.on('data',chunk=>chunks.push(chunk));
process.stdin.on('end',()=>{
  try{
    const input=JSON.parse(Buffer.concat(chunks).toString('utf8'));
    const projection=buildProjection(input);
    const target=process.argv[2];
    if(!target)return process.stdout.write(JSON.stringify(projection,null,2)+'\n');
    const resolved=path.resolve(target),temporary=resolved+'.tmp-'+process.pid;
    fs.writeFileSync(temporary,JSON.stringify(projection,null,2)+'\n',{mode:0o600});
    fs.renameSync(temporary,resolved);
    process.stdout.write(JSON.stringify({ok:true,target:resolved,captured_at:projection.captured_at})+'\n');
  }catch(error){process.stderr.write(error.message+'\n');process.exitCode=1;}
});
