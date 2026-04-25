---
theme: seriph
background: '#1A1F5E'
highlighter: shiki
lineNumbers: false
transition: fade
title: AI — Your New Superpower
canvasWidth: 900
---

<style>
.slidev-layout { 
  overflow:hidden; 
  font-family:'Inter',sans-serif; 
  padding: 0 !important; 
}

/* Large bleed circles via pseudo-elements */
.slide-cover::before {
  content:""; position:absolute; border-radius:50%;
  width:490px; height:490px; top:-130px; right:-130px;
  background:#2D3A8C; z-index:0; pointer-events:none;
}
.slide-cover::after {
  content:""; position:absolute; border-radius:50%;
  width:310px; height:310px; bottom:-80px; left:-80px;
  background:#2D3A8C; z-index:0; pointer-events:none;
}
.slide-journey::before {
  content:""; position:absolute; border-radius:50%;
  width:300px; height:300px; top:-100px; right:-100px;
  background:rgba(26,31,94,0.03); z-index:0; pointer-events:none;
}
.slide-hook::before {
  content:""; position:absolute; border-radius:50%;
  width:500px; height:500px; top:-150px; right:-150px;
  background:#FF8C5A; z-index:0; pointer-events:none;
}
.slide-hook::after {
  content:""; position:absolute; border-radius:50%;
  width:280px; height:280px; bottom:-80px; left:-80px;
  background:#E05A20; z-index:0; pointer-events:none;
}
.slide-demo::before {
  content:""; position:absolute; border-radius:50%;
  width:420px; height:420px; top:-120px; right:-120px;
  background:#1E2761; z-index:0; pointer-events:none;
}
.slide-mod1::before {
  content:""; position:absolute; border-radius:50%;
  width:400px; height:400px; top:-100px; right:-100px;
  background:#2D3A8C; z-index:0; pointer-events:none;
}
.slide-mod1::after {
  content:""; position:absolute; border-radius:50%;
  width:250px; height:250px; bottom:-80px; left:-80px;
  background:#06D6A0; opacity:0.15; z-index:0; pointer-events:none;
}
.slide-light::before {
  content:""; position:absolute; border-radius:50%;
  width:350px; height:350px; top:-100px; left:-100px;
  background:rgba(26,31,94,0.03); z-index:0; pointer-events:none;
}
.slide-pattern::before {
  content:""; position:absolute; border-radius:50%;
  width:450px; height:450px; bottom:-150px; right:-150px;
  background:#059669; z-index:0; pointer-events:none;
}
.slide-data::after {
  content:""; position:absolute; border-radius:50%;
  width:300px; height:300px; top:-50px; left:-50px;
  background:#E05A20; z-index:0; pointer-events:none;
}
.slide-mod2::before {
  content:""; position:absolute; border-radius:50%;
  width:500px; height:500px; top:-200px; right:-200px;
  background:#047857; z-index:0; pointer-events:none;
}
/* Small accent dots */
.dot { position:absolute; border-radius:50%; pointer-events:none; z-index:0; }

/* Content wrapper to stay above background graphics */
.content-wrapper {
  position:relative; z-index:10; height:100%; display:flex; flex-direction:column;
}

/* Orange footer bar */
.footer-bar {
  position:absolute; bottom:0; left:0; right:0; height:47px;
  background:#FF6B35; display:flex; align-items:center; justify-content:center;
  font-size:14px; font-weight:800; letter-spacing:0.18em; color:white; z-index:20;
}
/* Pill label */
.pill {
  display:inline-block; background:#FF6B35; color:white;
  font-size:11px; font-weight:900; letter-spacing:0.35em;
  padding:6px 18px; border-radius:9999px; text-transform:uppercase;
}
.pill-ghost {
  display:inline-block; background:rgba(255,255,255,0.2); color:white;
  font-size:11px; font-weight:900; letter-spacing:0.35em;
  padding:6px 18px; border-radius:9999px; text-transform:uppercase;
}
.pill-teal {
  display:inline-block; background:#06D6A0; color:#064e3b;
  font-size:11px; font-weight:900; letter-spacing:0.35em;
  padding:6px 18px; border-radius:9999px; text-transform:uppercase;
}
</style>

