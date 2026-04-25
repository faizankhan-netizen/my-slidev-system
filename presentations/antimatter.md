---
theme: seriph
background: '#020617'
highlighter: shiki
lineNumbers: false
transition: slide-left
title: Antimatter — The Cosmic Mirror
canvasWidth: 900
---

<style>
/* GLOBAL SOVEREIGNTY RESET - Applied to body and layout to ensure full-bleed */
body, #app, .slidev-layout {
  background: #020617 !important;
  margin: 0 !important;
  padding: 0 !important;
}

/* Specific layout styles with mandatory safety padding */
.slidev-layout.slide-dark {
  background: #020617 !important;
  padding: 3.5rem !important;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* Prevent pills from stretching full-width */
}
.slidev-layout.slide-cyan {
  background: #083344 !important;
  padding: 3.5rem !important;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

/* Pseudo-element decorative glows */
.slide-dark::before {
  content:""; position:absolute; border-radius:50%;
  width:500px; height:500px; top:-200px; right:-200px;
  background: radial-gradient(circle, rgba(139,92,246,0.15) 0%, transparent 70%);
  z-index:0; pointer-events:none;
}

/* UI Elements */
.content-wrapper { 
  position:relative; z-index:10; width:100%; 
  display:flex; flex-direction:column; align-items: flex-start;
}
.pill {
  display:inline-block; background:rgba(139,92,246,0.2); color:#A78BFA;
  font-size:10px; font-weight:900; letter-spacing:0.3em;
  padding:6px 16px; border-radius:9999px; text-transform:uppercase; margin-bottom: 1.5rem;
  border: 1px solid rgba(139,92,246,0.3);
}
.glow-card {
  background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);
  border-radius:24px; padding:1.5rem; backdrop-filter: blur(10px);
  box-shadow: 0 20px 50px rgba(0,0,0,0.3);
}
.formula { font-family: 'JetBrains Mono', monospace; color: #22D3EE; font-weight: 700; }
</style>

<!-- SLIDE 1: COVER -->
<div class="content-wrapper">
  <div style="display:flex; align-items:center; gap:3rem; margin-top: 1.5rem;">
    <div style="flex:1.2">
      <div class="pill">PHYSICS · SPECIAL SEMINAR</div>
      <div style="font-size:3.5rem;font-weight:900;color:white;line-height:1.1;letter-spacing:-0.03em; margin-bottom:0.5rem">Antimatter.</div>
      <div style="font-size:1.6rem;font-weight:700;color:#8B5CF6;margin-bottom:2rem">The Mirror of Reality</div>
      <div style="font-size:1.05rem;color:#94A3B8;line-height:1.5; max-width:400px">Explore the most expensive substance on Earth and the mystery of our missing universe.</div>
    </div>
    <div style="flex:0.8; border-radius:30px; overflow:hidden; box-shadow:0 25px 60px rgba(139,92,246,0.3); border:1px solid rgba(139,92,246,0.5)">
      <img src="/antimatter_cover.webp" style="width:100%; height:auto; object-fit:cover" />
    </div>
  </div>
</div>

---
class: slide-dark
---
<!-- SLIDE 2: THE CONCEPT -->
<div class="content-wrapper">
  <div class="pill">THE CONCEPT</div>
  <div style="font-size:2.8rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 2rem;">Everything has a Twin.</div>
  <div style="display:flex; gap:20px; width:100%">
    <div v-click class="glow-card" style="flex:1; border-top: 4px solid #22D3EE">
      <div style="font-size:1.3rem;font-weight:900;color:#22D3EE;margin-bottom:0.5rem">Matter</div>
      <div style="font-size:0.95rem;color:#94A3B8">The stuff you are made of. Atoms, cells, stars.</div>
    </div>
    <div v-click style="display:flex; align-items:center; font-size:2rem; color:#8B5CF6">↔</div>
    <div v-click class="glow-card" style="flex:1; border-top: 4px solid #EC4899">
      <div style="font-size:1.3rem;font-weight:900;color:#EC4899;margin-bottom:0.5rem">Antimatter</div>
      <div style="font-size:0.95rem;color:#94A3B8">Identical mass, but <b style="color:white">Opposite Charge</b>.</div>
    </div>
  </div>
  <div v-click style="margin-top:2rem; background:rgba(255,255,255,0.05); padding:1.2rem; border-radius:20px; border-left:6px solid #8B5CF6; width:100%">
    <div style="font-size:1.1rem;font-weight:700">Matter + Antimatter = <span style="color:#22D3EE">KABOOM!</span></div>
    <div style="font-size:0.95rem;opacity:0.7">When they touch, they vanish into pure energy.</div>
  </div>
</div>

---
class: slide-dark
---
<!-- SLIDE 3: DIRAC'S EQUATION -->
<div class="content-wrapper">
  <div class="pill">1928: THE DISCOVERY</div>
  <div style="font-size:2.8rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 2rem;">Paul Dirac's "Crazy" Math</div>
  <div style="display:flex; gap:2.5rem; align-items:center; width:100%">
    <div style="flex:1">
      <div v-click style="font-size:1rem; color:#CBD5E1; line-height:1.5; margin-bottom:1.5rem">Dirac combined <b style="color:white">Quantum Mechanics</b> and <b style="color:white">Relativity</b>, finding an equation with TWO solutions.</div>
      <div v-click style="background:#0F172A; padding:1.5rem; border-radius:20px; text-align:center; border:1px solid #22D3EE">
        <div style="font-size:2rem" class="formula">E = ±mc²</div>
        <div style="font-size:0.9rem; color:#22D3EE; margin-top:0.5rem">Prediction: The Positron</div>
      </div>
    </div>
    <div v-click style="flex:1; background:rgba(139,92,246,0.1); border:1px dashed #8B5CF6; padding:1.5rem; border-radius:24px">
      <div style="font-size:1.2rem; font-weight:900; color:#8B5CF6; margin-bottom:0.8rem">The Mirror Universe</div>
      <div style="font-size:0.95rem; color:#94A3B8">He predicted antimatter before it was ever seen in a lab.</div>
    </div>
  </div>
</div>

---
class: slide-dark
---
<!-- SLIDE 4: THE PROPERTIES -->
<div class="content-wrapper">
  <div class="pill">PARTICLE VS ANTI-PARTICLE</div>
  <div style="font-size:2.8rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 2rem;">Mirror Properties</div>
  <table style="width:100%; border-collapse: separate; border-spacing: 0 8px;">
    <tr style="color:#94A3B8; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.1em">
      <th style="text-align:left; padding:8px">Property</th>
      <th style="text-align:center">Electron (e⁻)</th>
      <th style="text-align:center">Positron (e⁺)</th>
    </tr>
    <tr v-click class="glow-card" style="background:rgba(255,255,255,0.02)">
      <td style="padding:12px; font-weight:700">Mass</td>
      <td style="text-align:center">9.1 × 10⁻³¹ kg</td>
      <td style="text-align:center; color:#22D3EE">SAME</td>
    </tr>
    <tr v-click class="glow-card" style="background:rgba(255,255,255,0.02)">
      <td style="padding:12px; font-weight:700">Charge</td>
      <td style="text-align:center">-1</td>
      <td style="text-align:center; color:#EC4899">+1 (Opposite)</td>
    </tr>
    <tr v-click class="glow-card" style="background:rgba(255,255,255,0.02)">
      <td style="padding:12px; font-weight:700">Spin</td>
      <td style="text-align:center">1/2</td>
      <td style="text-align:center; color:#22D3EE">SAME</td>
    </tr>
  </table>
</div>

---
class: slide-cyan
---
<!-- SLIDE 5: ANNIHILATION -->
<div class="content-wrapper items-center text-center">
  <div class="pill" style="background:rgba(255,255,255,0.1); color:white">THE POWER</div>
  <div style="font-size:3.2rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 0.8rem; line-height:1">Total Annihilation</div>
  <div style="font-size:1.3rem;color:#22D3EE;font-weight:700;margin-bottom:2.5rem">1 gram = Hiroshima Bomb × 3</div>
  <div style="display:flex; gap:20px; justify-content:center; width:100%">
    <div v-click class="glow-card" style="flex:1; border-bottom: 5px solid #EC4899">
      <div style="font-size:2.5rem;margin-bottom:0.8rem">💥</div>
      <div style="font-size:1.1rem;font-weight:900;color:white;margin-bottom:0.3rem">100% Efficiency</div>
      <div style="font-size:0.85rem;color:#A5F3FC">Converts all mass to energy.</div>
    </div>
    <div v-click class="glow-card" style="flex:1; border-bottom: 5px solid #22D3EE">
      <div style="font-size:2.5rem;margin-bottom:0.8rem">🚀</div>
      <div style="font-size:1.1rem;font-weight:900;color:white;margin-bottom:0.3rem">Starship Fuel</div>
      <div style="font-size:0.85rem;color:#A5F3FC">Ultimate fuel for deep space.</div>
    </div>
  </div>
</div>

---
class: slide-dark
---
<!-- SLIDE 6: THE MISSING UNIVERSE -->
<div class="content-wrapper">
  <div class="pill">THE BIG BANG PUZZLE</div>
  <div style="font-size:2.8rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 2rem;">Where did it all go?</div>
  <div style="display:flex; gap:2.5rem; align-items:center; width:100%">
    <div style="flex:1">
      <div v-click style="background:rgba(236,72,153,0.1); padding:1.2rem; border-radius:20px; border-left:6px solid #EC4899; margin-bottom:1.2rem">
        <div style="font-size:1.1rem; font-weight:900">The 1:1,000,000,001 Rule</div>
        <div style="font-size:0.85rem; opacity:0.8; margin-top:0.4rem">For every 1 billion pairs, there was 1 extra matter particle.</div>
      </div>
      <div v-click style="font-size:1rem; color:#CBD5E1; line-height:1.5">The rest annihilated. That "leftover" matter is <b style="color:#22D3EE">Everything We See</b>.</div>
    </div>
    <div v-click style="flex:0.7; text-align:center">
      <div style="font-size:4rem">⚖️</div>
      <div style="font-size:1.3rem; font-weight:900; color:#8B5CF6">Baryon Asymmetry</div>
    </div>
  </div>
</div>

---
class: slide-dark
---
<!-- SLIDE 7: MAKING IT (CERN) -->
<div class="content-wrapper">
  <div class="pill">CERN · SWITZERLAND</div>
  <div style="font-size:2.8rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 2rem;">Making Antimatter</div>
  <div style="display:flex; gap:15px; width:100%">
    <div v-click class="glow-card" style="flex:1">
      <div style="font-size:1.2rem;font-weight:900;color:#22D3EE;margin-bottom:0.5rem">Slamming Protons</div>
      <div style="font-size:0.85rem;color:#94A3B8">High energy collisions create pairs from pure energy.</div>
    </div>
    <div v-click class="glow-card" style="flex:1">
      <div style="font-size:1.2rem;font-weight:900;color:#8B5CF6;margin-bottom:0.5rem">Slowing Down</div>
      <div style="font-size:0.85rem;color:#94A3B8">We use "Decelerators" to catch antiprotons.</div>
    </div>
  </div>
  <div v-click style="margin-top:2rem; background:rgba(34,211,238,0.1); padding:1rem; border-radius:16px; text-align:center; width:100%">
    <span style="font-size:1rem;font-weight:900;color:#22D3EE">$62 Trillion per gram!</span>
  </div>
</div>

---
class: slide-dark
---
<!-- SLIDE 8: STORING IT -->
<div class="content-wrapper">
  <div class="pill">THE PENNING TRAP</div>
  <div style="font-size:2.8rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 2rem;">Magnet Magic</div>
  <div style="display:flex; gap:2.5rem; align-items:center; width:100%">
    <div style="flex:1">
      <div v-click style="display:flex; align-items:center; gap:1rem; margin-bottom:1.2rem; background:rgba(255,255,255,0.05); padding:1rem; border-radius:16px; border-left:5px solid #22D3EE">
        <div style="font-size:2rem">🧲</div>
        <div>
          <div style="font-size:1.1rem;font-weight:900;color:white">Magnetic Fields</div>
          <div style="font-size:0.85rem;color:#94A3B8">Keep them suspended in a vacuum.</div>
        </div>
      </div>
      <div v-click style="display:flex; align-items:center; gap:1rem; background:rgba(255,255,255,0.05); padding:1rem; border-radius:16px; border-left:5px solid #EC4899">
        <div style="font-size:2rem">❄️</div>
        <div>
          <div style="font-size:1.1rem;font-weight:900;color:white">Absolute Zero</div>
          <div style="font-size:0.85rem;color:#94A3B8">Extreme cold to keep them still.</div>
        </div>
      </div>
    </div>
    <div v-click style="flex:0.7; background:#0F172A; border:2px solid #8B5CF6; border-radius:24px; padding:1.5rem; text-align:center">
      <div style="font-size:2.5rem" class="animate-pulse">🌀</div>
      <div style="font-size:0.9rem; color:#8B5CF6; font-weight:700; margin-top:0.8rem">Suspension Trap</div>
    </div>
  </div>
</div>

---
class: slide-dark
---
<!-- SLIDE 9: REAL WORLD APPLICATION -->
<div class="content-wrapper">
  <div class="pill">IN YOUR HOSPITAL</div>
  <div style="font-size:2.8rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 2rem;">The PET Scan</div>
  <div style="display:flex; gap:15px; width:100%">
    <div v-click class="glow-card" style="flex:1; border-bottom-color:#22D3EE">
      <div style="font-size:1.8rem;margin-bottom:0.5rem">💉</div>
      <div style="font-size:1rem;font-weight:900;color:white">Tracer</div>
      <div style="font-size:0.8rem;color:#94A3B8">Positrons are released inside you.</div>
    </div>
    <div v-click class="glow-card" style="flex:1; border-bottom-color:#8B5CF6">
      <div style="font-size:1.8rem;margin-bottom:0.5rem">💥</div>
      <div style="font-size:1rem;font-weight:900;color:white">Flash</div>
      <div style="font-size:0.8rem;color:#94A3B8">They hit electrons and release light.</div>
    </div>
    <div v-click class="glow-card" style="flex:1; border-bottom-color:#EC4899">
      <div style="font-size:1.8rem;margin-bottom:0.5rem">🩺</div>
      <div style="font-size:1rem;font-weight:900;color:white">Image</div>
      <div style="font-size:0.8rem;color:#94A3B8">Light is detected to map the body.</div>
    </div>
  </div>
</div>

---
class: slide-dark
---
<!-- SLIDE 10: THE CHALLENGE -->
<div class="content-wrapper items-center text-center">
  <div class="pill">THE FUTURE</div>
  <div style="font-size:3.2rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 0.8rem; line-height:1">Your Turn to Solve It.</div>
  <div style="font-size:1.3rem;color:#22D3EE;font-weight:900;margin-bottom:2rem">The Mirror Universe Awaits</div>
  <div style="display:flex; gap:20px; justify-content:center; width:100%">
    <div v-click class="glow-card" style="flex:1; border-left: 5px solid #8B5CF6; text-align:left">
      <div style="font-size:2.5rem;margin-bottom:0.8rem">🔭</div>
      <div style="font-size:1.1rem;font-weight:900;color:white">Discover</div>
      <div style="font-size:0.85rem;color:#94A3B8">Why did matter win?</div>
    </div>
    <div v-click class="glow-card" style="flex:1; border-left: 5px solid #22D3EE; text-align:left">
      <div style="font-size:2.5rem;margin-bottom:0.8rem">🧪</div>
      <div style="font-size:1.1rem;font-weight:900;color:white">Engineer</div>
      <div style="font-size:0.85rem;color:#94A3B8">Store it for space travel.</div>
    </div>
  </div>
</div>

---
