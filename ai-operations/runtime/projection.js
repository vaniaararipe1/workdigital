'use strict';

const agentKeys=['patricia','felipe','clara','larissa','bruno','marcelo','gabriel'];
const isTest=value=>/(^|-)TEST(-|$)/i.test(value||'');
const key=(item,native)=>item[native]||item.key||'';

function buildProjection(input,{capturedAt=new Date().toISOString()}={}){
  if(!input?.health?.ok||input.health.database!=='connected')throw Error('Control Plane is not healthy');
  for(const name of ['agents','operations','tasks','work_packets'])if(!Array.isArray(input[name]))throw TypeError('Missing '+name);

  const agents=input.agents.map(a=>({...a,key:key(a,'agent_key')}));
  const actual=[...new Set(agents.map(a=>a.key))].sort();
  const expected=[...agentKeys].sort();
  if(actual.length!==expected.length||actual.some((value,index)=>value!==expected[index]))throw Error('Unexpected agent registry');

  const operations=input.operations.filter(o=>!isTest(key(o,'operation_key'))).map(o=>({...o,key:key(o,'operation_key'),coordinator:o.coordinator_agent||o.coordinator}));
  const operationIds=new Set(operations.map(o=>o.id));
  const tasks=input.tasks.filter(t=>!isTest(key(t,'task_key'))&&operationIds.has(t.operation_id)).map(t=>({...t,key:key(t,'task_key'),owner:t.owner_agent||t.owner}));
  const taskIds=new Set(tasks.map(t=>t.id));
  const work_packets=input.work_packets.filter(p=>!isTest(key(p,'packet_key'))&&operationIds.has(p.operation_id)&&taskIds.has(p.task_id)).map(p=>({...p,key:key(p,'packet_key'),destination:p.destination_agent||p.destination}));

  return {
    schema_version:2,
    source:'chatgpt-control-plane-projection',
    live:false,
    captured_at:capturedAt,
    control_plane:{status:input.health.status, database:input.health.database, version:input.health.version},
    agents,operations,tasks,work_packets
  };
}

module.exports={buildProjection,agentKeys};