<!-- SLIDE 1: COVER -->
<div class="slide-cover" style="position:relative;width:100%;height:100%;background:#1A1F5E; padding: 3rem;">
  <div class="dot" style="width:220px;height:220px;bottom:70px;right:30px;background:#FF6B35"></div>
  <div class="dot" style="width:13px;height:13px;top:80px;left:160px;background:#06D6A0"></div>
  <div class="dot" style="width:19px;height:19px;top:140px;right:310px;background:#FFD166"></div>
  <div class="dot" style="width:9px;height:9px;bottom:120px;left:230px;background:#FF6B35"></div>
  <div class="dot" style="width:11px;height:11px;top:230px;left:90px;background:#FFD166"></div>
  <div class="content-wrapper justify-center pb-12">
    <div>
      <div class="pill">CLASS 6 &amp; 7 · AI SEMINAR</div>
      <div style="font-size:5rem;font-weight:900;color:white;line-height:1;letter-spacing:-0.04em">AI:</div>
      <div style="font-size:3.5rem;font-weight:900;color:#FFD166;line-height:1.15;letter-spacing:-0.03em; margin-bottom: 1.5rem;">Your New<br/>Superpower</div>
      <div style="color:#8B9FCE;font-style:italic;font-weight:700;font-size:1.1rem">3 Hours · 5 Chapters · 1 Superpower Unlocked</div>
    </div>
  </div>
  <div class="footer-bar">See it. Think about it. Wonder about it. Let's go.</div>
</div>

---

