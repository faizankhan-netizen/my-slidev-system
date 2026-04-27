---
layout: center
class: style-school variant-lined
style: |
  --slide-bg: #1A1F5E;
  --slide-text: #FFFFFF;
  --accent-primary: #0EA5E9;
  --accent-secondary: #EC4899;
  --accent-tertiary: #EAB308;
  --font-base: 'Outfit', 'Gochi Hand', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Gochi+Hand&display=swap&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="school-wrapper" style="display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;">
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}'><div class="pill">HISTORY</div></div>
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">THE KHILAFAH</h1>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;">A History Adventure for Young Explorers</div>
</div>

---
layout: center
class: style-school variant-grid
style: |
  --slide-bg: #FF6B35;
  --slide-text: #1A1A1A;
  --accent-primary: #0EA5E9;
  --accent-secondary: #EC4899;
  --accent-tertiary: #EAB308;
  --font-base: 'Outfit', 'Gochi Hand', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Gochi+Hand&display=swap&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="school-wrapper" style="display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;">
  <div style="font-size:5rem;color:var(--accent-primary);opacity:0.5;margin-bottom:-2rem;font-family:serif;">"</div>
  <div v-motion :initial="{opacity:0}" :enter="{opacity:1}" style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;font-size:2.5rem;font-weight:700;font-style:italic;line-height:1.3;max-width:80%;">The best of your leaders are those whom you love and who love you, who pray for you and you pray for them.</div>
  <div v-motion :initial="{opacity:0,y:10}" :enter="{opacity:1,y:0}" style="margin-top:2rem;font-size:1.2rem;font-weight:600;text-transform:uppercase;letter-spacing:2px;">— Prophet Muhammad (ﷺ)</div>
</div>

---
layout: default
class: style-school variant-dots
style: |
  --slide-bg: #12173A;
  --slide-text: #FFFFFF;
  --accent-primary: #0EA5E9;
  --accent-secondary: #EC4899;
  --accent-tertiary: #EAB308;
  --font-base: 'Outfit', 'Gochi Hand', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Gochi+Hand&display=swap&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="school-wrapper" style="display:flex;flex-direction:column;height:100%;">
  <div style="display:flex;width:100%;height:100%;gap:3rem;">
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
      <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}'><div class="pill">ERA OF LIGHT</div></div>
      <h1 v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}' style="font-size: 2.2rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">The Rashidun Caliphate</h1>
      <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">The 'Rightly Guided' era established the foundations of Shura (consultation) and absolute justice, spanning from the Arabian Peninsula to the Levant and beyond.</div>
    </div>
    <div v-motion :initial="{opacity:0,x:50}" :enter="{opacity:1,x:0}" style="flex:1.2;padding:1rem;"><img src='https://images.unsplash.com/photo-1542640244-7e672d6cef21?auto=format&fit=crop&w=1200&q=80' style='width:100%;height:100%;object-fit:cover;border-radius:12px;' /></div>
  </div>
</div>

---
layout: default
class: style-school variant-notebook
style: |
  --slide-bg: #ECFDF5;
  --slide-text: #1A1A1A;
  --accent-primary: #0EA5E9;
  --accent-secondary: #EC4899;
  --accent-tertiary: #EAB308;
  --font-base: 'Outfit', 'Gochi Hand', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Gochi+Hand&display=swap&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="school-wrapper" style="display:flex;flex-direction:column;height:100%;">
  <div class="pill">HISTORICAL TIMELINE</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">The Great Dynasties</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; "></div>
  <div style="margin-top:1rem;width:100%;"><div v-click style="display:flex;gap:1.5rem;align-items:flex-start;margin-bottom:1rem;"><div style="font-size:1.5rem;font-weight:900;color:var(--accent-primary);opacity:0.8;">01</div><div v-click class="card" style="padding:1rem;">Umayyad Era|Establishment of statehood and administration across three continents.</div></div><div v-click style="display:flex;gap:1.5rem;align-items:flex-start;margin-bottom:1rem;"><div style="font-size:1.5rem;font-weight:900;color:var(--accent-primary);opacity:0.8;">02</div><div v-click class="card" style="padding:1rem;">Abbasid Golden Age|The zenith of science, culture, and theology in Baghdad.</div></div><div v-click style="display:flex;gap:1.5rem;align-items:flex-start;margin-bottom:1rem;"><div style="font-size:1.5rem;font-weight:900;color:var(--accent-primary);opacity:0.8;">03</div><div v-click class="card" style="padding:1rem;">Ottoman Legacy|The final great Khilafah, bridging East and West for centuries.</div></div></div>
