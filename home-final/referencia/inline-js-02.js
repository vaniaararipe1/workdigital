
// A seleção inicial termina na primeira interação e não é restaurada.
const wdExplore=document.getElementById('wd-explore');
const wdExploreCards=[...wdExplore.querySelectorAll('.wd-explore-card')];
let wdExploreInteracted=false;
function wdExploreClearInitial(){
 if(wdExploreInteracted)return;
 wdExploreInteracted=true;
 wdExploreCards.forEach(card=>card.classList.remove('is-active'));
 wdExploreCards.forEach(card=>{
  card.removeEventListener('mouseenter',wdExploreClearInitial);
  card.removeEventListener('focusin',wdExploreClearInitial);
 });
}
wdExploreCards.forEach(card=>{
 card.addEventListener('mouseenter',wdExploreClearInitial,{once:true});
 card.addEventListener('focusin',wdExploreClearInitial,{once:true});
});
document.querySelectorAll('[data-wd-explore-url]').forEach(link=>{
 const target=document.getElementById(link.getAttribute('href').slice(1));
 if(!target)link.href=link.dataset.wdExploreUrl;
});
