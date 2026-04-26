---
title: "Global AI Summit — 100-Slide Stress Test"
transition: fade
canvasWidth: 900
---
<style>
.slidev-layout { overflow:hidden; padding: 0 !important; }
body, #app { background: #0a0a0f; }
.pill {
  display:inline-block; padding:5px 16px; border-radius:9999px;
  font-size:10px; font-weight:900; letter-spacing:0.3em;
  text-transform:uppercase; color:white;
}
.content-wrapper {
  position:relative; z-index:10; height:100%;
  display:flex; flex-direction:column;
}
.dot { position:absolute; border-radius:50%; pointer-events:none; z-index:0; }
.stat-block {
  background:rgba(255,255,255,0.07); border-radius:16px;
  padding:1.2rem 1.5rem; border-top:4px solid currentColor;
}
</style>

<div style="position:relative;width:100%;height:100%;background:#03001a;padding:3.5rem;overflow:hidden;">
  <div class="dot" style="width:500px;height:500px;top:-150px;right:-150px;background:#6366F1;opacity:0.18;border-radius:50%;"></div>
  <div class="dot" style="width:300px;height:300px;bottom:-80px;left:-80px;background:#22D3EE;opacity:0.12;border-radius:50%;"></div>
  <div class="content-wrapper justify-center">
    <div>
      <span class="pill" style="background:#6366F1;color:white;">GLOBAL AI SUMMIT · STRESS TEST</span>
      <div style="font-size:5.5rem;font-weight:900;color:white;line-height:1;letter-spacing:-0.05em;margin-top:1rem;">AI at</div>
      <div style="font-size:5.5rem;font-weight:900;color:#22D3EE;line-height:1;letter-spacing:-0.05em;margin-bottom:1.5rem;">Scale.</div>
      <div style="color:#94A3B8;font-size:1.1rem;font-weight:600;">100 Slides · 5 Modules · Full Engine Stress Test</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#03001a;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#6366F1;color:white;margin-bottom:1.2rem;">TODAY'S AGENDA</span>
    <div style="font-size:2.5rem;font-weight:900;color:white;margin-bottom:1.5rem;">5 Modules. 100 Slides.</div>
    <div style="display:flex;flex-direction:column;gap:0.6rem;">
      <div v-click style="display:flex;align-items:center;gap:1.2rem;background:rgba(255,255,255,0.04);border-radius:12px;padding:0.8rem 1.2rem;border-left:4px solid #22D3EE;">
        <div style="font-size:1.8rem;font-weight:900;color:#22D3EE;font-family:monospace;">01</div>
        <div style="font-size:1.1rem;font-weight:700;color:white;">The AI Revolution</div>
      </div>
      <div v-click style="display:flex;align-items:center;gap:1.2rem;background:rgba(255,255,255,0.04);border-radius:12px;padding:0.8rem 1.2rem;border-left:4px solid #F97316;">
        <div style="font-size:1.8rem;font-weight:900;color:#F97316;font-family:monospace;">02</div>
        <div style="font-size:1.1rem;font-weight:700;color:white;">Business Impact</div>
      </div>
      <div v-click style="display:flex;align-items:center;gap:1.2rem;background:rgba(255,255,255,0.04);border-radius:12px;padding:0.8rem 1.2rem;border-left:4px solid #22C55E;">
        <div style="font-size:1.8rem;font-weight:900;color:#22C55E;font-family:monospace;">03</div>
        <div style="font-size:1.1rem;font-weight:700;color:white;">Technical Architecture</div>
      </div>
      <div v-click style="display:flex;align-items:center;gap:1.2rem;background:rgba(255,255,255,0.04);border-radius:12px;padding:0.8rem 1.2rem;border-left:4px solid #86EFAC;">
        <div style="font-size:1.8rem;font-weight:900;color:#86EFAC;font-family:monospace;">04</div>
        <div style="font-size:1.1rem;font-weight:700;color:white;">Sustainability & Ethics</div>
      </div>
      <div v-click style="display:flex;align-items:center;gap:1.2rem;background:rgba(255,255,255,0.04);border-radius:12px;padding:0.8rem 1.2rem;border-left:4px solid #D4AF37;">
        <div style="font-size:1.8rem;font-weight:900;color:#D4AF37;font-family:monospace;">05</div>
        <div style="font-size:1.1rem;font-weight:700;color:white;">The Future Roadmap</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#03001a;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#A78BFA;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#A78BFA;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">AI is the new electricity.</div>
    <div v-click style="font-size:1rem;color:#A78BFA;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Andrew Ng</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="dot" style="width:450px;height:450px;top:-150px;right:-150px;background:#22D3EE;opacity:0.12;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;">MODULE 1</span>
    <div style="font-size:4rem;font-weight:900;color:white;line-height:1.1;letter-spacing:-0.04em;margin-top:1rem;">The AI Revolution</div>
    <div style="font-size:1.2rem;color:#22D3EE;margin-top:1rem;font-weight:600;">🔬 Deep dive begins now.</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#22D3EE;line-height:1;letter-spacing:-0.05em;">40%</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Reduction in energy via AI optimization</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">RAG Systems vs Multi-Modal AI</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22D3EE;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">📊</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">RAG Systems</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22D3EE;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">💎</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Multi-Modal AI</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Vector Databases</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22D3EE;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🛰️</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Edge Computing</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22D3EE;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🌱</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Zero-Shot Learning</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22D3EE;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🏗️</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Prompt Engineering</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#22D3EE;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#22D3EE;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">AI will be the defining technology of the 21st century.</div>
    <div v-click style="font-size:1rem;color:#22D3EE;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Sundar Pichai</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Zero-Shot Learning</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">🎯 Quick Poll</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#22D3EE;font-weight:700;">Raise your hand if you've used AI in the last 24 hours.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#22D3EE;line-height:1;letter-spacing:-0.05em;">72%</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Of execs say AI is a top-3 priority</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Robotics vs Quantum ML</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22D3EE;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🤖</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Robotics</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22D3EE;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🏆</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Quantum ML</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Multi-Modal AI</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22D3EE;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">📡</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Safety Frameworks</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22D3EE;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🧬</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Carbon Footprint</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22D3EE;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">⚙️</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">AI Governance</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#22D3EE;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#22D3EE;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">We're at the iPhone moment for AI.</div>
    <div v-click style="font-size:1rem;color:#22D3EE;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Sam Altman</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Carbon Footprint</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">💬 Think-Pair-Share</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#22D3EE;font-weight:700;">What industry will AI disrupt most in the next 5 years?</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#22D3EE;line-height:1;letter-spacing:-0.05em;">60%</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Drop in ML model training costs since 2020</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Data Pipelines vs Vector Databases</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22D3EE;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🚀</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Data Pipelines</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22D3EE;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">💡</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Vector Databases</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Autonomous Agents</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22D3EE;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🧠</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Supply Chain AI</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22D3EE;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">⚡</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Predictive Analytics</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22D3EE;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🌍</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">NLP Breakthroughs</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#22D3EE;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#22D3EE;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">AI is the new electricity.</div>
    <div v-click style="font-size:1rem;color:#22D3EE;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Andrew Ng</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Predictive Analytics</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22D3EE;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0B0C2A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#22D3EE;color:#0B0C2A;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">🧠 Kahoot Round</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#22D3EE;font-weight:700;">Test your knowledge — open Kahoot on your device.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="dot" style="width:450px;height:450px;top:-150px;right:-150px;background:#F97316;opacity:0.12;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;">
    <span class="pill" style="background:#F97316;color:#ffffff;">MODULE 2</span>
    <div style="font-size:4rem;font-weight:900;color:white;line-height:1.1;letter-spacing:-0.04em;margin-top:1rem;">Business Impact</div>
    <div style="font-size:1.2rem;color:#F97316;margin-top:1rem;font-weight:600;">💡 Deep dive begins now.</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#F97316;line-height:1;letter-spacing:-0.05em;">500B</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Parameters in the largest LLMs today</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Supply Chain AI vs Predictive Analytics</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #F97316;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🛰️</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Supply Chain AI</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #F97316;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🤖</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Predictive Analytics</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Federated Learning</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #F97316;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🌱</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">On-Device AI</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #F97316;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🏗️</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">AI in Healthcare</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #F97316;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🔐</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">AI in Education</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#F97316;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#F97316;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">Every company will be an AI company.</div>
    <div v-click style="font-size:1rem;color:#F97316;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Jensen Huang</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">AI in Healthcare</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">🗳️ Live Vote</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#F97316;font-weight:700;">Which AI risk concerns you most? Cast your vote now.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#F97316;line-height:1;letter-spacing:-0.05em;">$4.4T</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Annual value AI could add to business</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Transformers vs Embeddings</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #F97316;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">📡</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Transformers</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #F97316;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🚀</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Embeddings</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Transformers</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #F97316;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🧬</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Embeddings</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #F97316;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">⚙️</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Inference Speed</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #F97316;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🌐</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Model Alignment</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#F97316;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#F97316;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">AI will be the defining technology of the 21st century.</div>
    <div v-click style="font-size:1rem;color:#F97316;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Sundar Pichai</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Inference Speed</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">🎯 Quick Poll</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#F97316;font-weight:700;">Raise your hand if you've used AI in the last 24 hours.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#F97316;line-height:1;letter-spacing:-0.05em;">10×</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Faster drug discovery with AI models</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Safety Frameworks vs Carbon Footprint</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #F97316;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🧠</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Safety Frameworks</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #F97316;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">📊</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Carbon Footprint</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Edge Computing</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #F97316;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">⚡</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Zero-Shot Learning</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #F97316;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🌍</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Prompt Engineering</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #F97316;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🔬</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Fine-Tuning</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#F97316;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#F97316;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">We're at the iPhone moment for AI.</div>
    <div v-click style="font-size:1rem;color:#F97316;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Sam Altman</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Prompt Engineering</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#F97316;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0F172A;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#F97316;color:#ffffff;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">💬 Think-Pair-Share</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#F97316;font-weight:700;">What industry will AI disrupt most in the next 5 years?</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="dot" style="width:450px;height:450px;top:-150px;right:-150px;background:#22C55E;opacity:0.12;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;">
    <span class="pill" style="background:#22C55E;color:#050d05;">MODULE 3</span>
    <div style="font-size:4rem;font-weight:900;color:white;line-height:1.1;letter-spacing:-0.04em;margin-top:1rem;">Technical Architecture</div>
    <div style="font-size:1.2rem;color:#22C55E;margin-top:1rem;font-weight:600;">📊 Deep dive begins now.</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#22C55E;line-height:1;letter-spacing:-0.05em;">3.5×</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Productivity gain with AI assistance</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">AI in Healthcare vs AI in Education</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22C55E;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🌱</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">AI in Healthcare</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22C55E;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">📡</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">AI in Education</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Carbon Footprint</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22C55E;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🏗️</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">AI Governance</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22C55E;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🔐</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Bias Detection</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22C55E;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">💎</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Synthetic Data</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#22C55E;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#22C55E;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">The question is not whether AI will change the world, but how fast.</div>
    <div v-click style="font-size:1rem;color:#22C55E;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Demis Hassabis</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Bias Detection</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">✍️ 60-Second Write</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#22C55E;font-weight:700;">Name 3 AI tools you use without thinking about it.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#22C55E;line-height:1;letter-spacing:-0.05em;">40%</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Reduction in energy via AI optimization</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Prompt Engineering vs Fine-Tuning</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22C55E;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🧬</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Prompt Engineering</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22C55E;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🧠</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Fine-Tuning</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Predictive Analytics</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22C55E;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">⚙️</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">NLP Breakthroughs</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22C55E;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🌐</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Computer Vision</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22C55E;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🏆</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Robotics</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#22C55E;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#22C55E;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">Every company will be an AI company.</div>
    <div v-click style="font-size:1rem;color:#22C55E;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Jensen Huang</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Computer Vision</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">🗳️ Live Vote</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#22C55E;font-weight:700;">Which AI risk concerns you most? Cast your vote now.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#22C55E;line-height:1;letter-spacing:-0.05em;">72%</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Of execs say AI is a top-3 priority</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">NLP Breakthroughs vs Computer Vision</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22C55E;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">⚡</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">NLP Breakthroughs</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #22C55E;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🛰️</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Computer Vision</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">On-Device AI</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22C55E;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🌍</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">AI in Healthcare</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22C55E;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🔬</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">AI in Education</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #22C55E;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">💡</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Attention Mechanisms</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#22C55E;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#22C55E;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">AI will be the defining technology of the 21st century.</div>
    <div v-click style="font-size:1rem;color:#22C55E;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Sundar Pichai</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">AI in Education</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#22C55E;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#050d05;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#22C55E;color:#050d05;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">🎯 Quick Poll</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#22C55E;font-weight:700;">Raise your hand if you've used AI in the last 24 hours.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="dot" style="width:450px;height:450px;top:-150px;right:-150px;background:#86EFAC;opacity:0.12;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;">MODULE 4</span>
    <div style="font-size:4rem;font-weight:900;color:white;line-height:1.1;letter-spacing:-0.04em;margin-top:1rem;">Sustainability & Ethics</div>
    <div style="font-size:1.2rem;color:#86EFAC;margin-top:1rem;font-weight:600;">🛰️ Deep dive begins now.</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#86EFAC;line-height:1;letter-spacing:-0.05em;">80%</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Enterprises using AI in some capacity</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Data Pipelines vs Vector Databases</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #86EFAC;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🏗️</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Data Pipelines</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #86EFAC;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🧬</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Vector Databases</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Inference Speed</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #86EFAC;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🔐</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Model Alignment</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #86EFAC;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">💎</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Data Pipelines</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #86EFAC;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🤖</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Vector Databases</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#86EFAC;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#86EFAC;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">AI is the new electricity.</div>
    <div v-click style="font-size:1rem;color:#86EFAC;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Andrew Ng</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Data Pipelines</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">🧠 Kahoot Round</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#86EFAC;font-weight:700;">Test your knowledge — open Kahoot on your device.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#86EFAC;line-height:1;letter-spacing:-0.05em;">500B</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Parameters in the largest LLMs today</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Synthetic Data vs Autonomous Agents</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #86EFAC;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">⚙️</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Synthetic Data</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #86EFAC;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">⚡</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Autonomous Agents</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Prompt Engineering</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #86EFAC;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🌐</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Fine-Tuning</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #86EFAC;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🏆</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">RAG Systems</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #86EFAC;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🚀</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Multi-Modal AI</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#86EFAC;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#86EFAC;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">The question is not whether AI will change the world, but how fast.</div>
    <div v-click style="font-size:1rem;color:#86EFAC;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Demis Hassabis</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">RAG Systems</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">✍️ 60-Second Write</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#86EFAC;font-weight:700;">Name 3 AI tools you use without thinking about it.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#86EFAC;line-height:1;letter-spacing:-0.05em;">$4.4T</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Annual value AI could add to business</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Attention Mechanisms vs Neural Networks</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #86EFAC;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🌍</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Attention Mechanisms</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #86EFAC;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🌱</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Neural Networks</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">AI Governance</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #86EFAC;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🔬</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Bias Detection</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #86EFAC;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">💡</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Synthetic Data</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #86EFAC;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">📊</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Autonomous Agents</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#86EFAC;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#86EFAC;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">Every company will be an AI company.</div>
    <div v-click style="font-size:1rem;color:#86EFAC;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Jensen Huang</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Synthetic Data</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#86EFAC;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0d1f12;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#86EFAC;color:#0d1f12;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">🗳️ Live Vote</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#86EFAC;font-weight:700;">Which AI risk concerns you most? Cast your vote now.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="dot" style="width:450px;height:450px;top:-150px;right:-150px;background:#D4AF37;opacity:0.12;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;">
    <span class="pill" style="background:#D4AF37;color:#0a0508;">MODULE 5</span>
    <div style="font-size:4rem;font-weight:900;color:white;line-height:1.1;letter-spacing:-0.04em;margin-top:1rem;">The Future Roadmap</div>
    <div style="font-size:1.2rem;color:#D4AF37;margin-top:1rem;font-weight:600;">🌱 Deep dive begins now.</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#D4AF37;line-height:1;letter-spacing:-0.05em;">97M</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">New AI-related jobs created by 2025</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Safety Frameworks vs Carbon Footprint</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #D4AF37;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🔐</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Safety Frameworks</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #D4AF37;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">⚙️</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Carbon Footprint</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Computer Vision</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #D4AF37;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">💎</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Robotics</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #D4AF37;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🤖</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Quantum ML</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #D4AF37;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">📡</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Federated Learning</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#D4AF37;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#D4AF37;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">We're at the iPhone moment for AI.</div>
    <div v-click style="font-size:1rem;color:#D4AF37;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Sam Altman</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Quantum ML</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">💬 Think-Pair-Share</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#D4AF37;font-weight:700;">What industry will AI disrupt most in the next 5 years?</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#D4AF37;line-height:1;letter-spacing:-0.05em;">3.5×</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Productivity gain with AI assistance</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Federated Learning vs On-Device AI</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #D4AF37;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🌐</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Federated Learning</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #D4AF37;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🌍</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">On-Device AI</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">AI in Education</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #D4AF37;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🏆</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Attention Mechanisms</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #D4AF37;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🚀</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Neural Networks</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #D4AF37;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🧠</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Transformers</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#D4AF37;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#D4AF37;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">AI is the new electricity.</div>
    <div v-click style="font-size:1rem;color:#D4AF37;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Andrew Ng</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Neural Networks</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">🧠 Kahoot Round</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#D4AF37;font-weight:700;">Test your knowledge — open Kahoot on your device.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:#D4AF37;line-height:1;letter-spacing:-0.05em;">40%</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">Reduction in energy via AI optimization</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Edge Computing vs Zero-Shot Learning</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #D4AF37;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🔬</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Edge Computing</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid #D4AF37;">
        <div style="font-size:2rem;margin-bottom:0.8rem;">🏗️</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">Zero-Shot Learning</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Model Alignment</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #D4AF37;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">💡</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Data Pipelines</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #D4AF37;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">📊</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Vector Databases</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid #D4AF37;">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🛰️</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">Edge Computing</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:#D4AF37;opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:#D4AF37;margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">The question is not whether AI will change the world, but how fast.</div>
    <div v-click style="font-size:1rem;color:#D4AF37;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— Demis Hassabis</div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Vector Databases</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">✍️ 60-Second Write</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:#D4AF37;font-weight:700;">Name 3 AI tools you use without thinking about it.</div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#0a0508;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#D4AF37;color:#0a0508;margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">Edge Computing</div>
    <div style="flex:1;">
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">01</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Scalable infrastructure enabling real-time inference at the network edge</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">02</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Self-supervised learning reducing labeled data requirements by 10×</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">03</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Constitutional AI frameworks ensuring model safety and alignment</div>
      </div>
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:#D4AF37;font-family:monospace;min-width:32px;">04</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">Multimodal pipelines unifying vision, audio, and language understanding</div>
      </div>
    </div>
  </div>
</div>

---

<div style="position:relative;width:100%;height:100%;background:#03001a;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="dot" style="width:500px;height:500px;top:-200px;right:-200px;background:#6366F1;opacity:0.15;border-radius:50%;"></div>
  <div class="dot" style="width:400px;height:400px;bottom:-150px;left:-150px;background:#22D3EE;opacity:0.10;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;">
    <span class="pill" style="background:#6366F1;color:white;">STRESS TEST COMPLETE</span>
    <div style="font-size:5rem;font-weight:900;color:white;line-height:1;letter-spacing:-0.05em;margin:1rem 0;">100 Slides.</div>
    <div style="font-size:5rem;font-weight:900;color:#22D3EE;line-height:1;letter-spacing:-0.05em;margin-bottom:1.5rem;">Engine Holds.</div>
    <div v-click style="font-size:1.2rem;color:#94A3B8;font-weight:600;">All archetypes · All layouts · All components — verified at scale.</div>
  </div>
</div>