<!-- SLIDE 2: TODAY'S JOURNEY -->
<div class="slide-journey" style="position:relative;width:100%;height:100%;background:#F5F7FF; padding: 2.5rem;">
  <div class="content-wrapper">
    <div style="font-size:0.75rem;font-weight:900;letter-spacing:0.35em;color:#94A3B8;text-transform:uppercase;margin-bottom:0.5rem">Overview</div>
    <div style="font-size:2.5rem;font-weight:900;color:#1A1F5E;margin-bottom:2rem;letter-spacing:-0.02em">Today's Journey</div>
    <div style="display:flex; gap:10px; align-items:center; justify-content:space-between; margin-bottom: 1rem;">
      <div v-click style="width:140px; background:#FFF0E8;border-radius:16px;padding:12px;border-bottom:5px solid #FF6B35; z-index:10">
        <div style="font-size:2rem;line-height:1;margin-bottom:8px">⚡</div>
        <div style="font-size:0.6rem;font-weight:900;color:#FF6B35;letter-spacing:0.1em;text-transform:uppercase">0–15 min</div>
        <div style="font-size:1rem;font-weight:900;color:#1A1F5E;margin-top:2px">The Hook</div>
        <div style="font-size:0.7rem;color:#94A3B8;margin-top:2px">Magic Show</div>
      </div>
      <div v-click style="font-size:1.2rem;font-weight:900;color:#CBD5E1">→</div>
      <div v-click style="width:140px; background:#EEF2FF;border-radius:16px;padding:12px;border-bottom:5px solid #2D3A8C; z-index:10">
        <div style="font-size:2rem;line-height:1;margin-bottom:8px">🧠</div>
        <div style="font-size:0.6rem;font-weight:900;color:#2D3A8C;letter-spacing:0.1em;text-transform:uppercase">15–60 min</div>
        <div style="font-size:1rem;font-weight:900;color:#1A1F5E;margin-top:2px">Module 1</div>
        <div style="font-size:0.7rem;color:#94A3B8;margin-top:2px">How AI Learns</div>
      </div>
      <div v-click style="font-size:1.2rem;font-weight:900;color:#CBD5E1">→</div>
      <div v-click style="width:140px; background:#ECFDF5;border-radius:16px;padding:12px;border-bottom:5px solid #06D6A0; z-index:10">
        <div style="font-size:2rem;line-height:1;margin-bottom:8px">🌍</div>
        <div style="font-size:0.6rem;font-weight:900;color:#059669;letter-spacing:0.1em;text-transform:uppercase">70–115 min</div>
        <div style="font-size:1rem;font-weight:900;color:#1A1F5E;margin-top:2px">Module 2</div>
        <div style="font-size:0.7rem;color:#94A3B8;margin-top:2px">AI Around You</div>
      </div>
    </div>
    <div style="display:flex; gap:10px; align-items:center; justify-content:flex-start; margin-bottom: 2rem;">
      <div v-click style="width:140px; background:#FFFBEB;border-radius:16px;padding:12px;border-bottom:5px solid #F59E0B; z-index:10">
        <div style="font-size:2rem;line-height:1;margin-bottom:8px">✏️</div>
        <div style="font-size:0.6rem;font-weight:900;color:#92400E;letter-spacing:0.1em;text-transform:uppercase">115–160 min</div>
        <div style="font-size:1rem;font-weight:900;color:#1A1F5E;margin-top:2px">Module 3</div>
        <div style="font-size:0.7rem;color:#94A3B8;margin-top:2px">Be the Algorithm</div>
      </div>
      <div style="font-size:1.2rem;font-weight:900;color:#CBD5E1; margin:0 22px;">→</div>
      <div v-click style="width:140px; background:#FEF2F2;border-radius:16px;padding:12px;border-bottom:5px solid #EF4444; z-index:10">
        <div style="font-size:2rem;line-height:1;margin-bottom:8px">🏫</div>
        <div style="font-size:0.6rem;font-weight:900;color:#EF4444;letter-spacing:0.1em;text-transform:uppercase">170–180 min</div>
        <div style="font-size:1rem;font-weight:900;color:#1A1F5E;margin-top:2px">Finale</div>
        <div style="font-size:0.7rem;color:#94A3B8;margin-top:2px">Dream School 2047</div>
      </div>
    </div>
    <div v-click style="background:#1A1F5E;color:white;border-radius:12px;padding:14px 20px;font-size:1rem;font-weight:900;text-align:center; max-width:800px; z-index:10">
      Call &amp; Response → "Superpower activate?" → YOU say: "ACTIVATE! 🚀"
    </div>
  </div>
</div>

---

<!-- SLIDE 3: THE HOOK -->
<div class="slide-hook" style="position:relative;width:100%;height:100%;background:#FF6B35; padding: 3rem;">
  <div class="dot" style="width:13px;height:13px;top:60px;left:140px;background:#FFD166"></div>
  <div class="dot" style="width:9px;height:9px;top:180px;right:200px;background:#CC4A10"></div>
  <div class="content-wrapper justify-center">
    <div>
      <div class="pill-ghost">0 – 15 MINUTES</div>
      <div style="font-size:4rem;line-height:1;margin-bottom:1rem">⚡</div>
      <div style="font-size:4.5rem;font-weight:900;color:white;line-height:1.05;letter-spacing:-0.04em; margin-bottom:2rem;">The Magic<br/>Show Begins</div>
      <div v-click style="font-size:1.8rem;font-weight:900;color:#FFD166">Haath uthao — magic dekho.</div>
    </div>
  </div>
</div>

---

