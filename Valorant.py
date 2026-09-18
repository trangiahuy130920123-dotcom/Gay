import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="NEON VALOR",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

GAME = r"""
<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>NEON VALOR</title>
<style>
*{box-sizing:border-box}html,body{margin:0;background:#070a10;color:#eaf4ff;font-family:Arial,sans-serif;overflow:hidden}
button{font:inherit;color:#fff;background:#101826;border:1px solid #31445d;border-radius:10px;padding:11px 15px;cursor:pointer}
button:hover{background:#172438;border-color:#6aa8ff}.hidden{display:none!important}
#app{height:100vh;min-height:560px;position:relative;background:radial-gradient(circle at 50% 20%,#12213c,#060910 60%)}
.screen{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.panel{background:rgba(8,13,23,.94);border:1px solid #263951;border-radius:18px;box-shadow:0 20px 70px #000a}
.menu{width:min(900px,94vw);padding:34px}.brand{font-size:48px;font-weight:900;letter-spacing:5px;color:#8fd3ff;text-shadow:0 0 25px #239cff}
.sub{color:#7f94ad;margin:5px 0 25px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.grid button{min-height:60px}
.full{width:100%;margin-top:12px}.back{margin-top:20px}
#game{position:absolute;inset:0;background:#020407}
canvas{position:absolute;inset:0;width:100%;height:100%;touch-action:none}
.hud{position:absolute;inset:0;pointer-events:none}.top{position:absolute;top:12px;left:12px;right:12px;display:flex;justify-content:space-between;font-weight:700}
.card{background:#07101ddd;border:1px solid #29405c;border-radius:9px;padding:8px 12px}
#cross{position:absolute;left:50%;top:50%;width:22px;height:22px;transform:translate(-50%,-50%)}
#cross:before,#cross:after{content:"";position:absolute;background:#dff4ff;box-shadow:0 0 8px #fff}
#cross:before{left:10px;top:2px;width:2px;height:18px}#cross:after{left:2px;top:10px;width:18px;height:2px}
.bottom{position:absolute;left:16px;right:16px;bottom:15px;display:flex;justify-content:space-between;align-items:end}
.hp{font-size:26px;font-weight:900}.ammo{font-size:28px;font-weight:900}
.controls{display:flex;gap:8px;pointer-events:auto}.controls button{width:55px;height:55px;padding:0}
#joy{position:absolute;left:22px;bottom:25px;width:140px;height:140px;border:2px solid #7692b055;border-radius:50%;background:#ffffff09;pointer-events:auto;display:none}
#knob{position:absolute;left:45px;top:45px;width:50px;height:50px;border-radius:50%;background:#9bcaff55;border:1px solid #bde0ff99}
.mobileBtns{position:absolute;right:18px;bottom:18px;display:none;gap:8px;pointer-events:auto}
.mobileBtns button{width:58px;height:58px;border-radius:50%;padding:0;background:#101b2dcc}
#loginBox{width:min(420px,92vw);padding:28px}input,select{width:100%;padding:12px;margin:6px 0 10px;border-radius:9px;border:1px solid #344c68;background:#0a111d;color:#fff}
.info{padding:22px;max-width:760px;width:92vw}.info h2{color:#8fd3ff}
.row{display:flex;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px solid #1c2b3d}
.ok{color:#70f0b0}.warn{color:#ffd36b}
#buy{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:min(650px,92vw);padding:22px;z-index:10}
#buy .grid{grid-template-columns:repeat(2,1fr)}
#message{position:absolute;left:50%;top:18%;transform:translateX(-50%);font-size:24px;font-weight:900;text-shadow:0 2px 10px #000;z-index:8}
@media (max-width:700px){
 .brand{font-size:34px}.menu{padding:22px}.grid{grid-template-columns:1fr 1fr}
 .grid button{min-height:54px}.bottom{bottom:8px}.controls{display:none}
 #joy,.mobileBtns{display:block}.mobileBtns{display:flex}
}
</style>
</head>
<body>
<div id="app">

<div id="menu" class="screen">
 <div class="panel menu">
  <div class="brand">NEON VALOR</div><div class="sub">TACTICAL FPS • PC + MOBILE</div>
  <div class="grid">
   <button onclick="startGame()">▶ PLAY</button>
   <button onclick="show('loadout')">🔫 LOADOUT</button>
   <button onclick="show('agents')">⚡ AGENTS</button>
   <button onclick="show('aim')">🎯 AIM / ESP</button>
   <button onclick="show('shop')">🛒 SHOP</button>
   <button onclick="show('profile')">👤 PROFILE</button>
  </div>
  <button class="full" onclick="show('settings')">⚙ SETTINGS</button>
 </div>
</div>

<div id="loadout" class="screen hidden"><div class="panel info">
 <h2>🔫 LOADOUT</h2>
 <div class="row"><span>Phantom-X — Rifle</span><button onclick="weapon='rifle'">EQUIP</button></div>
 <div class="row"><span>Vector-X — SMG</span><button onclick="weapon='smg'">EQUIP</button></div>
 <div class="row"><span>Frost SR — Sniper</span><button onclick="weapon='sniper'">EQUIP</button></div>
 <div class="row"><span>Pulse-9 — Pistol</span><button onclick="weapon='pistol'">EQUIP</button></div>
 <button class="back" onclick="show('menu')">← BACK</button>
 </div></div>

<div id="agents" class="screen hidden"><div class="panel info">
 <h2>⚡ AGENTS</h2>
 <div class="row"><span><b>VOLT</b><br>Dash • EMP • Thunder</span><button onclick="agent='volt'">SELECT</button></div>
 <div class="row"><span><b>VORTEX</b><br>Smoke • Flash • Overdrive</span><button onclick="agent='vortex'">SELECT</button></div>
 <div class="row"><span><b>TITAN</b><br>Shield • Barrier • Fortress</span><button onclick="agent='titan'">SELECT</button></div>
 <button class="back" onclick="show('menu')">← BACK</button>
 </div></div>

<div id="aim" class="screen hidden"><div id="loginBox" class="panel">
 <h2>🎯 AIM / ESP MENU</h2><p class="warn">🔐 LOGIN REQUIRED</p>
 <input id="tk" placeholder="Tài khoản"><input id="mk" type="password" placeholder="Mật khẩu">
 <button class="full" onclick="loginAim()">ĐĂNG NHẬP</button>
 <div id="aimSettings" class="hidden">
  <hr><h3>🎯 AIM</h3>
  <label><input id="aimOn" type="checkbox" checked> Aim Assist</label>
  <label>FOV <input id="fov" type="range" min="5" max="45" value="18"></label>
  <label>Target <select id="target"><option>HEAD</option><option>BODY</option></select></label>
  <label>Smoothness <input id="smooth" type="range" min="1" max="10" value="5"></label>
  <h3>👁 ESP</h3>
  <label><input id="espOn" type="checkbox" checked> Enemy ESP</label>
  <label><input id="boxOn" type="checkbox" checked> Box</label>
  <label><input id="hpOn" type="checkbox" checked> Health</label>
  <label><input id="distOn" type="checkbox" checked> Distance</label>
  <label><input id="nameOn" type="checkbox" checked> Name</label>
 </div>
 <button class="back" onclick="show('menu')">← BACK</button>
 </div></div>

<div id="shop" class="screen hidden"><div class="panel info">
 <h2>🛒 SHOP</h2><p>Credits: <b id="coins">800</b></p>
 <div class="row"><span>Cyber Pulse skin</span><button onclick="buy(800)">800</button></div>
 <div class="row"><span>Plasma Phantom skin</span><button onclick="buy(1500)">1500</button></div>
 <div class="row"><span>Ice Frost skin</span><button onclick="buy(2000)">2000</button></div>
 <button class="back" onclick="show('menu')">← BACK</button>
 </div></div>

<div id="profile" class="screen hidden"><div class="panel info">
 <h2>👤 PROFILE</h2>
 <div class="row"><span>Level</span><b>12</b></div><div class="row"><span>XP</span><b>7,420</b></div>
 <div class="row"><span>Kills</span><b id="pkills">0</b></div><div class="row"><span>Wins</span><b id="pwins">0</b></div>
 <button class="back" onclick="show('menu')">← BACK</button>
 </div></div>

<div id="settings" class="screen hidden"><div class="panel info">
 <h2>⚙ SETTINGS</h2>
 <div class="row"><span>Difficulty</span><select id="difficulty"><option>Easy</option><option selected>Normal</option><option>Hard</option><option>Extreme</option></select></div>
 <div class="row"><span>Graphics</span><select><option>Low</option><option selected>Medium</option><option>High</option></select></div>
 <p class="sub">PC: WASD + mouse • Mobile: joystick + touch buttons</p>
 <button class="back" onclick="show('menu')">← BACK</button>
 </div></div>

<div id="game" class="hidden">
 <canvas id="c"></canvas>
 <div class="hud">
  <div class="top"><div class="card" id="score">ATTACK 0 : 0 DEFEND</div><div class="card" id="round">ROUND 1 • BUY 08</div></div>
  <div id="cross"></div><div id="message"></div>
  <div class="bottom"><div class="card"><span class="hp" id="hp">100</span> HP<br><span id="armor">50</span> ARMOR</div><div class="card ammo" id="ammo">25 / 100</div></div>
 </div>
 <div id="buy" class="panel hidden"><h2>BUY PHASE</h2><p>Credits: <b id="cash">3000</b></p>
  <div class="grid"><button onclick="buyGun('rifle')">Phantom-X<br>2900</button><button onclick="buyGun('smg')">Vector-X<br>1600</button>
  <button onclick="buyGun('sniper')">Frost SR<br>4700</button><button onclick="buyGun('pistol')">Pulse-9<br>500</button></div>
  <button class="full" onclick="closeBuy()">START ROUND</button></div>
 <div id="joy"><div id="knob"></div></div>
 <div class="mobileBtns"><button ontouchstart="shoot=true" ontouchend="shoot=false">🔫</button><button onclick="reload()">🔄</button><button onclick="useSkill()">⚡</button><button onclick="interact()">F</button></div>
</div>
</div>

<script>
const canvas=document.getElementById('c'),ctx=canvas.getContext('2d');
let W,H,keys={},mouseX=0,mouseDown=false,shoot=false,weapon='rifle',agent='volt';
let logged=false,coins=800,kills=0,wins=0,scoreA=0,scoreD=0,roundNo=1,phase='buy',time=8;
let player={x:3.5,y:8.5,a:-1.57,hp:100,armor:50,ammo:25,reserve:100};
const map=[
"################",
"#..............#",
"#..####..####..#",
"#..#.........#..#",
"#..#..###....#..#",
"#.....#........#",
"###...#..###...#",
"#.....#........#",
"#..#.........#..#",
"#..####..####..#",
"#..............#",
"################"];
const enemies=[],friends=[];
const guns={rifle:{dmg:34,rate:8,mag:25,max:100},smg:{dmg:20,rate:13,mag:30,max:120},sniper:{dmg:95,rate:1,mag:5,max:25},pistol:{dmg:28,rate:5,mag:12,max:60}};
let lastShot=0;

function show(id){
 document.querySelectorAll('.screen').forEach(x=>x.classList.add('hidden'));
 document.getElementById('game').classList.add('hidden');
 if(id==='menu')document.getElementById('menu').classList.remove('hidden');
 else document.getElementById(id).classList.remove('hidden');
}
function loginAim(){
 if(document.getElementById('tk').value==='huymod' && document.getElementById('mk').value==='123'){
  logged=true;document.getElementById('aimSettings').classList.remove('hidden');
 }else alert('Sai tài khoản hoặc mật khẩu');
}
function buy(n){if(coins>=n){coins-=n;document.getElementById('coins').textContent=coins}else alert('Không đủ credits')}
function startGame(){
 document.querySelectorAll('.screen').forEach(x=>x.classList.add('hidden'));
 document.getElementById('game').classList.remove('hidden');
 resize();resetRound(); requestPointer();
}
function requestPointer(){canvas.onclick=()=>{if(!('ontouchstart' in window))canvas.requestPointerLock?.()}}
document.addEventListener('pointerlockchange',()=>{});
document.addEventListener('mousemove',e=>{if(document.pointerLockElement===canvas)player.a+=e.movementX*.0025});
window.addEventListener('keydown',e=>{keys[e.key.toLowerCase()]=true;if(e.key==='r')reload();if(e.key==='f')interact();if(e.key==='q'||e.key==='e')useSkill();if(e.key==='Tab')e.preventDefault()});
window.addEventListener('keyup',e=>keys[e.key.toLowerCase()]=false);
window.addEventListener('mousedown',e=>{if(e.button===0)mouseDown=true;if(e.button===2)e.preventDefault()});
window.addEventListener('mouseup',e=>{if(e.button===0)mouseDown=false});
window.addEventListener('contextmenu',e=>e.preventDefault());

function resetRound(){
 phase='buy';time=8;player.x=3.5;player.y=8.5;player.a=-1.57;player.hp=100;player.armor=50;
 player.ammo=guns[weapon].mag;player.reserve=guns[weapon].max;
 enemies.length=0;friends.length=0;
 for(let i=0;i<5;i++) enemies.push({x:12.5+(i%2)*.5,y:2.2+i*1.7,a:3.14,hp:100,alive:true,shot:0,name:'ENEMY-'+(i+1)});
 for(let i=0;i<4;i++) friends.push({x:2.2+i*.6,y:7+i*.5,hp:100,alive:true});
 document.getElementById('buy').classList.remove('hidden');document.getElementById('message').textContent='BUY PHASE';
}
function closeBuy(){phase='live';document.getElementById('buy').classList.add('hidden');document.getElementById('message').textContent='';}
function buyGun(g){weapon=g;player.ammo=guns[g].mag;player.reserve=guns[g].max;closeBuy()}
function reload(){let g=guns[weapon],need=g.mag-player.ammo;if(need<=0||player.reserve<=0)return;let n=Math.min(need,player.reserve);player.ammo+=n;player.reserve-=n}
function useSkill(){if(!logged)return;enemies.forEach(e=>{if(e.alive&&dist(player,e)<3.2)e.hp-=45});}
function interact(){if(phase!=='live')return;let siteA=player.x<7,siteB=player.x>9;if(siteA||siteB){phase='bomb';time=10;document.getElementById('message').textContent='NEON CORE PLANTED — DEFEND';}}
function dist(a,b){return Math.hypot(a.x-b.x,a.y-b.y)}
function wall(x,y){let ix=Math.floor(x),iy=Math.floor(y);return !map[iy]||map[iy][ix]==='#'}
function move(dx,dy){if(!wall(player.x+dx,player.y))player.x+=dx;if(!wall(player.x,player.y+dy))player.y+=dy}
function los(x1,y1,x2,y2){let d=Math.hypot(x2-x1,y2-y1),n=Math.ceil(d*12);for(let i=1;i<n;i++){let t=i/n;if(wall(x1+(x2-x1)*t,y1+(y2-y1)*t))return false}return true}
function shootGun(){
 let g=guns[weapon],now=performance.now()/1000;if(now-lastShot<1/g.rate||player.ammo<=0)return;
 lastShot=now;player.ammo--;
 let best=null,bestAng=999;
 enemies.forEach(e=>{if(!e.alive||!los(player.x,player.y,e.x,e.y))return;let a=Math.atan2(e.y-player.y,e.x-player.x),d=Math.abs(Math.atan2(Math.sin(a-player.a),Math.cos(a-player.a)));if(d<bestAng&&d<.10){best=e;bestAng=d}});
 if(logged&&document.getElementById('aimOn')?.checked){
   let f=+document.getElementById('fov').value*Math.PI/180;
   enemies.forEach(e=>{if(!e.alive||!los(player.x,player.y,e.x,e.y))return;let a=Math.atan2(e.y-player.y,e.x-player.x),d=Math.abs(Math.atan2(Math.sin(a-player.a),Math.cos(a-player.a)));if(d<f&&d<bestAng){best=e;bestAng=d}});
 }
 if(best){best.hp-=g.dmg;if(best.hp<=0){best.alive=false;kills++;document.getElementById('pkills').textContent=kills}}
}
function botAI(dt){
 enemies.forEach(e=>{
  if(!e.alive)return;
  let d=dist(player,e),a=Math.atan2(player.y-e.y,player.x-e.x);
  if(d<8&&los(e.x,e.y,player.x,player.y)){e.a=a;e.shot-=dt;if(e.shot<=0){e.shot=.7;player.hp-=difficultyDamage();}}
  else {let dx=Math.cos(a)*dt*.45,dy=Math.sin(a)*dt*.45;if(!wall(e.x+dx,e.y))e.x+=dx;if(!wall(e.x,e.y+dy))e.y+=dy}
 });
 friends.forEach(f=>{if(!f.alive)return;let target=enemies.find(e=>e.alive);if(target){let a=Math.atan2(target.y-f.y,target.x-f.x),dx=Math.cos(a)*dt*.25,dy=Math.sin(a)*dt*.25;if(!wall(f.x+dx,f.y))f.x+=dx;if(!wall(f.x,f.y+dy))f.y+=dy;if(Math.random()<dt*.3)target.hp-=20}});
}
function difficultyDamage(){let d=document.getElementById('difficulty').value;return d==='Easy'?5:d==='Hard'?11:d==='Extreme'?18:8}
function endRound(attacker){
 phase='end';if(attacker){scoreA++;wins+=(scoreA>scoreD?1:0)}else scoreD++;
 document.getElementById('pwins').textContent=wins;
 document.getElementById('message').textContent=attacker?'ROUND WON':'ROUND LOST';
 setTimeout(()=>{if(scoreA>=13||scoreD>=13){alert(scoreA>=13?'VICTORY!':'DEFEAT');scoreA=scoreD=0;roundNo=1}else roundNo++;resetRound()},1200);
}
function resize(){W=canvas.width=innerWidth*devicePixelRatio;H=canvas.height=innerHeight*devicePixelRatio;ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);W=innerWidth;H=innerHeight}
addEventListener('resize',resize);

function render(){
 ctx.clearRect(0,0,W,H);
 let grad=ctx.createLinearGradient(0,0,0,H/2);grad.addColorStop(0,'#182a42');grad.addColorStop(1,'#08101b');ctx.fillStyle=grad;ctx.fillRect(0,0,W,H/2);
 ctx.fillStyle='#15191d';ctx.fillRect(0,H/2,W,H/2);
 const rays=Math.max(180,Math.floor(W/4)),fov=Math.PI/2.7;
 for(let i=0;i<rays;i++){
  let ra=player.a-fov/2+fov*i/rays,step=.035,dd=0,hit=false;
  while(dd<18&&!hit){dd+=step;hit=wall(player.x+Math.cos(ra)*dd,player.y+Math.sin(ra)*dd)}
  let corr=dd*Math.cos(ra-player.a),h=Math.min(H*1.5,H/(corr*.75)),x=i*W/rays;
  ctx.fillStyle=(i%2?'#293b50':'#324961');ctx.fillRect(x,(H-h)/2,W/rays+1,h);
 }
 const objects=[...enemies.map(e=>({...e,type:'enemy'})),...friends.map(e=>({...e,type:'friend'}))].filter(o=>o.alive);
 objects.sort((a,b)=>dist(player,b)-dist(player,a));
 objects.forEach(o=>{
  let dx=o.x-player.x,dy=o.y-player.y,d=Math.hypot(dx,dy),a=Math.atan2(dy,dx)-player.a;
  a=Math.atan2(Math.sin(a),Math.cos(a));if(Math.abs(a)>fov/2+.2)return;
  let sx=W/2+(a/(fov/2))*W/2,sz=Math.min(H*1.1,H/(d*.75)),y=H/2-sz*.45;
  if(o.type==='enemy'){
   ctx.fillStyle='#ff4f72';ctx.fillRect(sx-sz*.12,y,sz*.24,sz*.75);ctx.fillStyle='#ffd1d9';ctx.beginPath();ctx.arc(sx,y,sz*.13,0,Math.PI*2);ctx.fill();
   if(logged&&document.getElementById('espOn')?.checked){
    if(document.getElementById('boxOn').checked){ctx.strokeStyle='#ff6688';ctx.lineWidth=2;ctx.strokeRect(sx-sz*.16,y-sz*.15,sz*.32,sz*.95)}
    if(document.getElementById('hpOn').checked){ctx.fillStyle='#222';ctx.fillRect(sx-sz*.18,y-sz*.24,sz*.36,5);ctx.fillStyle='#61ef9b';ctx.fillRect(sx-sz*.18,y-sz*.24,sz*.36*Math.max(0,o.hp)/100,5)}
    ctx.fillStyle='#fff';ctx.font='12px Arial';if(document.getElementById('nameOn').checked)ctx.fillText(o.name,sx-25,y-sz*.3);
    if(document.getElementById('distOn').checked)ctx.fillText(Math.round(d)+'m',sx-12,y-sz*.2);
   }
  }else{ctx.fillStyle='#57b7ff';ctx.fillRect(sx-sz*.1,y,sz*.2,sz*.7)}
 });
 drawMini();
}
function drawMini(){
 let s=9,ox=14,oy=70;ctx.fillStyle='#05080dcc';ctx.fillRect(ox-5,oy-5,map[0].length*s+10,map.length*s+10);
 for(let y=0;y<map.length;y++)for(let x=0;x<map[y].length;x++){ctx.fillStyle=map[y][x]==='#'?'#344a61':'#101a26';ctx.fillRect(ox+x*s,oy+y*s,s-1,s-1)}
 ctx.fillStyle='#72c7ff';ctx.beginPath();ctx.arc(ox+player.x*s,oy+player.y*s,3,0,7);ctx.fill();
 enemies.forEach(e=>{if(e.alive){ctx.fillStyle='#ff5c7d';ctx.fillRect(ox+e.x*s-2,oy+e.y*s-2,4,4)}})
}
let last=performance.now();
function loop(now){
 let dt=Math.min(.05,(now-last)/1000);last=now;
 if(!document.getElementById('game').classList.contains('hidden')){
  if(phase==='buy'){time-=dt;if(time<=0)closeBuy()}
  else if(phase==='live'||phase==='bomb'){
   let sp=(keys.shift?.5:2.2)*dt,dx=0,dy=0;
   if(keys.w){dx+=Math.cos(player.a)*sp;dy+=Math.sin(player.a)*sp}
   if(keys.s){dx-=Math.cos(player.a)*sp;dy-=Math.sin(player.a)*sp}
   if(keys.a){dx+=Math.cos(player.a-Math.PI/2)*sp;dy+=Math.sin(player.a-Math.PI/2)*sp}
   if(keys.d){dx+=Math.cos(player.a+Math.PI/2)*sp;dy+=Math.sin(player.a+Math.PI/2)*sp}
   move(dx,dy);if(mouseDown||shoot)shootGun();botAI(dt);
   if(phase==='bomb'){time-=dt;if(time<=0)endRound(true)}
   if(enemies.every(e=>!e.alive))endRound(true);else if(player.hp<=0)endRound(false);
  }
  document.getElementById('hp').textContent=Math.max(0,Math.round(player.hp));
  document.getElementById('ammo').textContent=player.ammo+' / '+player.reserve;
  document.getElementById('score').textContent='ATTACK '+scoreA+' : '+scoreD+' DEFEND';
  document.getElementById('round').textContent='ROUND '+roundNo+' • '+(phase==='buy'?'BUY '+Math.max(0,Math.ceil(time)):phase.toUpperCase());
  render();
 }
 requestAnimationFrame(loop);
}
requestAnimationFrame(loop);

// Mobile joystick
const joy=document.getElementById('joy'),knob=document.getElementById('knob');let joyId=null,jx=0,jy=0;
joy.addEventListener('touchstart',e=>{joyId=e.changedTouches[0].identifier;e.preventDefault()},{passive:false});
joy.addEventListener('touchmove',e=>{for(const t of e.changedTouches)if(t.identifier===joyId){let r=joy.getBoundingClientRect(),x=t.clientX-(r.left+r.width/2),y=t.clientY-(r.top+r.height/2),m=Math.min(45,Math.hypot(x,y)),a=Math.atan2(y,x);jx=Math.cos(a)*m/45;jy=Math.sin(a)*m/45;knob.style.transform=`translate(${jx*45}px,${jy*45}px)`;keys.w=jy<-.25;keys.s=jy>.25;keys.a=jx<-.25;keys.d=jx>.25}e.preventDefault()},{passive:false});
joy.addEventListener('touchend',e=>{keys.w=keys.s=keys.a=keys.d=false;jx=jy=0;knob.style.transform='translate(0,0)'});
function touchAim(e){if(!('ontouchstart' in window))return;let t=e.touches[0];player.a+=(t.clientX-innerWidth*.65)*.002;e.preventDefault()}
canvas.addEventListener('touchmove',touchAim,{passive:false});
</script>
</body>
</html>
"""

components.html(GAME, height=900, scrolling=False)
