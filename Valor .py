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
#app{width:100%;height:100dvh;min-height:560px;position:relative;background:radial-gradient(circle at 50% 20%,#12213c,#060910 60%);overflow:hidden}
#aim{align-items:flex-start;padding:20px 10px}
#aimPanel{width:min(760px,96vw);max-height:calc(100dvh - 40px);overflow:auto}
.screen{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.panel{background:rgba(8,13,23,.94);border:1px solid #263951;border-radius:18px;box-shadow:0 20px 70px #000a}
.menu{width:min(900px,94vw);padding:34px}.brand{font-size:48px;font-weight:900;letter-spacing:5px;color:#8fd3ff;text-shadow:0 0 25px #239cff}
.sub{color:#7f94ad;margin:5px 0 25px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.grid button{min-height:60px}
.full{width:100%;margin-top:12px}.back{margin-top:20px}
#game{position:absolute;inset:0;background:#020407;overflow:hidden}
canvas{position:absolute;inset:0;width:100%;height:100%;touch-action:none}
.hud{position:absolute;inset:0;pointer-events:none}
.top{position:absolute;top:12px;left:12px;right:12px;display:flex;justify-content:center;gap:12px;font-weight:800;z-index:5}
.card{background:linear-gradient(180deg,#071426e8,#050b14e8);border:1px solid #35516f;border-radius:10px;padding:8px 14px;box-shadow:0 8px 25px #0008;backdrop-filter:blur(8px)}
#score{min-width:210px;text-align:center}
#round{min-width:170px;text-align:center}
#siteBadge{position:absolute;right:16px;top:82px;padding:9px 16px;border-radius:18px;background:#0b1625dd;border:1px solid #466987;color:#eaf6ff;font-weight:900;letter-spacing:.5px;z-index:5}
#killfeed{position:absolute;left:16px;top:145px;display:flex;flex-direction:column;gap:5px;z-index:5}
.feed{padding:6px 10px;border-radius:6px;background:#07111dd9;border:1px solid #29425d;font-size:12px}
#weaponHud{position:absolute;right:18px;bottom:18px;text-align:right;z-index:5;text-shadow:0 2px 7px #000}
#weaponName{font-size:14px;letter-spacing:2px;color:#a8d9ff}
#ammoBig{font-size:34px;font-weight:900}
#statusHud{position:absolute;left:18px;bottom:18px;display:flex;align-items:end;gap:12px;z-index:5}
#hpBlock{min-width:125px}
#abilityBar{display:flex;gap:8px}
.ability{width:46px;height:46px;border-radius:10px;background:#081422cc;border:1px solid #44617e;display:flex;align-items:center;justify-content:center;font-weight:900;color:#bfe6ff;box-shadow:0 5px 18px #0008}
.bottom{display:none}
#cross{
 position:absolute;left:50%;top:50%;width:34px;height:34px;
 transform:translate(-50%,-50%);pointer-events:none;
 border:2px solid rgba(255,255,255,.95);
 border-radius:50%;
 box-shadow:0 0 8px rgba(255,255,255,.45), inset 0 0 4px rgba(255,255,255,.2);
}
#cross:before,#cross:after{content:"";position:absolute;background:#fff;box-shadow:0 0 6px #fff}
#cross:before{left:15px;top:5px;width:2px;height:6px;box-shadow:0 18px 6px #fff}
#cross:after{left:5px;top:15px;width:6px;height:2px;box-shadow:18px 0 6px #fff}
#cross .dot{position:absolute;left:50%;top:50%;width:4px;height:4px;
 transform:translate(-50%,-50%);border-radius:50%;background:#fff;
 box-shadow:0 0 7px #fff}
#cross.aim-on{width:44px;height:44px}
#cross.aim-on:before{top:3px}
#cross.aim-on:after{left:3px}
.bottom{position:absolute;left:16px;right:16px;bottom:15px;display:flex;justify-content:space-between;align-items:end}
.hp{font-size:26px;font-weight:900}.ammo{font-size:28px;font-weight:900}
.controls{display:flex;gap:8px;pointer-events:auto}.controls button{width:55px;height:55px;padding:0}
#joy{position:absolute;left:22px;bottom:25px;width:140px;height:140px;border:2px solid #7692b055;border-radius:50%;background:#ffffff09;pointer-events:auto;display:none;z-index:20}
#knob{position:absolute;left:45px;top:45px;width:50px;height:50px;border-radius:50%;background:#9bcaff55;border:1px solid #bde0ff99}
.mobileBtns{position:absolute;right:18px;bottom:18px;display:none;gap:8px;pointer-events:auto;z-index:20}
.mobileBtns button{width:58px;height:58px;border-radius:50%;padding:0;background:#101b2dcc}
#loginBox{width:min(420px,92vw);padding:28px}input,select{width:100%;padding:12px;margin:6px 0 10px;border-radius:9px;border:1px solid #344c68;background:#0a111d;color:#fff}
.info{padding:22px;max-width:760px;width:92vw}.info h2{color:#8fd3ff}
.row{display:flex;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px solid #1c2b3d}
.ok{color:#70f0b0}.warn{color:#ffd36b}
#buy{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:min(650px,92vw);padding:22px;z-index:10}
#buy .grid{grid-template-columns:repeat(2,1fr)}
#message{position:absolute;left:50%;top:18%;transform:translateX(-50%);font-size:24px;font-weight:900;text-shadow:0 2px 10px #000;z-index:8}
@media (max-width:700px){
 #cross{width:38px;height:38px}
 .top{top:8px;gap:6px;font-size:12px}
 #score{min-width:150px} #round{min-width:125px}
 #siteBadge{top:62px;right:10px;font-size:12px;padding:7px 11px}
 #statusHud{left:10px;bottom:10px;gap:6px}
 #hpBlock{min-width:92px;font-size:11px;padding:6px 9px}
 .hp{font-size:22px}
 .ability{width:38px;height:38px;border-radius:9px;font-size:12px}
 #weaponHud{right:10px;bottom:10px}
 #ammoBig{font-size:26px}
 #weaponName{font-size:11px}
 #killfeed{left:10px;top:112px}


 .screen{padding:10px 7px}
 #aim{padding:10px 7px}
 #aimPanel{max-height:calc(100dvh - 20px);width:96vw}
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

<div id="aim" class="screen hidden"><div class="panel info" id="aimPanel">
 <div id="aimLogin">
  <h2>🎯 AIM / ESP</h2>
  <p class="warn">🔐 LOGIN REQUIRED</p>
  <p class="sub">Đăng nhập riêng để mở bảng điều khiển AIM / ESP.</p>
  <input id="tk" autocomplete="username" placeholder="Tài khoản">
  <input id="mk" type="password" autocomplete="current-password" placeholder="Mật khẩu">
  <button class="full" onclick="loginAim()">ĐĂNG NHẬP</button>
  <p id="loginError" class="warn hidden">Sai tài khoản hoặc mật khẩu.</p>
 </div>
 <div id="aimSettings" class="hidden">
  <div style="display:flex;justify-content:space-between;align-items:center;gap:10px">
   <div><h2 style="margin-bottom:4px">🎯 AIM / ESP CONTROL</h2><div class="sub">Đã đăng nhập • huymod</div></div>
   <button onclick="logoutAim()">ĐĂNG XUẤT</button>
  </div>
  <hr>
  <h3>🎯 AIM</h3>
  <div class="row"><span>Aim Assist</span><input id="aimOn" type="checkbox" checked></div>
  <div class="row"><span>FOV</span><input id="fov" type="range" min="5" max="45" value="18"></div>
  <div class="row"><span>Target</span><select id="target"><option>HEAD</option><option>BODY</option></select></div>
  <div class="row"><span>Smoothness</span><input id="smooth" type="range" min="1" max="10" value="5"></div><div class="row"><span>Vòng aim</span><input id="circleAim" type="checkbox" checked onchange="setAimCircle(this.checked)"></div>
  <div class="row"><span>Kích thước vòng</span><input id="circleSize" type="range" min="20" max="70" value="34" oninput="setAimSize(this.value)"></div>
  <h3>👁 ESP</h3>
  <div class="row"><span>Enemy ESP</span><input id="espOn" type="checkbox" checked></div>
  <div class="row"><span>Box</span><input id="boxOn" type="checkbox" checked></div>
  <div class="row"><span>Health</span><input id="hpOn" type="checkbox" checked></div>
  <div class="row"><span>Distance</span><input id="distOn" type="checkbox" checked></div>
  <div class="row"><span>Name</span><input id="nameOn" type="checkbox" checked></div>
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
  <div id="siteBadge">A SITE</div>
  <div id="killfeed"></div>
  <div id="cross"><span class="dot"></span></div><div id="message"></div>
  <div id="statusHud">
    <div id="hpBlock" class="card"><span class="hp" id="hp">100</span> HP<br><span id="armor">50</span> ARMOR</div>
    <div id="abilityBar"><div class="ability">C</div><div class="ability">Q</div><div class="ability">E</div><div class="ability">X</div></div>
  </div>
  <div id="weaponHud"><div id="weaponName">PHANTOM-X</div><div id="ammoBig"><span id="ammo">25 / 100</span></div></div>
  
 </div>
 <div id="buy" class="panel hidden"><h2>BUY PHASE</h2><p>Credits: <b id="cash">3000</b></p>
  <div class="grid"><button onclick="buyGun('rifle')">Phantom-X<br>2900</button><button onclick="buyGun('smg')">Vector-X<br>1600</button>
  <button onclick="buyGun('sniper')">Frost SR<br>4700</button><button onclick="buyGun('pistol')">Pulse-9<br>500</button></div>
  <button class="full" onclick="closeBuy()">START ROUND</button></div>
 <div id="joy"><div id="knob"></div></div>
 <div class="mobileBtns">
  <button onpointerdown="shoot=true" onpointerup="shoot=false" ontouchstart="shoot=true" ontouchend="shoot=false">🔫</button>
  <button onclick="reload()">🔄</button><button onclick="useSkill()">⚡</button><button onclick="interact()">F</button>
</div>
</div>
</div>

<script>
const canvas=document.getElementById('c'),ctx=canvas.getContext('2d');
let W,H,keys={},mouseX=0,mouseDown=false,shoot=false,weapon='rifle',agent='volt';
let logged=false,coins=800,kills=0,wins=0,scoreA=0,scoreD=0,roundNo=1,phase='buy',time=8;
let player={x:2.5,y:7.5,a:0,hp:100,armor:50,ammo:25,reserve:100};
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
 const tk=document.getElementById('tk').value.trim();
 const mk=document.getElementById('mk').value;
 const err=document.getElementById('loginError');
 if(tk==='huymod' && mk==='123'){
  logged=true;
  err.classList.add('hidden');
  document.getElementById('aimLogin').classList.add('hidden');
  document.getElementById('aimSettings').classList.remove('hidden');
 }else{
  logged=false;
  err.classList.remove('hidden');
  document.getElementById('mk').value='';
 }
}
function logoutAim(){
 logged=false;
 document.getElementById('aimSettings').classList.add('hidden');
 document.getElementById('aimLogin').classList.remove('hidden');
 document.getElementById('tk').value='';
 document.getElementById('mk').value='';
}
function setAimCircle(on){
 const c=document.getElementById('cross');
 if(c)c.classList.toggle('aim-on',on);
}
function setAimSize(v){
 const c=document.getElementById('cross');
 if(c)c.style.width=v+'px',c.style.height=v+'px';
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
 phase='buy';time=8;player.x=2.5;player.y=7.5;player.a=0;player.hp=100;player.armor=50;
 player.ammo=guns[weapon].mag;player.reserve=guns[weapon].max;
 enemies.length=0;friends.length=0;
 for(let i=0;i<5;i++) enemies.push({x:12.5+(i%2)*.5,y:2.2+i*1.7,a:3.14,hp:100,alive:true,shot:0,name:'ENEMY-'+(i+1)});
 for(let i=0;i<4;i++) friends.push({x:2.2+i*.6,y:7+i*.5,hp:100,alive:true});
 document.getElementById('buy').classList.remove('hidden');document.getElementById('message').textContent='BUY PHASE';
}
function closeBuy(){phase='live';document.getElementById('buy').classList.add('hidden');document.getElementById('message').textContent='';}
function buyGun(g){
 weapon=g;player.ammo=guns[g].mag;player.reserve=guns[g].max;
 const names={rifle:'PHANTOM-X',smg:'VECTOR-X',sniper:'FROST SR',pistol:'PULSE-9'};
 document.getElementById('weaponName').textContent=names[g]||g.toUpperCase();
 closeBuy()
}
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
 if(best){
 best.hp-=g.dmg;
 if(best.hp<=0){
  best.alive=false;kills++;
  const feed=document.getElementById('killfeed');
  const row=document.createElement('div');row.className='feed';
  row.textContent='huymod  ⚡  '+best.name;
  feed.prepend(row);if(feed.children.length>3)feed.lastElementChild.remove();
  const k=document.getElementById('pkills');if(k)k.textContent=kills;
 }
}
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
function resize(){
 const d=Math.min(window.devicePixelRatio||1,2);
 W=window.innerWidth; H=window.innerHeight;
 canvas.width=Math.max(1,Math.floor(W*d));
 canvas.height=Math.max(1,Math.floor(H*d));
 canvas.style.width=W+'px'; canvas.style.height=H+'px';
 ctx.setTransform(d,0,0,d,0,0);
}
addEventListener('resize',resize);

function drawWeapon(){
  // Stylized original sci-fi rifle, drawn in-game (no external asset).
  const scale=Math.min(W,H)/720;
  ctx.save();
  ctx.translate(W*.77,H*.82);
  ctx.rotate(-0.08);
  ctx.scale(scale,scale);

  // Arm
  let arm=ctx.createLinearGradient(-60,40,120,170);
  arm.addColorStop(0,'#26374a');arm.addColorStop(1,'#0a1018');
  ctx.fillStyle=arm;
  ctx.beginPath();ctx.moveTo(-95,80);ctx.lineTo(15,38);ctx.lineTo(105,155);ctx.lineTo(-20,185);ctx.closePath();ctx.fill();

  // Glove
  ctx.fillStyle='#101a25';ctx.strokeStyle='#51677d';ctx.lineWidth=3;
  ctx.beginPath();ctx.roundRect(-28,15,92,66,18);ctx.fill();ctx.stroke();

  // Rifle body
  let metal=ctx.createLinearGradient(-10,-70,190,55);
  metal.addColorStop(0,'#34485b');metal.addColorStop(.5,'#121c28');metal.addColorStop(1,'#070d14');
  ctx.fillStyle=metal;ctx.strokeStyle='#667f97';ctx.lineWidth=3;
  ctx.beginPath();ctx.moveTo(-5,-65);ctx.lineTo(180,-40);ctx.lineTo(205,8);ctx.lineTo(70,42);ctx.lineTo(-18,10);ctx.closePath();ctx.fill();ctx.stroke();

  // Barrel
  ctx.fillStyle='#080d13';ctx.fillRect(178,-25,115,24);
  ctx.fillStyle='#1e2d3b';ctx.fillRect(205,-20,85,13);
  ctx.fillStyle='#62dcff';ctx.fillRect(218,-18,32,4);

  // Receiver details
  ctx.fillStyle='#1b2c3c';ctx.fillRect(38,-44,72,12);
  ctx.fillStyle='#5bdcff';ctx.fillRect(63,-42,24,5);
  ctx.fillStyle='#0a111a';ctx.fillRect(88,-20,48,25);

  // Magazine
  ctx.fillStyle='#0c141d';ctx.strokeStyle='#4b6175';
  ctx.beginPath();ctx.moveTo(8,25);ctx.lineTo(53,12);ctx.lineTo(82,90);ctx.lineTo(36,102);ctx.closePath();ctx.fill();ctx.stroke();

  // Muzzle glow
  ctx.shadowColor='#54dfff';ctx.shadowBlur=16;
  ctx.fillStyle='#54dfff';ctx.fillRect(284,-19,8,12);ctx.shadowBlur=0;
  ctx.restore();
}

function render(){
 ctx.clearRect(0,0,W,H);

 // Sky with soft clouds and a sun glow.
 const sky=ctx.createLinearGradient(0,0,0,H*.62);
 sky.addColorStop(0,'#5aa7d8'); sky.addColorStop(.48,'#2f719c'); sky.addColorStop(1,'#122a3d');
 ctx.fillStyle=sky;ctx.fillRect(0,0,W,H*.65);

 ctx.globalAlpha=.16;
 for(let i=0;i<6;i++){
   ctx.fillStyle='#fff';
   ctx.beginPath();ctx.ellipse(W*(.08+i*.18),H*(.18+(i%2)*.05),W*.12,H*.035,0,0,Math.PI*2);ctx.fill();
 }
 ctx.globalAlpha=1;

 // Distant skyline / foliage.
 ctx.fillStyle='#193d42';
 ctx.fillRect(0,H*.38,W,H*.16);
 ctx.fillStyle='#1f563f';
 for(let i=0;i<18;i++){
   let x=i*W/17;
   ctx.beginPath();ctx.arc(x,H*.38,18+(i%4)*7,0,Math.PI*2);ctx.fill();
 }

 // Ground perspective.
 const ground=ctx.createLinearGradient(0,H*.48,0,H);
 ground.addColorStop(0,'#40505a');ground.addColorStop(.25,'#28363d');ground.addColorStop(1,'#0d141a');
 ctx.fillStyle=ground;ctx.fillRect(0,H*.48,W,H*.52);

 // Perspective lane/tiles.
 ctx.strokeStyle='rgba(150,185,198,.18)';ctx.lineWidth=1;
 for(let y=0;y<10;y++){
   const t=y/10, yy=H*.5+(H*.5)*t*t;
   ctx.beginPath();ctx.moveTo(0,yy);ctx.lineTo(W,yy);ctx.stroke();
 }
 for(let x=-8;x<=8;x++){
   ctx.beginPath();ctx.moveTo(W/2,H*.49);ctx.lineTo(W/2+x*W*.16,H);ctx.stroke();
 }

 // Architectural walls/cover silhouettes.
 ctx.fillStyle='#263943';
 ctx.fillRect(0,H*.43,W*.16,H*.30);
 ctx.fillStyle='#344b55';ctx.fillRect(0,H*.45,W*.12,H*.18);
 ctx.fillStyle='#17252d';ctx.fillRect(W*.82,H*.36,W*.18,H*.30);
 ctx.fillStyle='#3b5359';ctx.fillRect(W*.86,H*.39,W*.14,H*.17);

 // Raycast walls.
 const rays=Math.min(320,Math.max(180,Math.floor(W/3.2)));
 const fov=Math.PI/2.7,colW=W/rays;
 for(let i=0;i<rays;i++){
   const ra=player.a-fov/2+fov*(i+.5)/rays;
   let dd=.05,hit=false;
   while(dd<18&&!hit){dd+=.045;hit=wall(player.x+Math.cos(ra)*dd,player.y+Math.sin(ra)*dd);}
   const corr=Math.max(.12,dd*Math.cos(ra-player.a));
   const h=Math.min(H*1.35,H/(corr*.88));
   const top=Math.max(0,(H-h)/2),bottom=Math.min(H,(H+h)/2);
   const shade=Math.max(30,Math.min(120,120-corr*5));
   const r=Math.floor(shade*.52),g=Math.floor(shade*.67),bl=Math.floor(shade*.76);
   ctx.fillStyle=`rgb(${r},${g},${bl})`;
   ctx.fillRect(i*colW,top,colW+1,bottom-top);

   // wall edge light
   if(i%18===0){
     ctx.fillStyle='rgba(125,210,240,.12)';
     ctx.fillRect(i*colW,top,1,bottom-top);
   }
 }

 // Enemy/friendly characters.
 const objects=[...enemies.map(e=>({...e,type:'enemy'})),...friends.map(e=>({...e,type:'friend'}))]
   .filter(o=>o.alive).sort((a,b)=>dist(player,b)-dist(player,a));

 objects.forEach(o=>{
   const dx=o.x-player.x,dy=o.y-player.y,d=Math.max(.15,Math.hypot(dx,dy));
   let ang=Math.atan2(dy,dx)-player.a;ang=Math.atan2(Math.sin(ang),Math.cos(ang));
   if(Math.abs(ang)>fov/2+.16)return;
   const sx=W/2+(ang/(fov/2))*W/2, sz=Math.min(H*.68,H/(d*.88)), yy=H/2-sz*.46;
   ctx.save();
   ctx.shadowColor=o.type==='enemy'?'#ff4266':'#44baff';ctx.shadowBlur=8;
   ctx.fillStyle=o.type==='enemy'?'#c73552':'#318ac3';
   ctx.fillRect(sx-sz*.11,yy,sz*.22,sz*.68);
   ctx.fillStyle=o.type==='enemy'?'#ffd2d8':'#b9e8ff';
   ctx.beginPath();ctx.arc(sx,yy,Math.max(3,sz*.12),0,Math.PI*2);ctx.fill();
   ctx.shadowBlur=0;

   if(o.type==='enemy'&&logged&&document.getElementById('espOn')?.checked){
     if(document.getElementById('boxOn').checked){
       ctx.strokeStyle='#ff6688';ctx.lineWidth=2;
       ctx.strokeRect(sx-sz*.16,yy-sz*.15,sz*.32,sz*.95);
     }
     if(document.getElementById('hpOn').checked){
       ctx.fillStyle='#111';ctx.fillRect(sx-sz*.18,yy-sz*.24,sz*.36,5);
       ctx.fillStyle='#6df0a0';ctx.fillRect(sx-sz*.18,yy-sz*.24,sz*.36*Math.max(0,o.hp)/100,5);
     }
     ctx.fillStyle='#fff';ctx.font='12px Arial';
     if(document.getElementById('nameOn').checked)ctx.fillText(o.name,sx-25,yy-sz*.3);
     if(document.getElementById('distOn').checked)ctx.fillText(Math.round(d)+'m',sx-12,yy-sz*.2);
   }
   ctx.restore();
 });

 drawMini();
 drawWeapon();

 // Slight cinematic vignette.
 const v=ctx.createRadialGradient(W/2,H*.52,Math.min(W,H)*.18,W/2,H*.52,Math.max(W,H)*.72);
 v.addColorStop(0,'rgba(0,0,0,0)');
 v.addColorStop(1,'rgba(0,0,0,.48)');
 ctx.fillStyle=v;ctx.fillRect(0,0,W,H);
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
  document.getElementById('siteBadge').textContent=(player.x<7?'A SITE':player.x>9?'B SITE':'MID');
  document.getElementById('ammoBig').textContent=player.ammo+' / '+player.reserve;
  render();
 }
 requestAnimationFrame(loop);
}
requestAnimationFrame(loop);

// Mobile controls
const touchDevice=('ontouchstart' in window)||(navigator.maxTouchPoints>0);
if(touchDevice){
 document.getElementById('joy').style.display='block';
 document.querySelector('.mobileBtns').style.display='flex';
}
const joy=document.getElementById('joy'),knob=document.getElementById('knob');let joyId=null,jx=0,jy=0;
joy.addEventListener('touchstart',e=>{joyId=e.changedTouches[0].identifier;e.preventDefault()},{passive:false});
joy.addEventListener('touchmove',e=>{for(const t of e.changedTouches)if(t.identifier===joyId){let r=joy.getBoundingClientRect(),x=t.clientX-(r.left+r.width/2),y=t.clientY-(r.top+r.height/2),m=Math.min(45,Math.hypot(x,y)),a=Math.atan2(y,x);jx=Math.cos(a)*m/45;jy=Math.sin(a)*m/45;knob.style.transform=`translate(${jx*45}px,${jy*45}px)`;keys.w=jy<-.25;keys.s=jy>.25;keys.a=jx<-.25;keys.d=jx>.25}e.preventDefault()},{passive:false});
joy.addEventListener('touchend',e=>{keys.w=keys.s=keys.a=keys.d=false;jx=jy=0;knob.style.transform='translate(0,0)'});
let aimTouchId=null,lastAimX=0,lastAimY=0;
canvas.addEventListener('touchstart',e=>{
 if(!touchDevice)return;
 for(const t of e.changedTouches){
   if(t.clientX>innerWidth*.38){
     aimTouchId=t.identifier;lastAimX=t.clientX;lastAimY=t.clientY;break;
   }
 }
 e.preventDefault();
},{passive:false});
canvas.addEventListener('touchmove',e=>{
 if(!touchDevice)return;
 for(const t of e.changedTouches){
   if(t.identifier===aimTouchId){
     const dx=t.clientX-lastAimX,dy=t.clientY-lastAimY;
     player.a+=dx*.004;
     lastAimX=t.clientX;lastAimY=t.clientY;
   }
 }
 e.preventDefault();
},{passive:false});
canvas.addEventListener('touchend',e=>{
 for(const t of e.changedTouches)if(t.identifier===aimTouchId)aimTouchId=null;
},{passive:false});

// Force touch controls on real touch devices. Streamlit's iframe can report a
// desktop-sized CSS viewport even when viewed on a phone.
if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
  document.getElementById('joy').style.display='block';
  document.querySelector('.mobileBtns').style.display='flex';
}
// Drag anywhere on the right half to aim; don't steal the joystick area.
let aimTouchId=null, aimLastX=0;
canvas.addEventListener('touchstart',e=>{
  for(const t of e.changedTouches){
    if(t.clientX > innerWidth*0.38){ aimTouchId=t.identifier; aimLastX=t.clientX; }
  }
  e.preventDefault();
},{passive:false});
canvas.addEventListener('touchmove',e=>{
  for(const t of e.changedTouches){
    if(t.identifier===aimTouchId){
      player.a += (t.clientX-aimLastX)*0.008;
      aimLastX=t.clientX;
    }
  }
  e.preventDefault();
},{passive:false});
canvas.addEventListener('touchend',e=>{
  for(const t of e.changedTouches) if(t.identifier===aimTouchId) aimTouchId=null;
},{passive:false});
</script>
</body>
</html>
"""

components.html(GAME, height=900, scrolling=False)