<!-- SLIDE 4: DEMO 01 -->
<div class="slide-demo" style="position:relative;width:100%;height:100%;background:#12173A; padding: 3rem;">
  <div class="dot" style="width:180px;height:180px;bottom:40px;left:-40px;background:#FF6B35;opacity:0.35;border-radius:50%"></div>
  <div class="dot" style="width:10px;height:10px;top:70px;left:150px;background:#FFD166"></div>
  <div class="dot" style="width:8px;height:8px;top:200px;right:220px;background:#06D6A0"></div>
  <div class="content-wrapper">
    <div>
      <div class="pill">DEMO 01 · LIVE</div>
      <div style="font-size:3.5rem;font-weight:900;color:white;line-height:1.05;letter-spacing:-0.03em; margin-bottom: 0.5rem;">Shout any 3 words.</div>
      <div style="font-size:2.8rem;font-weight:900;color:#FFD166;letter-spacing:-0.02em; margin-bottom: 2.5rem;">Watch AI make a painting.</div>
      <div v-click style="background:#1E2761;border-radius:16px;padding:14px 24px;display:inline-flex;align-items:center;gap:14px; margin-bottom: 1.5rem;">
        <span style="font-size:1.8rem">🎨</span>
        <span style="font-size:1.4rem;font-weight:900;color:#E2E8FF">Open Bing Image Creator</span>
      </div>
      <div v-click style="font-size:1.4rem;font-style:italic;color:#94A3B8;font-weight:700">Did the computer draw this? Or did it think?</div>
    </div>
  </div>
</div>

---

<!-- SLIDE 5: DEMO 02 -->
<div class="slide-demo" style="position:relative;width:100%;height:100%;background:#12173A; padding: 3rem;">
  <div class="dot" style="width:180px;height:180px;bottom:40px;left:-40px;background:#06D6A0;opacity:0.2;border-radius:50%"></div>
  <div class="dot" style="width:10px;height:10px;top:70px;left:150px;background:#FFD166"></div>
  <div class="dot" style="width:8px;height:8px;bottom:120px;right:180px;background:#06D6A0"></div>
  <div class="content-wrapper">
    <div>
      <div class="pill-teal">DEMO 02 · LIVE</div>
      <div style="font-size:4.5rem;font-weight:900;line-height:1.05;letter-spacing:-0.04em; margin-bottom: 1.5rem;">
        <span style="color:white">Real voice</span><br/>
        <span style="color:#06D6A0">or AI?</span>
      </div>
      <div style="font-size:2rem;font-weight:900;color:#FFD166; margin-bottom: 1.5rem;">🎧  Listen carefully.</div>
      <div v-click style="background:#1E2761;border-radius:16px;padding:14px 24px;display:inline-flex;align-items:center;gap:14px; margin-bottom: 2rem;">
        <span style="font-size:1.6rem">🎙</span>
        <span style="font-size:1.4rem;font-weight:900;color:#E2E8FF">Open ElevenLabs</span>
      </div>
      <div v-click style="font-size:1.2rem;font-weight:900;color:#06D6A0;border-left:4px solid #06D6A0;padding-left:18px">"Your voice has a fingerprint. AI just learned it in 10 seconds."</div>
    </div>
  </div>
</div>

---

<!-- SLIDE 6: MODULE 1 INTRO -->
<div class="slide-mod1" style="position:relative;width:100%;height:100%;background:#1A1F5E; padding: 3rem;">
  <div class="dot" style="width:12px;height:12px;top:70px;left:140px;background:#FFD166"></div>
  <div class="dot" style="width:18px;height:18px;bottom:100px;right:200px;background:#FF6B35"></div>
  <div class="content-wrapper justify-center items-center text-center">
    <div>
      <div class="pill-ghost" style="background:rgba(6,214,160,0.2); color:#06D6A0">15 – 60 MINUTES</div>
      <div style="font-size:5rem;line-height:1;margin-bottom:1rem">🧠</div>
      <div style="font-size:3.5rem;font-weight:900;color:white;line-height:1.1;letter-spacing:-0.03em; margin-bottom:1rem;">Module 1</div>
      <div style="font-size:4.5rem;font-weight:900;color:#06D6A0;line-height:1;letter-spacing:-0.04em;">How AI Learns</div>
    </div>
  </div>
</div>

---

