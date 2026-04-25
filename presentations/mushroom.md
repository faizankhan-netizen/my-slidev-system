---
theme: seriph
background: '#064E3B'
highlighter: shiki
lineNumbers: false
transition: fade
title: Mushroom Farming — Wealth from Waste
canvasWidth: 900
---

<style>
/* ABSOLUTE GLOBAL RESET FOR FULL-BLEED */
body, #app, #slide-container, .slidev-slides-container, .slidev-layout {
  background: #064E3B !important; /* Default to dark green to hide borders */
  margin: 0 !important;
  padding: 0 !important;
}

/* Specific layout styles with built-in safe-zone padding */
.slidev-layout.slide-green {
  background: #064E3B !important;
  padding: 3.5rem !important; /* Increased padding for safety */
  display: flex;
  flex-direction: column;
}
.slidev-layout.slide-light {
  background: #F5F7FF !important;
  padding: 3.5rem !important;
  display: flex;
  flex-direction: column;
}

/* Decorative circles via pseudo-elements - positioned relative to layout */
.slide-green::before {
  content:""; position:absolute; border-radius:50%;
  width:400px; height:400px; top:-150px; right:-150px;
  background:#065F46; z-index:0; pointer-events:none;
}
.slide-light::before {
  content:""; position:absolute; border-radius:50%;
  width:350px; height:350px; top:-120px; left:-120px;
  background:#F59E0B; opacity:0.07; z-index:0; pointer-events:none;
}

/* Content wrapper with NO fixed height to prevent overflow/clipping */
.content-wrapper {
  position:relative;
  z-index:10;
  width: 100%;
}

.pill {
  display:inline-block; background:#F59E0B; color:#451a03;
  font-size:10px; font-weight:900; letter-spacing:0.25em;
  padding:6px 16px; border-radius:9999px; text-transform:uppercase;
  margin-bottom: 1.5rem;
}
.card {
  background:white; border-radius:20px; padding:1.2rem;
  box-shadow:0 12px 30px rgba(0,0,0,0.08); border-bottom:5px solid #F59E0B;
}
</style>

<!-- SLIDE 1: COVER -->
---
class: slide-green
---
<div class="content-wrapper">
  <div style="display:flex; align-items:center; gap:2.5rem; margin-top: 1rem;">
    <div style="flex:1.2">
      <div class="pill">KRISHI VIGYAN · SEMINAR</div>
      <div style="font-size:3.5rem;font-weight:900;color:white;line-height:1;letter-spacing:-0.03em; margin-bottom:0.5rem">Mushroom</div>
      <div style="font-size:3.5rem;font-weight:900;color:#FFD166;line-height:1;letter-spacing:-0.03em; margin-bottom:1.5rem">Farming.</div>
      <div style="font-size:1.1rem;color:#A7F3D0;font-weight:700">Wealth from Waste • Big Profit</div>
    </div>
    <div style="flex:0.8; border-radius:24px; overflow:hidden; box-shadow:0 20px 40px rgba(0,0,0,0.3); border:4px solid rgba(255,255,255,0.1)">
      <img src="/cover.png" style="width:100%; height:240px; object-fit:cover" />
    </div>
  </div>
</div>

---
class: slide-light
---
<!-- SLIDE 2: THE MONEY MAP -->
<div class="content-wrapper">
  <div class="pill" style="background:#064E3B; color:white">WHY DO THIS?</div>
  <div style="font-size:2.8rem;font-weight:900;color:#064E3B;letter-spacing:-0.03em; margin-bottom: 2rem;">Grow Gold in a Room</div>
  <div style="display:flex; gap:15px; align-items: stretch;">
    <div v-click class="card" style="flex:1; text-align:center">
      <div style="font-size:2.5rem;margin-bottom:0.8rem">🏠</div>
      <div style="font-size:1.2rem;font-weight:900;color:#064E3B;margin-bottom:0.3rem">Any Room</div>
      <div style="font-size:0.9rem;color:#64748B">Grow inside your house.</div>
    </div>
    <div v-click class="card" style="flex:1; text-align:center; border-bottom-color:#059669">
      <div style="font-size:2.5rem;margin-bottom:0.8rem">📅</div>
      <div style="font-size:1.2rem;font-weight:900;color:#064E3B;margin-bottom:0.3rem">Fast Money</div>
      <div style="font-size:0.9rem;color:#64748B">Harvest in 30 days.</div>
    </div>
    <div v-click class="card" style="flex:1; text-align:center; border-bottom-color:#F97316">
      <div style="font-size:2.5rem;margin-bottom:0.8rem">💰</div>
      <div style="font-size:1.2rem;font-weight:900;color:#064E3B;margin-bottom:0.3rem">High Price</div>
      <div style="font-size:0.9rem;color:#64748B">Sells for ₹300 per kg.</div>
    </div>
  </div>
</div>

