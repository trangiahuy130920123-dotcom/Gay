import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="NEON RUNNER",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

GAME = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
*{box-sizing:border-box}
body{margin:0;background:#050711;font-family:Arial,sans-serif;overflow:hidden}
#game{width:100%;max-width:1100px;height:650px;margin:auto;position:relative;overflow:hidden;background:radial-gradient(circle at 75% 25%,#182b58 0,#0a1028 30%,#050711 70%);border:2px solid #263b72;border-radius:14px;user-select:none}
canvas{width:100%;height:100%;display:block}
#hud{position:absolute;left:18px;top:15px;z-index:5;color:white;font-weight:bold;font-size:16px;text-shadow:0 2px 5px black;pointer-events:none}
.bar{width:180px;height:12px;border:1px solid #aaa;margin-top:5px;background:#111}
.fill{height:100%;width:100%}
#hp{background:#ff3c6e} #energy{background:#29d9ff}
#menu{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;flex-direction:column;background:rgba(2,5,15,.82);color:white;z-index:20;text-align:center}
#menu h1{font-size:58px;margin:0;color:#40eaff;text-shadow:0 0 25px #167caa}
#menu p{color:#c8d5ff}
button{border:0;border-radius:10px;padding:13px 24px;font-size:17px;font-weight:bold;cursor:pointer;background:#40eaff;color:#031018}
#touch{position:absolute;bottom:15px;left:15px;right:15px;display:flex;justify-content:space-between;z-index:10;pointer-events:none}
.pad{display:flex;gap:10px}
.touchBtn{width:58px;height:58px;border-radius:50%;border:1px solid #526b9e;background:rgba(10,20,45,.8);color:white;display:flex;justify-content:center;align-items:center;font-size:24px;pointer-events:auto;touch-action:none}
#dash{width:75px;border-radius:16px;font-size:14px}
#msg{position:absolute;top:45%;width:100%;text-align:center;color:white;font-size:28px;font-weight:bold;opacity:0;pointer-events:none}
</style>
</head>
<body>
<div id="game">
<canvas id="canvas"></canvas>
<div id="hud">
❤️ HP<div class="bar"><div id="hp" class="fill"></div></div>
⚡ TIME DASH<div class="bar"><div id="energy" class="fill"></div></div>
<div style="margin-top:7px">🪙 <span id="coins">0</span> &nbsp;|&nbsp; 🏁 Màn <span id="level">1</span> &nbsp;|&nbsp; ⭐ <span id="score">0</span></div>
</div>
<div id="msg"></div>
<div id="menu">
<h1>NEON RUNNER</h1>
<p>⚡ THÀNH PHỐ TẬN THẾ</p>
<p>A/D hoặc ←/→ : Di chuyển<br>W / ↑ / SPACE : Nhảy<br>SHIFT : TIME DASH</p>
<button id="start">BẮT ĐẦU</button>
</div>
<div id="touch">
<div class="pad"><div class="touchBtn" id="left">◀</div><div class="touchBtn" id="right">▶</div></div>
<div class="pad"><div class="touchBtn" id="jump">▲</div><div class="touchBtn" id="dash">TIME<br>DASH</div></div>
</div>
</div>
<script>
const canvas=document.getElementById("canvas"),ctx=canvas.getContext("2d");
let W=1100,H=650,running=false,last=0,camera=0,keys={};
const player={x:120,y:480,w:38,h:58,vx:0,vy:0,speed:5.5,jump:13,hp:100,energy:100,grounded:false,inv:0,dash:false};
let coins=0,score=0,level=1,checkpoint=100,platforms=[],enemies=[],coinList=[],particles=[],portal=null;
function resize(){const r=canvas.getBoundingClientRect();W=r.width;H=r.height;canvas.width=W*devicePixelRatio;canvas.height=H*devicePixelRatio;ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0)} window.addEventListener("resize",resize);resize();
function resetLevel(){
player.x=120;player.y=430;player.vx=0;player.vy=0;player.hp=100;player.energy=100;
platforms=[
{x:0,y:550,w:700,h:100},{x:760,y:550,w:500,h:100},{x:1350,y:550,w:650,h:100},{x:2080,y:550,w:700,h:100},
{x:380,y:430,w:180,h:25},{x:700,y:350,w:180,h:25},{x:1000,y:430,w:200,h:25},{x:1300,y:330,w:200,h:25},
{x:1650,y:420,w:220,h:25},{x:1950,y:300,w:220,h:25},{x:2350,y:400,w:200,h:25}];
enemies=[{x:500,y:490,w:38,h:60,vx:1.3},{x:930,y:490,w:38,h:60,vx:-1.5},{x:1450,y:490,w:38,h:60,vx:1.4},{x:1800,y:490,w:38,h:60,vx:-1.8},{x:2200,y:490,w:38,h:60,vx:1.7}];
coinList=[{x:430,y:380},{x:500,y:380},{x:750,y:300},{x:820,y:300},{x:1060,y:380},{x:1130,y:380},{x:1360,y:280},{x:1430,y:280},{x:1700,y:370},{x:1770,y:370},{x:2000,y:250},{x:2070,y:250},{x:2400,y:350},{x:2470,y:350}];
portal={x:2640,y:470,w:60,h:80}}
function nextLevel(){level++;score+=1000;resetLevel();showMessage("⚡ LEVEL "+level)}
function showMessage(t){const m=document.getElementById("msg");m.textContent=t;m.style.opacity=1;setTimeout(()=>m.style.opacity=0,1200)}
function rectHit(a,b){return a.x<b.x+b.w&&a.x+a.w>b.x&&a.y<b.y+b.h&&a.y+a.h>b.y}
function spawnParticles(x,y,n=8){for(let i=0;i<n;i++)particles.push({x,y,vx:(Math.random()-.5)*5,vy:(Math.random()-.5)*5,life:30+Math.random()*20})}
function update(){
if(!running)return;
let slow=player.dash?.42:1;
if(keys["ArrowLeft"]||keys["a"])player.vx-=.45;if(keys["ArrowRight"]||keys["d"])player.vx+=.45;
player.vx*=.84;if(Math.abs(player.vx)>player.speed)player.vx=Math.sign(player.vx)*player.speed;
player.vy+=.55*slow;player.x+=player.vx*slow;player.y+=player.vy*slow;
if((keys[" "]||keys["ArrowUp"]||keys["w"])&&player.grounded){player.vy=-player.jump;player.grounded=false}
player.grounded=false;
for(const p of platforms)if(player.x+player.w>p.x&&player.x<p.x+p.w&&player.y+player.h>=p.y&&player.y+player.h<=p.y+25&&player.vy>=0){player.y=p.y-player.h;player.vy=0;player.grounded=true}
if(player.y>700){player.x=checkpoint;player.y=400;player.vy=0;player.hp-=20;showMessage("⚠ FALL!")}
for(const e of enemies){e.x+=e.vx;if(Math.random()<.01)e.vx*=-1;if(rectHit(player,e)&&player.inv<=0){player.hp-=15;player.inv=70;player.vx=-Math.sign(e.x-player.x)*8;player.vy=-7;spawnParticles(player.x,player.y,15)}}
for(let i=coinList.length-1;i>=0;i--){const c=coinList[i];if(player.x<c.x+20&&player.x+player.w>c.x&&player.y<c.y+20&&player.y+player.h>c.y){coins++;score+=100;spawnParticles(c.x,c.y,10);coinList.splice(i,1)}}
if(player.inv>0)player.inv--;if(player.dash){player.energy-=1.2;if(player.energy<=0){player.energy=0;player.dash=false}}else player.energy=Math.min(100,player.energy+.18);
camera+=(player.x-camera-W*.35)*.08;camera=Math.max(0,camera);if(portal&&rectHit(player,portal))nextLevel();
for(let i=particles.length-1;i>=0;i--){const p=particles[i];p.x+=p.vx;p.y+=p.vy;p.life--;if(p.life<=0)particles.splice(i,1)}
if(player.hp<=0){running=false;document.getElementById("menu").style.display="flex";document.querySelector("#menu h1").textContent="GAME OVER";document.querySelector("#menu p").textContent="Điểm: "+score+" | Coin: "+coins;document.getElementById("start").textContent="CHƠI LẠI"}
document.getElementById("hp").style.width=Math.max(0,player.hp)+"%";document.getElementById("energy").style.width=player.energy+"%";document.getElementById("coins").textContent=coins;document.getElementById("score").textContent=score;document.getElementById("level").textContent=level}
function drawBackground(){
ctx.fillStyle="#050711";ctx.fillRect(0,0,W,H);ctx.beginPath();ctx.arc(W*.78,100,55,0,Math.PI*2);ctx.fillStyle="#b9eaff";ctx.globalAlpha=.15;ctx.fill();ctx.globalAlpha=1;
for(let i=0;i<35;i++){const x=i*100-(camera*.18%100),h=70+(i*37%150);ctx.fillStyle="#0b1630";ctx.fillRect(x,H-100-h,75,h);for(let j=0;j<5;j++){ctx.fillStyle="#26436c";ctx.fillRect(x+10+j*13,H-90-h+(j*17%70),5,8)}}
for(let i=0;i<20;i++){const x=i*150-(camera*.35%150),h=100+(i*53%190);ctx.fillStyle="#101b35";ctx.fillRect(x,H-100-h,110,h);ctx.strokeStyle="#1d4770";ctx.strokeRect(x,H-100-h,110,h)}}
function draw(){
drawBackground();ctx.save();ctx.translate(-camera,0);
for(const p of platforms){ctx.fillStyle="#121c36";ctx.fillRect(p.x,p.y,p.w,p.h);ctx.fillStyle="#36d9ff";ctx.fillRect(p.x,p.y,p.w,4);ctx.fillStyle="#20365b";for(let x=p.x+10;x<p.x+p.w;x+=35)ctx.fillRect(x,p.y+14,20,3)}
if(portal){ctx.strokeStyle="#d83cff";ctx.lineWidth=6;ctx.strokeRect(portal.x,portal.y,portal.w,portal.h);ctx.fillStyle="#d83cff";ctx.globalAlpha=.18;ctx.fillRect(portal.x,portal.y,portal.w,portal.h);ctx.globalAlpha=1}
for(const c of coinList){ctx.beginPath();ctx.arc(c.x+8,c.y+8,9,0,Math.PI*2);ctx.fillStyle="#ffd83d";ctx.fill();ctx.strokeStyle="#fff3a0";ctx.stroke()}
for(const e of enemies){ctx.fillStyle="#ef315e";ctx.fillRect(e.x,e.y,e.w,e.h);ctx.fillStyle="#0b0e18";ctx.fillRect(e.x+7,e.y+13,8,8);ctx.fillRect(e.x+23,e.y+13,8,8);ctx.fillStyle="#ffb4c4";ctx.fillRect(e.x+8,e.y+42,22,5)}
if(player.inv%8<4){ctx.fillStyle=player.dash?"#8ff6ff":"#40eaff";ctx.fillRect(player.x,player.y,player.w,player.h);ctx.fillStyle="#d9faff";ctx.fillRect(player.x+7,player.y-18,25,22);ctx.fillStyle="#14253d";ctx.fillRect(player.x+10,player.y-13,20,7);ctx.fillStyle="#173c61";ctx.fillRect(player.x+7,player.y+27,25,18);ctx.fillStyle="#39a9d0";ctx.fillRect(player.x+5,player.y+45,10,13);ctx.fillRect(player.x+23,player.y+45,10,13)}
if(player.dash)for(let i=1;i<7;i++){ctx.globalAlpha=.12;ctx.fillStyle="#40eaff";ctx.fillRect(player.x-i*15,player.y+8,player.w,player.h-16)}ctx.globalAlpha=1;
for(const p of particles){ctx.globalAlpha=Math.max(0,p.life/50);ctx.fillStyle="#40eaff";ctx.fillRect(p.x,p.y,5,5)}ctx.globalAlpha=1;ctx.restore()}
function loop(t){if(!last)last=t;update();draw();last=t;requestAnimationFrame(loop)}
function startGame(){coins=0;score=0;level=1;checkpoint=100;resetLevel();running=true;document.getElementById("menu").style.display="none"}
document.getElementById("start").addEventListener("click",startGame);
window.addEventListener("keydown",e=>{keys[e.key]=true;if(e.key==="Shift"&&player.energy>5)player.dash=true;if([" ","ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].includes(e.key))e.preventDefault()});
window.addEventListener("keyup",e=>{keys[e.key]=false;if(e.key==="Shift")player.dash=false});
function hold(id,key){const el=document.getElementById(id);const on=e=>{e.preventDefault();keys[key]=true},off=e=>{e.preventDefault();keys[key]=false};el.addEventListener("pointerdown",on);el.addEventListener("pointerup",off);el.addEventListener("pointercancel",off);el.addEventListener("pointerleave",off)}
hold("left","ArrowLeft");hold("right","ArrowRight");hold("jump"," ");
const dashBtn=document.getElementById("dash");dashBtn.addEventListener("pointerdown",e=>{e.preventDefault();if(player.energy>5)player.dash=true});dashBtn.addEventListener("pointerup",e=>{e.preventDefault();player.dash=false});dashBtn.addEventListener("pointercancel",()=>player.dash=false);
resetLevel();requestAnimationFrame(loop);
</script>
</body>
</html>
"""

components.html(GAME, height=680, scrolling=False)