<!-- SLIDE 7: OLD WAY VS NEW WAY -->
<div class="slide-light" style="position:relative;width:100%;height:100%;background:#F5F7FF; padding: 2rem;">
  <div class="dot" style="width:14px;height:14px;top:40px;right:100px;background:#FF6B35"></div>
  <div class="content-wrapper">
    <div class="pill" style="background:#1A1F5E; margin-bottom: 1rem;">THE BIG SHIFT</div>
    <div style="font-size:2.5rem;font-weight:900;color:#1A1F5E;letter-spacing:-0.03em; margin-bottom: 1.5rem;">Rules vs. Examples</div>
    <div style="display:flex; gap:15px; align-items: stretch;">
      <div v-click style="flex:1; background:white; border-radius:20px; padding:1.5rem; box-shadow:0 10px 30px rgba(0,0,0,0.05); border-top:6px solid #94A3B8">
        <div style="font-size:2rem;margin-bottom:0.5rem">⌨️</div>
        <div style="font-size:1.2rem;font-weight:900;color:#1A1F5E;margin-bottom:0.2rem">The Old Way</div>
        <div style="font-size:0.9rem;color:#64748B;margin-bottom:1rem">Humans write the rules.</div>
        <div style="background:#F1F5F9; border-radius:10px; padding:0.8rem; font-family:monospace; font-size:0.75rem; color:#475569; line-height: 1.4">
          if (has_fur &amp;&amp; barks) {<br/>
          &nbsp;&nbsp;return "Dog";<br/>
          } else {<br/>
          &nbsp;&nbsp;return "Unknown";<br/>
          }
        </div>
      </div>
      <div v-click style="display:flex;align-items:center;font-size:1.5rem;color:#CBD5E1">VS</div>
      <div v-click style="flex:1; background:white; border-radius:20px; padding:1.5rem; box-shadow:0 10px 30px rgba(0,0,0,0.05); border-top:6px solid #06D6A0">
        <div style="font-size:2rem;margin-bottom:0.5rem">🧠</div>
        <div style="font-size:1.2rem;font-weight:900;color:#1A1F5E;margin-bottom:0.2rem">The AI Way</div>
        <div style="font-size:0.9rem;color:#64748B;margin-bottom:1rem">Humans show examples.</div>
        <div style="display:flex; flex-wrap:wrap; gap:6px">
          <div style="width:36px;height:36px;background:#D1FAE5;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem">🐶</div>
          <div style="width:36px;height:36px;background:#D1FAE5;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem">🐶</div>
          <div style="width:36px;height:36px;background:#D1FAE5;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem">🐶</div>
          <div style="width:36px;height:36px;background:#D1FAE5;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem">🐶</div>
          <div style="width:36px;height:36px;background:#D1FAE5;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem">🐶</div>
          <div style="width:36px;height:36px;background:#D1FAE5;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem">🐶</div>
          <div style="width:36px;height:36px;background:#D1FAE5;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem">🐶</div>
          <div style="width:36px;height:36px;background:#D1FAE5;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem">🐶</div>
        </div>
      </div>
    </div>
  </div>
</div>

---

<!-- SLIDE 8: SPOT THE PATTERN -->
<div class="slide-pattern" style="position:relative;width:100%;height:100%;background:#064E3B; padding: 2.5rem;">
  <div class="dot" style="width:16px;height:16px;top:60px;right:180px;background:#FFD166"></div>
  <div class="dot" style="width:10px;height:10px;bottom:120px;left:80px;background:#06D6A0"></div>
  <div class="content-wrapper">
    <div class="pill" style="background:#059669; margin-bottom: 1rem;">THE PATTERN HUNTER</div>
    <div style="font-size:3rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 0.2rem; line-height:1">Chihuahua</div>
    <div style="font-size:3rem;font-weight:900;color:#FFD166;letter-spacing:-0.03em; margin-bottom: 1.5rem; line-height:1">or Muffin?</div>
    <div v-click style="display:flex; justify-content:center; gap:15px; margin-bottom:1.5rem">
      <div style="width:80px;height:80px;background:white;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:2.5rem;box-shadow:0 10px 20px rgba(0,0,0,0.2)">🐶</div>
      <div style="width:80px;height:80px;background:white;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:2.5rem;box-shadow:0 10px 20px rgba(0,0,0,0.2)">🧁</div>
      <div style="width:80px;height:80px;background:white;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:2.5rem;box-shadow:0 10px 20px rgba(0,0,0,0.2)">🐶</div>
      <div style="width:80px;height:80px;background:white;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:2.5rem;box-shadow:0 10px 20px rgba(0,0,0,0.2)">🧁</div>
    </div>
    <div v-click style="background:#134E4A; border-radius:16px; padding:1.2rem; text-align:center; max-width:650px; margin:0 auto; border:2px solid #059669">
      <div style="font-size:1.3rem;font-weight:900;color:white; margin-bottom: 0.5rem;">AI doesn't "see" a dog.</div>
      <div style="font-size:1rem;color:#A7F3D0; line-height: 1.4">It sees pixels, edges, and colors. If it sees 10,000 photos, it learns the <strong style="color:#FFD166">pattern</strong>.</div>
    </div>
  </div>