---
class: slide-green
---
<!-- SLIDE 3: STEP 1 - THE HOUSE -->
<div class="content-wrapper">
  <div class="pill">STEP 1</div>
  <div style="font-size:2.8rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 2rem;">The Mushroom House</div>
  <div style="display:flex; gap:2.5rem; align-items:center">
    <div style="flex:1">
      <div v-click style="display:flex; align-items:center; gap:1rem; margin-bottom:1rem; background:rgba(255,255,255,0.08); padding:1.2rem; border-radius:16px; border-left:5px solid #FFD166">
        <div style="font-size:2rem">🌑</div>
        <div>
          <div style="font-size:1.2rem;font-weight:900;color:white">Dark &amp; Cool</div>
          <div style="font-size:0.9rem;color:#A7F3D0">Keep it dark.</div>
        </div>
      </div>
      <div v-click style="display:flex; align-items:center; gap:1rem; background:rgba(255,255,255,0.08); padding:1.2rem; border-radius:16px; border-left:5px solid #FFD166">
        <div style="font-size:2rem">🚿</div>
        <div>
          <div style="font-size:1.2rem;font-weight:900;color:white">Wet &amp; Fresh</div>
          <div style="font-size:0.9rem;color:#A7F3D0">Keep it humid.</div>
        </div>
      </div>
    </div>
    <div v-click style="flex:1; background:#047857; padding:1.5rem; border-radius:24px; text-align:center; box-shadow:0 10px 20px rgba(0,0,0,0.2)">
      <div style="font-size:3rem; margin-bottom:0.5rem">🌡️</div>
      <div style="font-size:1.5rem; font-weight:900; color:#FFD166">20°C - 28°C</div>
      <div style="font-size:0.9rem; color:white; opacity:0.8">Happy Temperature</div>
    </div>
  </div>
</div>

---
class: slide-light
---
<!-- SLIDE 4: STEP 2 - THE BAGS -->
<div class="content-wrapper">
  <div class="pill" style="background:#064E3B; color:white">STEP 2</div>
  <div style="font-size:2.8rem;font-weight:900;color:#064E3B;letter-spacing:-0.03em; margin-bottom: 2rem;">Making the "Bed"</div>
  <div style="display:flex; gap:12px; margin-bottom: 2rem;">
    <div v-click class="card" style="flex:1; text-align:center; border-bottom-color:#92400E">
      <div style="font-size:2.2rem;margin-bottom:0.6rem">🌾</div>
      <div style="font-size:1.1rem;font-weight:900;color:#064E3B">Boil Straw</div>
    </div>
    <div v-click class="card" style="flex:1; text-align:center; border-bottom-color:#059669">
      <div style="font-size:2.2rem;margin-bottom:0.6rem">🍄</div>
      <div style="font-size:1.1rem;font-weight:900;color:#064E3B">Add Spores</div>
    </div>
    <div v-click class="card" style="flex:1; text-align:center; border-bottom-color:#2563EB">
      <div style="font-size:2.2rem;margin-bottom:0.6rem">🛍️</div>
      <div style="font-size:1.1rem;font-weight:900;color:#064E3B">Pack Bags</div>
    </div>
  </div>
  <div v-click style="background:#064E3B; color:white; padding:1.2rem; border-radius:16px; text-align:center">
    <div style="font-size:1.2rem;font-weight:900;color:#FFD166">Wait for 21 Days</div>
    <div style="font-size:0.9rem;opacity:0.8">The bag will turn completely <strong style="color:#FFD166">WHITE</strong>.</div>
  </div>
</div>

---
class: slide-green
---
<!-- SLIDE 5: HARVEST & CASH -->
<div class="content-wrapper text-center">
  <div class="pill">THE PAYDAY</div>
  <div style="font-size:3.5rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 0.5rem; line-height:1">Pick &amp; Profit.</div>
  <div style="font-size:1.5rem;color:#FFD166;font-weight:900;margin-bottom:2.5rem">From Waste to Cash</div>
  <div style="display:flex; gap:20px; justify-content:center">
    <div v-click style="background:rgba(255,255,255,0.08); border-radius:20px; padding:1.5rem; width:250px; border:1px solid rgba(255,255,255,0.15)">
      <div style="font-size:3.5rem;margin-bottom:0.8rem">👐</div>
      <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.3rem">Twist &amp; Pull</div>
      <div style="font-size:0.9rem;color:#A7F3D0">Don't use a knife.</div>
    </div>
    <div v-click style="background:#F59E0B; border-radius:20px; padding:1.5rem; width:250px; color:#451a03; box-shadow:0 15px 30px rgba(0,0,0,0.2)">
      <div style="font-size:3.5rem;margin-bottom:0.8rem">🏬</div>
      <div style="font-size:1.2rem;font-weight:900;margin-bottom:0.3rem">Sell Fresh</div>
      <div style="font-size:0.9rem;opacity:0.9">Hotels love fresh!</div>
    </div>
  </div>
</div>

---