'use strict';
const keys=new Set(['patricia','felipe','clara','larissa','bruno','marcelo','gabriel']);
const finished=new Set(['DONE','MEASURED','COMPLETED','CANCELLED']);
const key=x=>x.packet_key||x.task_key||x.operation_key||x.key||'';
const find=(items,ref)=>typeof ref==='string'&&ref.length?items.find(x=>x.id===ref||key(x)===ref):undefined;
function executionConstraint(c){return typeof c==='string'?c:Array.isArray(c)?c.join('\n'):String(c?.execution||'');}
// Pure planning: no state writes, model calls, claims or inferred approval.
function planQueue(state){
  for(const k of ['agents','operations','tasks','work_packets'])if(!Array.isArray(state[k]))throw TypeError('Missing '+k);
  const ready=[],blocked=[],review=[];
  for(const p of state.work_packets){
    if(/(^|-)TEST(-|$)/.test(key(p))||finished.has(p.status))continue;
    if(p.status==='REVIEW'){review.push({packet_key:key(p),action:'patricia-review'});continue;}
    const reasons=[],destination=p.destination_agent||p.destination;
    const agent=state.agents.find(a=>(a.agent_key||a.key)===destination);
    if(!keys.has(destination)||!agent||agent.status!=='active')reasons.push('agent-unavailable');
    const task=find(state.tasks,p.task_id||p.task);
    if(!task)reasons.push('task-missing');
    else{
      if(!['READY','IN_PROGRESS','EXECUTING','APPROVED'].includes(task.status))reasons.push('task-not-runnable');
      if(task.completed_at||finished.has(task.status))reasons.push('task-finished');
      if(task.constraints?.approval_required===true)reasons.push('explicit-approval-required');
      const deps=task.dependencies||[];
      if(!Array.isArray(deps))reasons.push('invalid-dependencies');
      else for(const dep of deps){
        const ref=typeof dep==='string'?dep:dep?.task_id||dep?.task_key;
        const t=find(state.tasks,ref);
        if(!t||!['DONE','MEASURED','COMPLETED'].includes(t.status))reasons.push('dependency-unresolved');
      }
      if(/não executar|não executada|aguarda work packet/i.test(executionConstraint(task.constraints)))reasons.push('constraint-reconciliation-required');
    }
    const op=find(state.operations,p.operation_id||task?.operation_id);
    if(!op||!['IN_PROGRESS','EXECUTING','APPROVED','READY'].includes(op.status))reasons.push('operation-not-runnable');
    if(p.received_at||p.completed_at||p.result)reasons.push('already-started-or-result-present');
    if(!['SENT','READY'].includes(p.status))reasons.push('packet-not-runnable');
    if(p.approval_required===true||p.action_scope==='external')reasons.push('explicit-approval-required');
    const entry={packet_key:key(p),destination_agent:destination,task_key:task?key(task):null};
    if(reasons.length)blocked.push({...entry,reasons:[...new Set(reasons)]});
    else ready.push({...entry,priority:Number.isFinite(task.priority)?task.priority:0});
  }
  ready.sort((a,b)=>b.priority-a.priority||a.packet_key.localeCompare(b.packet_key));
  return {mode:'read-only-plan',ready,blocked,review,concurrency_limit:1,runtime_verified:false,
    warning:'Re-read live state before dispatch. No atomic lease exposed; do not run concurrent dispatchers.'};
}
module.exports={planQueue};
