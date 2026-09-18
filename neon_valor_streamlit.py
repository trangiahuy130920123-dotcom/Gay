import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="NEON VALOR",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

GAME_HTML = r"""
<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<style>
*{box-sizing:border-box}
body{margin:0;background:#080b12;color:#f4f7ff;font-family:system-ui,-apple-system,sans-serif}
.app{max-width:1100px;margin:auto;padding:14px}
.panel{background:#101521;border:1px solid #273044;border-radius:18px;padding:14px}
.top{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.logo{font-size:24px;font-weight:900;letter-spacing:.5px}
.small{font-size:12px;color:#a9b3c7}
button,input,select{font:inherit}
button{min-height:44px;border:1px solid #354058;border-radius:10px;background:#171e2c;color:white;padding:9px 13px;cursor:pointer}
button:hover{background:#20293a}
.primary{background:#2f6fed;border-color:#2f6fed}
.danger{background:#7d2634}
.tabs{display:flex;gap:8px;overflow:auto;margin:12px 0}
.tab{white-space:nowrap}
.hidden{display:none!important}
.menu{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:12px}
.menu button{min-height:58px}
.game{position:relative;margin-top:12px;background:#0b101a;border:1px solid #293248;border-radius:15px;overflow:hidden}
canvas{display:block;width:100%;height:auto;aspect-ratio:16/9;touch-action:none;background:#0c1220}
.hud{position:absolute;left:10px;right:10px;top:10px;display:flex;justify-content:space-between;pointer-events:none}
.hudbox{background:#0b101add;border:1px solid #3a455b;border-radius:9px;padding:7px 10px;font-size:12px}
.hpbar{width:150px;height:7px;background:#30384a;border-radius:9px;overflow:hidden;margin-top:4px}
.hpfill{height:100%;width:100%;background:#28c76f}
.mobile{position:absolute;inset:0;pointer-events:none}
.joy{position:absolute;left:18px;bottom:18px;width:105px;height:105px;border-radius:50%;border:1px solid #ffffff35;background:#ffffff12;pointer-events:auto;touch-action:none}
.knob{position:absolute;width:46px;height:46px;left:29px;top:29px;border-radius:50%;background:#ffffff55}
.actions{position:absolute;right:16px;bottom:15px;display:flex;gap:9px;align-items:end;pointer-events:auto}
.act{width:58px;height:58px;border-radius:50%;padding:0;background:#ffffff16}
.fire{width:76px;height:76px;background:#2f6fedaa}
.overlay{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:#05070dcc}
.modal{width:min(420px,90%);background:#111827;border:1px solid #364158;border-radius:16px;padding:18px}
.modal h2{margin:0 0 6px}
.field{margin:10px 0}
.field label{display:block;font-size:12px;color:#aeb8cb;margin-bottom:5px}
.field input,.field select{width:100%;padding:11px;border-radius:9px;border:1px solid #354058;background:#0b1019;color:white}
.row{display:flex;gap:9px;flex-wrap:wrap}
.row>*{flex:1}
.status{font-size:12px;color:#9eabc0;margin-top:8px;min-height:18px}
.settings{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.card{background:#0d131f;border:1px solid #293248;border-radius:12px;padding:12px}
.card h3{margin:0 0 8px;font-size:14px}
.switchrow{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid #20283a;font-size:13px}
.switchrow:last-child{border-bottom:0}
.badge{padding:4px 8px;border-radius:999px;background:#172238;color:#b8c9ed;font-size:11px}
@media(max-width:650px){
 .menu{grid-template-columns:1fr 1fr}
 .settings{grid-template-columns:1fr}
 .logo{font-size:20px}
}
</style>
</head>
<body>
<div class="app">
<div class="panel">
  <div class="top">
    <div class="logo">🔥 NEON VALOR</div>
    <div class="small">5v5 Tactical FPS • PC + Mobile</div>
  </div>

  <div class="tabs">
    <button class="tab primary" id="playTab">▶ PLAY</button>
    <button class="tab" id="aimTab">🎯 AIM / ESP</button>
    <button class="tab" id="loadTab">🔫 LOADOUT</button>
    <button class="tab" id="shopTab">🛒 SHOP</button>
    <button class="tab" id="settingsTab">⚙ SETTINGS</button>
  </div>

  <section id="home">
    <div class="card">
      <h3>NEON CITY</h3>
      <div class="small">Đội bạn: 5 người • Địch: 5 bot • First to 13 rounds</div>
    </div>
    <div class="menu">
      <button class="primary" id="start">▶ BẮT ĐẦU TRẬN</button>
      <button id="aimOpen">🎯 AIM / ESP</button>
      <button id="loadOpen">🔫 LOADOUT</button>
      <button id="shopOpen">🛒 SHOP</button>
      <button id="settingsOpen">⚙ SETTINGS</button>
      <button id="logout">🚪 LOGOUT</button>
    </div>
  </section>

  <section id="aim" class="hidden">
    <div class="card">
      <h3>🔐 AIM / ESP — PRIVATE MENU</h3>
      <div class="small">Menu này có lớp đăng nhập riêng. Tài khoản demo được tạo sẵn.</div>
    </div>

    <div id="aimLogin" class="modal" style="margin-top:12px">
      <h2>🔐 AIM / ESP LOGIN</h2>
      <div class="field"><label>Tài khoản</label><input id="aimUser" value="huymod" autocomplete="username"></div>
      <div class="field"><label>Mật khẩu</label><input id="aimPass" type="password" value="123" autocomplete="current-password"></div>
      <button class="primary" id="aimLoginBtn">ĐĂNG NHẬP</button>
      <div class="status" id="loginStatus">Demo: huymod / 123</div>
    </div>

    <div id="aimPanel" class="hidden" style="margin-top:12px">
      <div class="settings">
        <div class="card">
          <h3>🎯 AIM</h3>
          <div class="switchrow">Aim Assist <button id="aimAssist">OFF</button></div>
          <div class="switchrow">Target <select id="target"><option>HEAD</option><option>BODY</option></select></div>
          <div class="switchrow">FOV <input id="fov" type="range" min="30" max="180" value="90"></div>
          <div class="switchrow">Smooth <input id="smooth" type="range" min="1" max="100" value="65"></div>
        </div>
        <div class="card">
          <h3>👁 ESP</h3>
          <div class="switchrow">Enemy ESP <button id="esp">ON</button></div>
          <div class="switchrow">Box <button id="box">ON</button></div>
          <div class="switchrow">Health <button id="health">ON</button></div>
          <div class="switchrow">Distance <button id="distance">ON</button></div>
        </div>
      </div>
      <div class="row" style="margin-top:10px">
        <button id="aimLogout">🔒 KHÓA AIM / ESP</button>
        <button id="aimBack">← MENU</button>
      </div>
    </div>
  </section>

  <section id="loadout" class="hidden">
    <div class="card">
      <h3>🔫 LOADOUT</h3>
      <div class="row">
        <button>Pulse-9</button><button>Neon SMG</button><button>Phantom-X</button><button>Frost SR</button>
      </div>
    </div>
  </section>

  <section id="shop" class="hidden">
    <div class="card">
      <h3>🛒 SHOP</h3>
      <p class="small">💰 Coins: <b id="coins">1250</b></p>
      <div class="row">
        <button>Cyber Pulse — 800</button><button>Plasma Phantom — 1500</button><button>Ice Frost — 2000</button>
      </div>
    </div>
  </section>

  <section id="settings" class="hidden">
    <div class="settings">
      <div class="card"><h3>🎮 Controls</h3><p class="small">PC: WASD + Mouse + R + Space + G</p><p class="small">Mobile: joystick + nút bắn/skill</p></div>
      <div class="card"><h3>⚡ Performance</h3><p class="small">Canvas 2D nhẹ, giới hạn bot và hiệu ứng để phù hợp điện thoại.</p></div>
    </div>
  </section>

  <section id="gameSection" class="hidden">
    <div class="game" id="game">
      <canvas id="cv" width="960" height="540"></canvas>
      <div class="hud">
        <div class="hudbox">❤️ HP<div class="hpbar"><div id="hpfill" class="hpfill"></div></div></div>
        <div class="hudbox">🎯 Score: <b id="score">0</b> • Wave: <b id="wave">1</b></div>
      </div>
      <div class="mobile">
        <div class="joy" id="joy"><div class="knob" id="knob"></div></div>
        <div class="actions">
          <button class="act" id="gren">💣</button>
          <button class="act" id="dash">⚡</button>
          <button class="act fire" id="fire">🔫</button>
        </div>
      </div>
      <div id="gameOver" class="overlay hidden">
        <div class="modal">
          <h2>GAME OVER</h2>
          <p>Score: <b id="finalScore">0</b></p>
          <button class="primary" id="again">CHƠI LẠI</button>
        </div>
      </div>
    </div>
    <div class="row" style="margin-top:10px">
      <button id="backMenu">← MENU</button>
      <button id="restartGame">↻ RESTART</button>
    </div>
  </section>
</div>
</div>

<script>
(() => {
"use strict";
if(window.__NEON_VALOR__) return;
window.__NEON_VALOR__ = true;

const $ = id => document.getElementById(id);
const sections = ["home","aim","loadout","shop","settings","gameSection"];
function show(name){
  sections.forEach(x => $(x).classList.toggle("hidden", x !== name));
}
$("playTab").onclick=()=>show("home");
$("aimTab").onclick=()=>show("aim");
$("loadTab").onclick=()=>show("loadout");
$("shopTab").onclick=()=>show("shop");
$("settingsTab").onclick=()=>show("settings");
$("start").onclick=()=>{show("gameSection");reset()};
$("aimOpen").onclick=()=>show("aim");
$("loadOpen").onclick=()=>show("loadout");
$("shopOpen").onclick=()=>show("shop");
$("settingsOpen").onclick=()=>show("settings");
$("logout").onclick=()=>show("home");
$("aimBack").onclick=()=>show("home");

let aimLogged=false;
$("aimLoginBtn").onclick=()=>{
  const u=$("aimUser").value.trim(), p=$("aimPass").value;
  if(u==="huymod" && p==="123"){
    aimLogged=true;
    $("aimLogin").classList.add("hidden");
    $("aimPanel").classList.remove("hidden");
    $("loginStatus").textContent="Đăng nhập thành công.";
  }else{
    $("loginStatus").textContent="Sai tài khoản hoặc mật khẩu.";
  }
};
$("aimLogout").onclick=()=>{
  aimLogged=false;
  $("aimPanel").classList.add("hidden");
  $("aimLogin").classList.remove("hidden");
};

function toggle(btn){
  const on=btn.textContent==="ON";
  btn.textContent=on?"OFF":"ON";
}
["aimAssist","esp","box","health","distance"].forEach(id=>$(id).onclick=()=>toggle($(id)));

const c=$("cv"), ctx=c.getContext("2d");
let keys={}, mouse={x:480,y:270,down:false}, joy={x:0,y:0};
let player, bullets, enemies, particles, score, wave, spawnTimer, gameOver, last=0;

function reset(){
  player={x:480,y:270,r:15,hp:100,max:100,angle:0,cool:0,dash:0,grenades:2};
  bullets=[]; enemies=[]; particles=[]; score=0; wave=1; spawnTimer=.2; gameOver=false;
  $("gameOver").classList.add("hidden");
  for(let i=0;i<5;i++) spawnEnemy();
}
function spawnEnemy(){
  const side=Math.floor(Math.random()*4);
  const x=side<2?(side?940:20):Math.random()*940;
  const y=side<2?Math.random()*500:(side==2?20:520);
  enemies.push({x,y,r:14,hp:2+Math.floor(wave*.45),speed:40+wave*3});
}
function updateAim(){
  player.angle=Math.atan2(mouse.y-player.y,mouse.x-player.x);
}
function shoot(){
  if(gameOver || player.cool>0)return;
  player.cool=.16;
  const a=player.angle;
  bullets.push({x:player.x+Math.cos(a)*20,y:player.y+Math.sin(a)*20,
    vx:Math.cos(a)*650,vy:Math.sin(a)*650,r:4});
}
function dash(){
  if(gameOver || player.dash>0)return;
  player.dash=.8;
  player.x=Math.max(20,Math.min(940,player.x+Math.cos(player.angle)*110));
  player.y=Math.max(20,Math.min(520,player.y+Math.sin(player.angle)*110));
}
function grenade(){
  if(gameOver || player.grenades<=0)return;
  player.grenades--;
  const gx=player.x+Math.cos(player.angle)*130, gy=player.y+Math.sin(player.angle)*130;
  for(let i=enemies.length-1;i>=0;i--){
    const e=enemies[i],d=Math.hypot(e.x-gx,e.y-gy);
    if(d<125){e.hp-=4;if(e.hp<=0){score+=25;enemies.splice(i,1)}}
  }
  for(let i=0;i<22;i++) particles.push({x:gx,y:gy,vx:(Math.random()-.5)*240,vy:(Math.random()-.5)*240,t:.45});
}
function update(dt){
  if(gameOver)return;
  player.cool=Math.max(0,player.cool-dt);
  player.dash=Math.max(0,player.dash-dt);
  let dx=(keys.d?1:0)-(keys.a?1:0)+joy.x;
  let dy=(keys.s?1:0)-(keys.w?1:0)+joy.y;
  const len=Math.hypot(dx,dy);
  if(len){dx/=len;dy/=len;player.x+=dx*190*dt;player.y+=dy*190*dt}
  player.x=Math.max(20,Math.min(940,player.x));
  player.y=Math.max(20,Math.min(520,player.y));
  updateAim();

  spawnTimer-=dt;
  if(spawnTimer<=0){
    spawnTimer=Math.max(.35,1.15-wave*.035);
    if(enemies.length<Math.min(18,4+wave*2))spawnEnemy();
  }
  for(const b of bullets){b.x+=b.vx*dt;b.y+=b.vy*dt}
  bullets=bullets.filter(b=>b.x>-20&&b.x<980&&b.y>-20&&b.y<560);

  for(const e of enemies){
    const a=Math.atan2(player.y-e.y,player.x-e.x);
    e.x+=Math.cos(a)*e.speed*dt;e.y+=Math.sin(a)*e.speed*dt;
    if(Math.hypot(player.x-e.x,player.y-e.y)<player.r+e.r){
      player.hp-=18*dt;
      if(player.hp<=0){player.hp=0;endGame()}
    }
  }

  for(let i=enemies.length-1;i>=0;i--){
    const e=enemies[i];
    for(let j=bullets.length-1;j>=0;j--){
      const b=bullets[j];
      if(Math.hypot(e.x-b.x,e.y-b.y)<e.r+b.r){
        e.hp--;bullets.splice(j,1);
        if(e.hp<=0){score+=10;enemies.splice(i,1)}
        break;
      }
    }
  }
  for(const q of particles){q.x+=q.vx*dt;q.y+=q.vy*dt;q.t-=dt}
  particles=particles.filter(q=>q.t>0);

  wave=1+Math.floor(score/100);
  $("score").textContent=score;
  $("wave").textContent=wave;
  $("hpfill").style.width=(player.hp/player.max*100)+"%";
}
function endGame(){
  gameOver=true;
  $("finalScore").textContent=score;
  $("gameOver").classList.remove("hidden");
}
function draw(){
  ctx.clearRect(0,0,960,540);
  ctx.fillStyle="#0d1422";ctx.fillRect(0,0,960,540);
  ctx.strokeStyle="#1a2537";ctx.lineWidth=1;
  for(let x=0;x<=960;x+=40){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,540);ctx.stroke()}
  for(let y=0;y<=540;y+=40){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(960,y);ctx.stroke()}
  ctx.fillStyle="#27344a";
  for(let i=0;i<12;i++){const x=(i*173)%900+30,y=(i*97)%480+30;ctx.fillRect(x,y,28,28)}

  // Decorative site zones
  ctx.strokeStyle="#40506b";ctx.strokeRect(70,70,220,150);ctx.strokeRect(670,320,220,150);
  ctx.fillStyle="#7d8ba2";ctx.font="bold 14px system-ui";ctx.fillText("A SITE",85,92);ctx.fillText("B SITE",685,342);

  for(const q of particles){ctx.globalAlpha=Math.max(0,q.t/.45);ctx.fillStyle="#ffd166";ctx.beginPath();ctx.arc(q.x,q.y,4,0,Math.PI*2);ctx.fill()}ctx.globalAlpha=1;
  for(const b of bullets){ctx.fillStyle="#e8f1ff";ctx.beginPath();ctx.arc(b.x,b.y,b.r,0,Math.PI*2);ctx.fill()}

  for(const e of enemies){
    const showEsp=aimLogged && $("esp").textContent==="ON";
    if(showEsp && $("box").textContent==="ON"){
      ctx.strokeStyle="#ff526d";ctx.strokeRect(e.x-19,e.y-22,38,44);
    }
    ctx.fillStyle="#e4475f";ctx.beginPath();ctx.arc(e.x,e.y,e.r,0,Math.PI*2);ctx.fill();
    ctx.fillStyle="#101722";ctx.fillRect(e.x-8,e.y-3,16,5);
    if(showEsp && $("health").textContent==="ON"){
      ctx.fillStyle="#303746";ctx.fillRect(e.x-16,e.y-25,32,4);
      ctx.fillStyle="#35d07f";ctx.fillRect(e.x-16,e.y-25,32*Math.max(0,e.hp/(2+Math.floor(wave*.45))),4);
    }
    if(showEsp && $("distance").textContent==="ON"){
      ctx.fillStyle="#d7deea";ctx.font="10px system-ui";ctx.fillText(Math.round(Math.hypot(player.x-e.x,player.y-e.y))+"m",e.x-13,e.y+29);
    }
  }

  ctx.save();ctx.translate(player.x,player.y);ctx.rotate(player.angle);
  ctx.fillStyle="#45a7ff";ctx.beginPath();ctx.arc(0,0,player.r,0,Math.PI*2);ctx.fill();
  ctx.fillStyle="#dcecff";ctx.fillRect(8,-5,28,10);ctx.restore();

  if(aimLogged && $("aimAssist").textContent==="ON"){
    const fov=Number($("fov").value);
    ctx.save();ctx.strokeStyle="#67a9ff55";ctx.beginPath();ctx.arc(player.x,player.y,fov,player.angle-fov*Math.PI/360,player.angle+fov*Math.PI/360);ctx.stroke();ctx.restore();
  }
}
function loop(t){
  const dt=Math.min(.033,(t-last)/1000||0);last=t;
  update(dt);draw();requestAnimationFrame(loop);
}
window.addEventListener("keydown",e=>{
  keys[e.key.toLowerCase()]=true;
  if(e.code==="Space"){e.preventDefault();dash()}
  if(e.key.toLowerCase()==="g")grenade();
});
window.addEventListener("keyup",e=>keys[e.key.toLowerCase()]=false);
c.addEventListener("pointermove",e=>{
  const r=c.getBoundingClientRect();
  mouse.x=(e.clientX-r.left)*960/r.width;
  mouse.y=(e.clientY-r.top)*540/r.height;
});
c.addEventListener("pointerdown",e=>{
  if(e.pointerType!=="touch"){mouse.down=true;shoot()}
});
window.addEventListener("pointerup",()=>mouse.down=false);
setInterval(()=>{if(mouse.down)shoot()},80);

$("fire").addEventListener("pointerdown",e=>{e.preventDefault();shoot()});
$("dash").addEventListener("pointerdown",e=>{e.preventDefault();dash()});
$("gren").addEventListener("pointerdown",e=>{e.preventDefault();grenade()});

const joyEl=$("joy"),knob=$("knob");
function joyMove(e){
  const r=joyEl.getBoundingClientRect(),cx=r.left+r.width/2,cy=r.top+r.height/2;
  let dx=e.clientX-cx,dy=e.clientY-cy,m=Math.hypot(dx,dy),lim=38;
  if(m>lim){dx=dx/m*lim;dy=dy/m*lim}
  joy.x=dx/lim;joy.y=dy/lim;knob.style.transform=`translate(${dx}px,${dy}px)`;
}
joyEl.addEventListener("pointerdown",e=>{joyEl.setPointerCapture(e.pointerId);joyMove(e)});
joyEl.addEventListener("pointermove",joyMove);
joyEl.addEventListener("pointerup",()=>{joy.x=joy.y=0;knob.style.transform="translate(0,0)"});

$("backMenu").onclick=()=>show("home");
$("restartGame").onclick=reset;
$("again").onclick=reset;
$("gameOver").addEventListener("pointerdown",e=>{if(e.target===$("gameOver"))e.stopPropagation()});

reset();show("home");requestAnimationFrame(loop);
})();
</script>
</body>
</html>
"""

st.markdown("## 🔥 NEON VALOR")
st.caption("Bản prototype Streamlit • PC + điện thoại • AIM/ESP có đăng nhập riêng: huymod / 123")
components.html(GAME_HTML, height=900, scrolling=False)
