const fallbackPositions={bruno:[14,18],gabriel:[50,12],felipe:[86,18],clara:[14,76],larissa:[50,85],marcelo:[86,76],patricia:[50,48]};
let state=null,selected=null;
const qs=s=>document.querySelector(s), qsa=s=>[...document.querySelectorAll(s)];
const safe=(v,f='—')=>v||f;
function workFor(key){
  const task=state?.tasks?.find(t=>t.owner===key&&!['DONE','MEASURED','CANCELLED'].includes(t.status));
  if(task)return task.title;
  const packet=state?.work_packets?.find(p=>p.destination===key&&!['DONE','COMPLETED'].includes(p.status));
  if(packet)return packet.objective;
  return key==='patricia'?'Coordena fila, dependências e revisões.':'Disponível para nova atribuição interna.';
}
function renderAgents(){
  const host=qs('#agentNodes');host.innerHTML='';
  const ordered=[...state.agents.filter(a=>a.key!=='patricia'),state.agents.find(a=>a.key==='patricia')].filter(Boolean);
  ordered.forEach(a=>{const [x,y]=fallbackPositions[a.key]||[50,50];const hasWork=state.tasks.some(t=>t.owner===a.key&&!['DONE','MEASURED','CANCELLED'].includes(t.status));const b=document.createElement('button');b.className='agent-node'+(a.key==='patricia'?' center':'')+(hasWork?' has-work':'');b.style.left=x+'%';b.style.top=y+'%';b.innerHTML='<span class="avatar">'+a.name[0]+'</span><strong>'+a.name+'</strong><small>'+a.role+'</small>';b.onclick=()=>selectAgent(a,b);host.appendChild(b)});
  const pat=ordered.find(a=>a.key==='patricia');if(pat)selectAgent(pat,host.querySelector('.center'),false);
}
function selectAgent(a,node,open=false){selected=a;qsa('.agent-node').forEach(n=>n.classList.remove('selected'));node?.classList.add('selected');qs('#activityName').textContent=a.name+' · '+a.role;qs('#activityText').textContent=workFor(a.key);if(open)openDrawer()}
function openDrawer(){if(!selected)return;qs('#drawerAvatar').textContent=selected.name[0];qs('#drawerName').textContent=selected.name;qs('#drawerRole').textContent=selected.role;qs('#drawerSpecialty').textContent=selected.specialty||'Contrato especializado cadastrado.';qs('#drawerActivity').textContent=workFor(selected.key);qs('#drawer').classList.add('open');qs('#scrim').classList.add('open');qs('#drawer').setAttribute('aria-hidden','false')}
function closeDrawer(){qs('#drawer').classList.remove('open');qs('#scrim').classList.remove('open');qs('#drawer').setAttribute('aria-hidden','true')}
function card(title,description,status){return '<article class="data-card"><div><h3>'+title+'</h3><p>'+safe(description)+'</p></div><span class="tag '+(status==='DONE'?'done':'')+'">'+safe(status)+'</span></article>'}
function renderLists(){
  qs('#operationsList').innerHTML=state.operations.map(o=>card(o.key+' · '+o.name,'Coordenação: '+safe(o.coordinator),o.status)).join('');
  qs('#tasksList').innerHTML=state.tasks.map(t=>card(t.key+' · '+t.title,'Responsável: '+safe(t.owner)+' · Prioridade '+safe(String(t.priority))+(t.next_action?' · Próxima ação: '+t.next_action:''),t.status)).join('');
  qs('#packetsList').innerHTML=state.work_packets.map(p=>card(p.key+' → '+safe(p.destination),p.objective,p.status)).join('');
  qs('#agentCount').textContent=state.agents.length;qs('#operationCount').textContent=state.operations.filter(o=>o.status==='IN_PROGRESS').length;qs('#queueCount').textContent=state.tasks.filter(t=>!['DONE','MEASURED','CANCELLED'].includes(t.status)).length;
}
function switchView(name,button){qsa('.view').forEach(v=>v.classList.remove('active'));qsa('.nav-item').forEach(n=>n.classList.remove('active'));qs('#'+name+'View').classList.add('active');button.classList.add('active');const labels={space:['Equipe em movimento','Patrícia coordena especialistas, tarefas e dependências.'],operations:['Operações','Frentes ativas e histórico operacional.'],tasks:['Fila de trabalho','Prioridades, responsáveis e estados atuais.'],packets:['Work Packets','Transferências estruturadas entre os agentes.']};qs('#viewTitle').textContent=labels[name][0];qs('#viewSubtitle').textContent=labels[name][1]}
async function boot(){try{const r=await fetch('/api/control-plane');state=await r.json();if(!state.agents)throw Error();const live=Boolean(state.live);qs('#syncChip').classList.toggle('live',live);qs('.side-status').classList.toggle('live',live);qs('#syncChip').innerHTML='<i></i> '+(live?'Control Plane ao vivo':'snapshot verificado');qs('#sideState').textContent=live?'online':'snapshot de '+new Date(state.captured_at||Date.now()).toLocaleDateString('pt-BR');renderAgents();renderLists()}catch{qs('#syncChip').innerHTML='<i></i> estado indisponível';qs('#sideState').textContent='indisponível'}}
qsa('.nav-item').forEach(b=>b.onclick=()=>switchView(b.dataset.view,b));qs('#inspectAgent').onclick=()=>openDrawer();qs('#closeDrawer').onclick=closeDrawer;qs('#scrim').onclick=closeDrawer;document.addEventListener('keydown',e=>{if(e.key==='Escape')closeDrawer()});boot();

