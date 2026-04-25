---
theme: seriph
background: '#FFFBEB'
highlighter: shiki
lineNumbers: false
transition: slide-left
class: style-workshop
---

<style>
@import './styles/workshop.css';
</style>

<!-- SLIDE 1: WORKSHOP COVER -->
<div class="content-wrapper">
  <div style="margin-top: 1.5rem; text-align: center; width: 100%">
    <div class="pill">PRACTICAL TRAINING · LAB 01</div>
    <div style="font-size:3.5rem;font-weight:900;color:#78350F;margin-bottom:1rem; border-bottom:5px solid #FCD34D; display:inline-block">
      Antimatter Handling
    </div>
    <div style="font-size:1.5rem;font-weight:700;color:#92400E;margin-bottom:3rem">
      Containment & Safety Procedures
    </div>
    <div style="background:white; border:2px dashed #D97706; padding:2rem; max-width:500px; margin: 0 auto; transform: rotate(1deg)">
      <div style="font-size:1.1rem; color:#451A03; font-weight:700">Today's Goal:</div>
      <div style="font-size:1.3rem; color:#D97706; font-weight:900">Stabilize 100 Antiprotons for 1 Hour</div>
    </div>
  </div>
</div>

---
class: style-workshop
---
<!-- SLIDE 2: THE PROCEDURE (TRAPPING) -->
<div class="content-wrapper">
  <div class="pill">PROCEDURE 01</div>
  <div style="font-size:2.8rem;font-weight:900;color:#78350F;margin-bottom: 2rem;">Loading the Penning Trap</div>
  <div style="display:flex; gap:2rem; align-items:center; width:100%">
    <div style="flex:1">
      <div v-click class="card" style="margin-bottom: 1.5rem">
        <div style="font-size:1.2rem; font-weight:900; color:#B45309">1. Decelerate:</div>
        <div style="font-size:1rem; color:#451A03">Tune AD magnets to reduce antiproton velocity to 10% light speed.</div>
      </div>
      <div v-click class="card">
        <div style="font-size:1.2rem; font-weight:900; color:#B45309">2. Capture:</div>
        <div style="font-size:1rem; color:#451A03">Pulse the electrostatic gate to lock particles in the center.</div>
      </div>
    </div>
    <div v-click class="activity-box" style="flex:0.8">
      <div style="font-size:1.2rem; font-weight:900; margin-bottom:0.5rem">🚧 DO NOT TOUCH</div>
      <div style="font-size:0.95rem">If particles touch the metal wall, annihilation will occur instantly. Check vacuum seals!</div>
    </div>
  </div>
</div>

---
class: style-workshop
---
<!-- SLIDE 3: SAFETY PROTOCOLS -->
<div class="content-wrapper">
  <div class="pill">SAFETY FIRST</div>
  <div style="font-size:2.8rem;font-weight:900;color:#78350F;margin-bottom: 2rem;">Hazard Management</div>
  <div style="display:flex; gap:20px; width:100%">
    <div v-click class="card" style="flex:1">
      <div style="font-size:1.2rem; font-weight:900; color:#B45309; margin-bottom:0.5rem">Gamma Radiation</div>
      <div style="font-size:0.9rem">511 keV photons are emitted during contact. Wear lead-lined aprons.</div>
    </div>
    <div v-click class="card" style="flex:1">
      <div style="font-size:1.2rem; font-weight:900; color:#B45309; margin-bottom:0.5rem">Magnetic Field</div>
      <div style="font-size:0.9rem">High Tesla fields. No watches, pacemakers, or steel tools near the trap.</div>
    </div>
    <div v-click class="card" style="flex:1">
      <div style="font-size:1.2rem; font-weight:900; color:#B45309; margin-bottom:0.5rem">Cryo-Failure</div>
      <div style="font-size:0.9rem">If cooling fails, dump the load into the annihilation target immediately.</div>
    </div>
  </div>
</div>

---
class: style-workshop
---
<!-- SLIDE 4: TROUBLESHOOTING -->
<div class="content-wrapper">
  <div class="pill">TROUBLESHOOTING</div>
  <div style="font-size:2.8rem;font-weight:900;color:#78350F;margin-bottom: 2rem;">Magnetic Drift Correction</div>
  <div style="display:flex; gap:3rem; align-items:center; width:100%">
    <div style="flex:1">
      <div v-click style="margin-bottom:1.5rem">
        <div style="font-size:1.3rem; font-weight:900; color:#78350F">The Symptom:</div>
        <div style="font-size:1rem; color:#451A03">Slow increase in gamma detector background noise.</div>
      </div>
      <div v-click style="background:#FEF3C7; padding:1.2rem; border-radius:8px; border:1px solid #F59E0B">
        <div style="font-size:1.1rem; font-weight:900; color:#D97706">The Fix:</div>
        <div style="font-size:0.95rem">Recalibrate the Z-axis electrodes to center the particle cloud.</div>
      </div>
    </div>
    <div v-click style="flex:0.8; text-align:center">
      <div style="font-size:5rem">🌀</div>
      <div style="font-size:1.1rem; color:#D97706; font-weight:700">Drift Check: Every 15 Mins</div>
    </div>
  </div>
</div>

---
class: style-workshop
---
<!-- SLIDE 5: FINAL EXERCISE -->
<div class="content-wrapper items-center text-center">
  <div class="pill">HOMEWORK</div>
  <div style="font-size:3.5rem;font-weight:900;color:#78350F;margin-bottom: 1rem; line-height:1">Design Your Containment Cycle</div>
  <div style="font-size:1.4rem;color:#D97706;font-weight:700;margin-bottom:3rem">Practical Exam: 100% Stability Goal</div>
  <div style="max-width:600px; text-align:left; background:white; border:2px dashed #D97706; padding:2rem">
    <div v-click style="margin-bottom:1rem; display:flex; align-items:center; gap:1rem">
      <div style="background:#FCD34D; width:12px; height:12px; border-radius:0px"></div>
      <div style="font-size:1rem; color:#451A03">Calculate the required Magnetic Field (Tesla) for 511 keV containment.</div>
    </div>
    <div v-click style="margin-bottom:1rem; display:flex; align-items:center; gap:1rem">
      <div style="background:#FCD34D; width:12px; height:12px; border-radius:0px"></div>
      <div style="font-size:1rem; color:#451A03">Draft an Emergency Dump plan for Cryo-Failure.</div>
    </div>
    <div v-click style="display:flex; align-items:center; gap:1rem">
      <div style="background:#FCD34D; width:12px; height:12px; border-radius:0px"></div>
      <div style="font-size:1rem; color:#451A03">Submit your Calibration Log to the Instructor.</div>
    </div>
  </div>
</div>

