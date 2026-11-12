'use strict';
// Navigation core reused from the shared deck; interactions are specific to this deck.
const stage=document.querySelector('#stage'),slides=[...document.querySelectorAll('.slide')];let current=0,singleTimer;
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
function fit(){stage.style.setProperty('--scale',Math.min(innerWidth/1920,innerHeight/1080));}
addEventListener('resize',fit);fit();
slides.forEach((s,i)=>{const b=document.createElement('button');b.setAttribute('aria-label',`${i+1}. ${s.dataset.title}`);b.title=s.dataset.title;b.addEventListener('click',()=>show(i));$('#dots').append(b)});
function show(n){current=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,i)=>{s.classList.toggle('active',i===current);s.setAttribute('aria-hidden',String(i!==current));s.inert=i!==current});stage.classList.toggle('cover-active',current===0);[...$('#dots').children].forEach((d,i)=>d.setAttribute('aria-current',String(i===current)));$('#prev').disabled=current===0;$('#next').disabled=current===slides.length-1;$('#announcer').textContent=`${current+1} of ${slides.length}: ${slides[current].dataset.title}`;document.title=`${slides[current].dataset.title} · This Week · GOES with X`;if(location.hash!==`#${current+1}`)history.replaceState(null,'',`#${current+1}`);}
$('#prev').onclick=()=>show(current-1);$('#next').onclick=()=>show(current+1);
function fullscreen(){if(document.fullscreenElement){document.exitFullscreen?.().catch(()=>{})}else{document.documentElement.requestFullscreen?.().catch(()=>{})}}
$('#fullscreen').onclick=fullscreen;
stage.addEventListener('dblclick',e=>{if(!e.target.closest('button'))fullscreen()});
// Background clicks navigate after a short delay so a double-click only toggles full screen.
stage.addEventListener('click',e=>{if(e.target.closest('button,a,input,[role=tab]')){clearTimeout(singleTimer);return}e.stopImmediatePropagation();if(e.detail>1){clearTimeout(singleTimer);return}const x=e.clientX;singleTimer=setTimeout(()=>{const r=stage.getBoundingClientRect();show(current+(x<r.left+r.width/2?-1:1))},260)},true);
addEventListener('keydown',e=>{if(e.key.toLowerCase()==='f'){e.preventDefault();fullscreen();return}if(e.target.closest('button')&&(e.key===' '||e.key==='Enter'))return;if(['ArrowRight',' ','PageDown'].includes(e.key)){e.preventDefault();show(current+1)}if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();show(current-1)}if(e.key==='Home')show(0);if(e.key==='End')show(slides.length-1)});
let touch;stage.addEventListener('touchstart',e=>{touch=e.target.closest('button')?null:{x:e.changedTouches[0].clientX,y:e.changedTouches[0].clientY}},{passive:true});stage.addEventListener('touchend',e=>{if(!touch)return;const dx=e.changedTouches[0].clientX-touch.x,dy=e.changedTouches[0].clientY-touch.y;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.3){e.preventDefault();clearTimeout(singleTimer);show(current+(dx<0?1:-1))}touch=null},{passive:false});
// Slide 2: tapping a standard shows that one module changes on its own.
const unlocksHTML=$('#std-response').innerHTML;
$$('.std').forEach(b=>b.onclick=()=>{const on=!b.classList.contains('updated');$$('.std').forEach(x=>{x.classList.remove('updated');x.setAttribute('aria-pressed','false');x.querySelector('em').textContent=x.querySelector('em').dataset.n||x.querySelector('em').textContent});const r=$('#std-response');if(on){const em=b.querySelector('em');em.dataset.n=em.dataset.n||em.textContent;em.textContent='✓ updated';b.classList.add('updated');b.setAttribute('aria-pressed','true');r.classList.add('note');r.innerHTML='';const p=document.createElement('p');const k=document.createElement('b');k.textContent='⇄';p.append(k,document.createTextNode(`Only the ${b.dataset.std.toLowerCase()} standard changes. Regenerate; nothing else moves.`));r.append(p)}else{r.classList.remove('note');r.innerHTML=unlocksHTML}});
$$('.std em').forEach(e=>e.dataset.n=e.textContent);
// Slide 3: tap a topic to light up everything it builds on (real prerequisite links).
const panel=$('#kg-panel'),nodes=$$('.kg-node'),edges=$$('.kg-edge');
function ancestors(id,acc=new Set()){const n=document.getElementById(id);(n.dataset.pre||'').split(' ').filter(Boolean).forEach(p=>{if(!acc.has(p)){acc.add(p);ancestors(p,acc)}});return acc}
function focusNode(id){const a=ancestors(id);panel.classList.add('focus');nodes.forEach(n=>{n.classList.toggle('sel',n.id===id);n.classList.toggle('anc',a.has(n.id));n.setAttribute('aria-pressed',String(n.id===id))});edges.forEach(e=>e.classList.toggle('on',(e.dataset.to===id||a.has(e.dataset.to))&&a.has(e.dataset.from)));const n=document.getElementById(id);const lanes=new Set([...a,id].map(x=>Math.round(parseFloat(document.getElementById(x).style.top))));$('#kg-response').textContent=a.size?`“${n.dataset.full}” builds on ${a.size} topic${a.size>1?'s':''}${lanes.size>1?`, across ${lanes.size} units`:''}.`:`“${n.dataset.full}” is a starting point: no prerequisites.`}
function clearFocus(){panel.classList.remove('focus');nodes.forEach(n=>{n.classList.remove('sel','anc');n.setAttribute('aria-pressed','false')});edges.forEach(e=>e.classList.remove('on'));$('#kg-response').textContent='Tap a topic to see what it builds on.'}
nodes.forEach(n=>n.onclick=()=>n.classList.contains('sel')?clearFocus():focusNode(n.id));
// Slide 4: two kinds of patch through the same loop.
function mode(m){$('#loop').dataset.mode=m;$('#decide-label').textContent=m==='content'?'No: an agent patches it':'Yes: a human reviews it';$('#patch-label').textContent=m==='content'?'The content':'The graph';$$('.action[data-mode]').forEach(b=>{const on=b.dataset.mode===m;b.classList.toggle('selected',on);b.setAttribute('aria-pressed',String(on))})}
$$('.action[data-mode]').forEach(b=>b.onclick=()=>mode(b.dataset.mode));
$$('button').forEach(b=>b.addEventListener('click',e=>e.stopPropagation()));
const defaultNode=nodes.find(n=>n.dataset.full.startsWith('Volume formula'));if(defaultNode)focusNode(defaultNode.id);
mode('content');show(Math.max(0,Math.min(slides.length-1,(parseInt(location.hash.slice(1))||1)-1)));
