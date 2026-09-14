import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Fishing Quest", page_icon="🎣", layout="centered")

html = r"""
<!doctype html><html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no">
<style>
*{box-sizing:border-box}html,body{margin:0;background:#071827;font-family:Arial,sans-serif;overflow:hidden;touch-action:none}
#game{position:relative;margin:auto;width:min(100vw,460px);height:min(760px,calc(100svh - 8px));min-height:600px;overflow:hidden;border:4px solid #17344b;border-radius:24px;background:linear-gradient(#72d6ff 0 36%,#239bd0 36% 43%,#0874a5 43%);box-shadow:0 18px 55px #0008}
#sun{position:absolute;right:28px;top:35px;width:70px;height:70px;border-radius:50%;background:#ffe477;box-shadow:0 0 35px #fff5}
.cloud{position:absolute;background:#fff9;width:105px;height:28px;border-radius:30px}.cloud:before,.cloud:after{content:"";position:absolute;background:inherit;border-radius:50%}.cloud:before{width:45px;height:45px;left:18px;top:-22px}.cloud:after{width:55px;height:50px;left:53px;top:-27px}.c1{top:80px;left:25px}.c2{top:150px;right:-25px;transform:scale(.8)}
#water{position:absolute;left:0;right:0;top:36%;bottom:0;background:repeating-linear-gradient(0deg,#086f9e 0 22px,#0878a8 22px 44px)}
.wave{position:absolute;left:-10%;width:120%;height:15px;border-radius:50%;border-top:5px solid #64d4ef;opacity:.7}.w1{top:7%}.w2{top:18%}.w3{top:31%}.w4{top:47%}.w5{top:66%}
#boat{position:absolute;top:27%;left:50%;transform:translateX(-50%);width:170px;height:72px;z-index:5}
#boat .body{position:absolute;bottom:0;width:170px;height:40px;background:#a95c32;border:5px solid #482b27;border-radius:8px 8px 55px 55px}
#boat .seat{position:absolute;left:48px;top:13px;width:75px;height:18px;background:#e8a44d;border:4px solid #482b27;border-radius:5px}
#person{position:absolute;left:69px;top:-17px;width:35px;height:35px;background:#ffd2a0;border:4px solid #482b27;border-radius:50%;z-index:2}
#hat{position:absolute;left:57px;top:-29px;width:60px;height:22px;background:#ef6b52;border:4px solid #482b27;border-radius:18px 18px 4px 4px;z-index:3}
#rod{position:absolute;left:98px;top:-63px;width:7px;height:90px;background:#5a3d2f;transform:rotate(14deg);transform-origin:bottom;z-index:1}
#line{position:absolute;left:124px;top:13px;width:2px;height:155px;background:#fff;opacity:.85;z-index:1}
#bobber{position:absolute;left:119px;top:162px;width:17px;height:17px;background:#ff5c5c;border:3px solid #482b27;border-radius:50%;z-index:7}
#hook{position:absolute;left:125px;top:174px;width:9px;height:15px;border-left:3px solid white;border-bottom:3px solid white;border-radius:0 0 9px 9px;z-index:7}
#hud{position:absolute;top:16px;left:16px;right:16px;display:flex;justify-content:space-between;z-index:20}.badge{background:#153c58e8;color:#fff;border:3px solid #0b2538;border-radius:16px;padding:9px 13px;font-weight:900;font-size:16px;box-shadow:0 5px #0b2538}
#catch{position:absolute;top:93px;left:50%;transform:translateX(-50%);color:#fff;font-size:21px;font-weight:900;text-shadow:0 3px #12445d;z-index:20;text-align:center;width:90%}
#fishArea{position:absolute;inset:43% 0 0;z-index:4}.fish{position:absolute;width:48px;height:28px;border-radius:55% 45% 45% 55%;border:3px solid #163a4d;box-shadow:inset -7px -4px #0002}.fish:before{content:"";position:absolute;right:5px;top:7px;width:6px;height:6px;background:#111;border-radius:50%}.fish:after{content:"";position:absolute;left:-15px;top:4px;border-top:9px solid transparent;border-bottom:9px solid transparent;border-right:17px solid currentColor}.f1{background:#ffbd43;color:#ffbd43;top:25%;left:12%;animation:swim1 8s linear infinite}.f2{background:#ff6d73;color:#ff6d73;top:47%;left:70%;animation:swim2 10s linear infinite}.f3{background:#7be08b;color:#7be08b;top:68%;left:28%;animation:swim1 12s linear infinite reverse}@keyframes swim1{from{transform:translateX(-40px)}to{transform:translateX(360px)}}@keyframes swim2{from{transform:translateX(300px) scaleX(-1)}to{transform:translateX(-300px) scaleX(-1)}}
#menu{position:absolute;inset:0;z-index:50;background:#06203855;backdrop-filter:blur(2px);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:25px}h1{margin:0 0 7px;color:#fff;font-size:48px;font-weight:1000;letter-spacing:2px;text-shadow:0 6px #15445f}.sub{color:#dff8ff;font-weight:800;margin-bottom:22px}button{border:4px solid #173246;border-radius:15px;background:linear-gradient(#ffd85b,#f3a92f);color:#4b3022;padding:13px 28px;font-size:22px;font-weight:1000;box-shadow:0 7px #173246;cursor:pointer}button:active{transform:translateY(5px);box-shadow:0 2px #173246}#start{font-size:28px;min-width:220px}#instructions{margin-top:22px;color:#fff;text-align:center;font-weight:800;line-height:1.6}
#fishCard{display:none;position:absolute;z-index:40;left:50%;top:50%;transform:translate(-50%,-50%);width:84%;background:#f8fdff;border:5px solid #173246;border-radius:22px;padding:22px;text-align:center;box-shadow:0 12px 40px #0008}#fishEmoji{font-size:70px}#fishName{font-size:25px;font-weight:1000;color:#173246}.gold{color:#e49b18;font-weight:1000;font-size:25px}#tap{position:absolute;inset:43% 0 0;z-index:12}#power{position:absolute;left:50%;bottom:22px;transform:translateX(-50%);width:220px;height:18px;border:3px solid #173246;background:#d9f7ff;border-radius:15px;z-index:25;overflow:hidden}#bar{height:100%;width:20%;background:#ffcf43}
</style></head><body><div id="game">
<div id="sun"></div><div class="cloud c1"></div><div class="cloud c2"></div><div id="water"><div class="wave w1"></div><div class="wave w2"></div><div class="wave w3"></div><div class="wave w4"></div><div class="wave w5"></div></div>
<div id="hud"><div class="badge">💰 Xu: <span id="coins">0</span></div><div class="badge">🏆 Kỷ lục: <span id="best">0</span></div></div><div id="catch">🎣 Nhấn CHƠI để câu cá!</div>
<div id="boat"><div id="rod"></div><div id="line"></div><div id="bobber"></div><div id="hook"></div><div id="person"></div><div id="hat"></div><div class="seat"></div><div class="body"></div></div>
<div id="fishArea"><div class="fish f1"></div><div class="fish f2"></div><div class="fish f3"></div></div><div id="tap"></div><div id="power"><div id="bar"></div></div>
<div id="fishCard"><div id="fishEmoji">🐟</div><div id="fishName">Cá</div><div class="gold">+<span id="reward">10</span> xu</div><button id="again">🎣 CÂU TIẾP</button></div>
<div id="menu"><h1>🎣 FISHING QUEST</h1><div class="sub">CÂU CÁ • KIẾM XU • SĂN CÁ HIẾM</div><button id="start">▶ CHƠI</button><div id="instructions">📱 Chạm màn hình / nhấn SPACE để thả câu<br>🎯 Khi cá cắn câu, nhấn thật nhanh để kéo cá lên!</div></div>
</div>
<script>
const menu=document.getElementById("menu"),tap=document.getElementById("tap"),card=document.getElementById("fishCard"),catchText=document.getElementById("catch"),bar=document.getElementById("bar");
let playing=false,bite=false,coins=+localStorage.fishCoins||0,best=+localStorage.fishBest||0,timer=null,score=0;
document.getElementById("coins").textContent=coins;document.getElementById("best").textContent=best;
const fish=[["🐟","Cá xanh",8,55],["🐠","Cá nhiệt đới",15,25],["🐡","Cá nóc",25,12],["🦑","Mực khổng lồ",40,6],["🦈","Cá mập",100,2]];
function start(){playing=true;score=0;menu.style.display="none";card.style.display="none";cast()}
function cast(){if(!playing)return;bite=false;bar.style.width="20%";catchText.textContent="🎣 Đang chờ cá cắn...";clearTimeout(timer);timer=setTimeout(()=>{bite=true;bar.style.width="100%";catchText.textContent="‼️ CÁ CẮN CÂU! NHẤN NGAY!";},1300+Math.random()*3500)}
function reel(){if(!playing)return;if(bite){clearTimeout(timer);bite=false;catchFish()}else{catchText.textContent="🌊 Chưa có cá...";bar.style.width="35%"}}
function catchFish(){let r=Math.random()*100,a=0,p=fish[0];for(const f of fish){a+=f[3];if(r<a){p=f;break}}coins+=p[2];score++;if(score>best)best=score;localStorage.fishCoins=coins;localStorage.fishBest=best;document.getElementById("coins").textContent=coins;document.getElementById("best").textContent=best;document.getElementById("fishEmoji").textContent=p[0];document.getElementById("fishName").textContent=p[1];document.getElementById("reward").textContent=p[2];card.style.display="block";bar.style.width="0%"}
function action(e){if(e)e.preventDefault();if(!playing)start();else reel()}
document.getElementById("start").onclick=start;document.getElementById("again").onclick=()=>{card.style.display="none";cast()};tap.addEventListener("pointerdown",action);document.addEventListener("keydown",e=>{if(e.code==="Space"){e.preventDefault();action(e)}});
</script></body></html>
"""

components.html(html, height=770, scrolling=False)