</div>

---
layout: default
class: style-school variant-lined
style: |
  --slide-bg: #FFFBEB;
  --slide-text: #1A1A1A;
  --accent-primary: #0EA5E9;
  --accent-secondary: #EC4899;
  --accent-tertiary: #EAB308;
  --font-base: 'Outfit', 'Gochi Hand', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Gochi+Hand&display=swap&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="school-wrapper" style="display:flex;flex-direction:column;height:100%;">
  <div class="pill">GOVERNANCE</div>
  <h1 style="font-size: 2.2rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">The Pillars of the State</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; max-width:60%;">Unlike secular models, the Khilafah is built upon the dual responsibility to the Creator and the creation.</div>
  <div v-click style="margin-top:auto;padding:1.5rem;background:color-mix(in srgb,var(--slide-text) 5%,transparent);border-left:4px solid var(--accent-primary);border-radius:8px;">
    <div style="font-size:2rem;margin-bottom:0.5rem;">⚖️</div>
    <div style="font-weight:700;">Justice, Shura, and Accountability</div>
  </div>
</div>

---
layout: default
class: style-school variant-grid
style: |
  --slide-bg: #4C0519;
  --slide-text: #FFFFFF;
  --accent-primary: #0EA5E9;
  --accent-secondary: #EC4899;
  --accent-tertiary: #EAB308;
  --font-base: 'Outfit', 'Gochi Hand', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Gochi+Hand&display=swap&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="school-wrapper" style="display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;">
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}'><div class="pill">GLOBAL REACH</div></div>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}'><div class="stat">1300</div></div>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 200}}' style="font-size:2rem;font-weight:900;text-transform:uppercase;letter-spacing:2px;">YEARS OF CONTINUITY</div>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 300}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;margin-top:1.5rem;">From the 7th century until the early 20th, the model of the Khilafah remained the central political identity of the Muslim world.</div>
</div>

---
layout: default
class: style-school variant-dots
style: |
  --slide-bg: #0F172A;
  --slide-text: #FFFFFF;
  --accent-primary: #0EA5E9;
  --accent-secondary: #EC4899;
  --accent-tertiary: #EAB308;
  --font-base: 'Outfit', 'Gochi Hand', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Gochi+Hand&display=swap&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="school-wrapper" style="display:flex;flex-direction:column;height:100%;">
  <div class="pill">LEGAL SYSTEM</div>
  <h1 style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">Justice for All</h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;width:100%;margin-top:2rem;flex:1;">
    <div v-click class="card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;"><div style='font-size:3rem;margin-bottom:1rem;'>⚖️</div><div style='font-size:1.2rem;font-weight:800;'>Equity: Protection of rights for Muslims and non-Muslims alike.</div></div>
    <div v-click class="card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;"><div style='font-size:3rem;margin-bottom:1rem;'>📜</div><div style='font-size:1.2rem;font-weight:800;'>Accountability: The Caliph is subject to the same law as the citizens.</div></div>
  </div>
</div>

---
layout: center
class: style-school variant-notebook
style: |
  --slide-bg: #1A1F5E;
  --slide-text: #FFFFFF;
  --accent-primary: #0EA5E9;
  --accent-secondary: #EC4899;
  --accent-tertiary: #EAB308;
  --font-base: 'Outfit', 'Gochi Hand', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Gochi+Hand&display=swap&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="school-wrapper" style="display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;">
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">A Legacy Unfolding.</h1>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size:1.5rem;opacity:0.8;">Revisiting the history to inspire the future.</div>
</div>