</div>

---

<!-- SLIDE 9: DATA IS FOOD -->
<div class="slide-data" style="position:relative;width:100%;height:100%;background:#FF6B35; padding: 2.5rem;">
  <div class="dot" style="width:14px;height:14px;bottom:80px;right:140px;background:#FFD166"></div>
  <div class="content-wrapper items-center text-center">
    <div class="pill-ghost" style="background:rgba(26,31,94,0.2); margin-bottom: 1rem;">THE GOLDEN RULE</div>
    <div style="font-size:3.2rem;font-weight:900;color:white;letter-spacing:-0.03em; margin-bottom: 0.8rem; line-height:1.1">Data is <span style="color:#1A1F5E">Food</span><br/>for AI.</div>
    <div v-click style="font-size:1.6rem;font-weight:900;color:#FFD166; margin-bottom: 2rem;">Garbage In = Garbage Out</div>
    <div style="display:flex; gap:15px; align-items:center; justify-content:center">
      <div v-click style="background:white; border-radius:20px; padding:1.2rem; text-align:center; width:200px; box-shadow:0 10px 30px rgba(0,0,0,0.1)">
        <div style="font-size:2rem;margin-bottom:0.5rem">📸 📝 🗣️</div>
        <div style="font-size:1.1rem;font-weight:900;color:#1A1F5E">10,000 Examples</div>
      </div>
      <div v-click style="font-size:1.8rem;color:white;font-weight:900">→</div>
      <div v-click style="background:#1A1F5E; border-radius:20px; padding:1.2rem; text-align:center; width:200px; box-shadow:0 10px 30px rgba(0,0,0,0.1)">
        <div style="font-size:2rem;margin-bottom:0.5rem">🚀</div>
        <div style="font-size:1.1rem;font-weight:900;color:#06D6A0">Smart AI</div>
      </div>
    </div>
  </div>
</div>

---

<!-- SLIDE 10: MODULE 2 INTRO -->
<div class="slide-mod2" style="position:relative;width:100%;height:100%;background:#065F46; padding: 3rem;">
  <div class="dot" style="width:15px;height:15px;top:80px;left:180px;background:#FFD166"></div>
  <div class="dot" style="width:20px;height:20px;bottom:120px;right:220px;background:#06D6A0"></div>
  <div class="content-wrapper justify-center items-center text-center">
    <div>
      <div class="pill-ghost" style="background:rgba(255,209,102,0.2); color:#FFD166">70 – 115 MINUTES</div>
      <div style="font-size:5rem;line-height:1;margin-bottom:1rem">🌍</div>
      <div style="font-size:3.5rem;font-weight:900;color:white;line-height:1.1;letter-spacing:-0.03em; margin-bottom:1rem;">Module 2</div>
      <div style="font-size:4.5rem;font-weight:900;color:#FFD166;line-height:1;letter-spacing:-0.04em;">AI Around You</div>
      <div v-click style="font-size:1.5rem;color:#A7F3D0;font-weight:700;margin-top:2rem;font-style:italic">From smart kheti to Bollywood deepfakes.</div>
    </div>
  </div>
</div>

---
