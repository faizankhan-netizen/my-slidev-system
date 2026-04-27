---
layout: center
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}'><div class="pill">V5 MATRIX TEST</div></div>
  <h1 v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">Test Cover</h1>
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;">Ensuring Design Sovereignty</div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}'><div class="pill">V5 MATRIX TEST</div></div>
  <h1 v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}' style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Test Agenda</h1>
  <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:1.5rem;margin-top:2rem;"><div v-click v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 200}}' @click="$nav.go($nav.currentPage + 1)" style="background:color-mix(in srgb,var(--slide-text) 5%,transparent);border:1px solid color-mix(in srgb,var(--slide-text) 10%,transparent);padding:1.5rem;border-radius:16px;cursor:pointer;transition:all 0.3s ease;pointer-events:auto;"><div style="font-size:0.8rem;opacity:0.5;font-weight:900;margin-bottom:0.5rem;">01</div><div style="font-size:1.2rem;font-weight:900;">Step 1|Initial Setup</div></div><div v-click v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 300}}' @click="$nav.go($nav.currentPage + 2)" style="background:color-mix(in srgb,var(--slide-text) 5%,transparent);border:1px solid color-mix(in srgb,var(--slide-text) 10%,transparent);padding:1.5rem;border-radius:16px;cursor:pointer;transition:all 0.3s ease;pointer-events:auto;"><div style="font-size:0.8rem;opacity:0.5;font-weight:900;margin-bottom:0.5rem;">02</div><div style="font-size:1.2rem;font-weight:900;">Step 2|Refactor Logic</div></div><div v-click v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 400}}' @click="$nav.go($nav.currentPage + 3)" style="background:color-mix(in srgb,var(--slide-text) 5%,transparent);border:1px solid color-mix(in srgb,var(--slide-text) 10%,transparent);padding:1.5rem;border-radius:16px;cursor:pointer;transition:all 0.3s ease;pointer-events:auto;"><div style="font-size:0.8rem;opacity:0.5;font-weight:900;margin-bottom:0.5rem;">03</div><div style="font-size:1.2rem;font-weight:900;">Step 3|Inject Classes</div></div><div v-click v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 500}}' @click="$nav.go($nav.currentPage + 4)" style="background:color-mix(in srgb,var(--slide-text) 5%,transparent);border:1px solid color-mix(in srgb,var(--slide-text) 10%,transparent);padding:1.5rem;border-radius:16px;cursor:pointer;transition:all 0.3s ease;pointer-events:auto;"><div style="font-size:0.8rem;opacity:0.5;font-weight:900;margin-bottom:0.5rem;">04</div><div style="font-size:1.2rem;font-weight:900;">Step 4|Final Render</div></div></div>
</div>

---
layout: center
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}' style="font-size:4rem;margin-bottom:1rem;">✨</div>
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}'><div class="pill">V5 MATRIX TEST</div></div>
  <h1 v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 200}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;text-transform:uppercase;">Test Section Intro</h1>
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 300}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;">This is a visual regression test for the 'section_intro' layout in the Cinematic Engine V5.</div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div class="pill">V5 MATRIX TEST</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Test Concept</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; max-width:60%;">This is a visual regression test for the 'concept' layout in the Cinematic Engine V5.</div>
  <div v-click style="margin-top:auto;padding:1.5rem;background:color-mix(in srgb,var(--slide-text) 5%,transparent);border-left:4px solid var(--accent-primary);border-radius:8px;">
    <div style="font-size:2rem;margin-bottom:0.5rem;">✨</div>
    <div style="font-weight:700;"></div>
  </div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div class="pill">V5 MATRIX TEST</div>
  <h1 style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">Test Comparison</h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;width:100%;margin-top:2rem;flex:1;">
    <div v-click class="card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;"><div style='font-size:3rem;margin-bottom:1rem;'>❌ Legacy Inline Styles</div><div style='font-size:1.2rem;font-weight:800;'>Hardcoded</div></div>
    <div v-click class="card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;"><div style='font-size:3rem;margin-bottom:1rem;'>✅ V5 Design Sovereignty</div><div style='font-size:1.2rem;font-weight:800;'>Class-based</div></div>
  </div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}'><div class="pill">V5 MATRIX TEST</div></div>
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}'><div class="stat">99.9%</div></div>
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 200}}' style="font-size:2rem;font-weight:900;text-transform:uppercase;letter-spacing:2px;">Uptime</div>
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 300}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;margin-top:1.5rem;">This is a visual regression test for the 'data_point' layout in the Cinematic Engine V5.</div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div class="pill">V5 MATRIX TEST</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Test Process</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">This is a visual regression test for the 'process' layout in the Cinematic Engine V5.</div>
  <div style="margin-top:1rem;width:100%;"><div v-click style="display:flex;gap:1.5rem;align-items:flex-start;margin-bottom:1rem;"><div style="font-size:1.5rem;font-weight:900;color:var(--accent-primary);opacity:0.8;">01</div><div v-click class="card" style="padding:1rem;">Step 1|Initial Setup</div></div><div v-click style="display:flex;gap:1.5rem;align-items:flex-start;margin-bottom:1rem;"><div style="font-size:1.5rem;font-weight:900;color:var(--accent-primary);opacity:0.8;">02</div><div v-click class="card" style="padding:1rem;">Step 2|Refactor Logic</div></div><div v-click style="display:flex;gap:1.5rem;align-items:flex-start;margin-bottom:1rem;"><div style="font-size:1.5rem;font-weight:900;color:var(--accent-primary);opacity:0.8;">03</div><div v-click class="card" style="padding:1rem;">Step 3|Inject Classes</div></div><div v-click style="display:flex;gap:1.5rem;align-items:flex-start;margin-bottom:1rem;"><div style="font-size:1.5rem;font-weight:900;color:var(--accent-primary);opacity:0.8;">04</div><div v-click class="card" style="padding:1rem;">Step 4|Final Render</div></div></div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div class="pill">V5 MATRIX TEST</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Test Feature Grid</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">This is a visual regression test for the 'feature_grid' layout in the Cinematic Engine V5.</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;width:100%;margin-top:1rem;flex:1;"><div v-click class="card" style="display:flex;flex-direction:column;gap:0.5rem;"><div style="font-size:2rem;">Step 1</div><div style="font-weight:700;font-size:1.1rem;">Initial Setup</div></div><div v-click class="card" style="display:flex;flex-direction:column;gap:0.5rem;"><div style="font-size:2rem;">Step 2</div><div style="font-weight:700;font-size:1.1rem;">Refactor Logic</div></div><div v-click class="card" style="display:flex;flex-direction:column;gap:0.5rem;"><div style="font-size:2rem;">Step 3</div><div style="font-weight:700;font-size:1.1rem;">Inject Classes</div></div><div v-click class="card" style="display:flex;flex-direction:column;gap:0.5rem;"><div style="font-size:2rem;">Step 4</div><div style="font-weight:700;font-size:1.1rem;">Final Render</div></div></div>
</div>

---
layout: center
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <div style="font-size:5rem;color:var(--accent-primary);opacity:0.5;margin-bottom:-2rem;font-family:serif;">"</div>
  <div v-motion :initial="{opacity:0}" :enter="{opacity:1}" style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;font-size:2.5rem;font-weight:700;font-style:italic;line-height:1.3;max-width:80%;">Design is not just what it looks like and feels like. Design is how it works.</div>
  <div v-motion :initial="{opacity:0,y:10}" :enter="{opacity:1,y:0}" style="margin-top:2rem;font-size:1.2rem;font-weight:600;text-transform:uppercase;letter-spacing:2px;">— Steve Jobs</div>
</div>

---
layout: center
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <div style="display:inline-block;padding:4px 16px;border-radius:4px;font-size:10px;font-weight:900;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.8rem;background:rgba(255,0,0,0.2);border:1px solid rgba(255,0,0,0.5);color:#ff9999;">ACTIVITY BREAK</div>
  <div style="font-size:4rem;margin-bottom:1rem;">✨</div>
  <h1 style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">Test Activity</h1>
  <div v-click class="card" style="max-width:70%;margin:2rem auto;font-size:1.5rem;font-weight:700;">This is a visual regression test for the 'activity' layout in the Cinematic Engine V5.</div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div style="display:flex;width:100%;height:100%;gap:3rem;">
    <div style="flex:1.2;display:flex;flex-direction:column;">
      <div class="pill">V5 MATRIX TEST</div>
      <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Test Case Study</h1>
      <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">This is a visual regression test for the 'case_study' layout in the Cinematic Engine V5.</div>
      <div v-click style="margin-top:auto;padding:1.5rem;background:color-mix(in srgb,var(--slide-text) 5%,transparent);border-radius:8px;border-left:4px solid var(--accent-primary);">
        <span style="font-weight:900;font-size:0.8rem;opacity:0.5;">CASE HIGHLIGHT</span><br/>
        <div style="font-size:1.1rem;font-weight:700;margin-top:0.5rem;">V5 Migration Success</div>
      </div>
    </div>
    <div v-click style="flex:0.8;background:color-mix(in srgb,var(--slide-text) 3%,transparent);border-radius:12px;border:1px dashed color-mix(in srgb,var(--slide-text) 10%,transparent);display:flex;align-items:center;justify-content:center;padding:2rem;">
      <div style="text-align:center;"><div style="font-size:5rem;margin-bottom:1rem;">🚀</div><div style="font-weight:900;letter-spacing:2px;"><div class="stat">10x</div></div><div style="opacity:0.6;font-size:0.9rem;">Cleanliness</div></div>
    </div>
  </div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}'><div class="pill">V5 MATRIX TEST</div></div>
  <h1 v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}' style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Test Cycle</h1>
  <div style="flex:1;position:relative;width:100%;display:flex;align-items:center;justify-content:center;margin-top:20px;margin-bottom:40px;">
    <div v-motion :initial="{scale:0}" :enter="{scale:1,transition:{type:'spring',delay:500}}" style="width:62.99999999999999px;height:62.99999999999999px;background:var(--accent-primary);border-radius:50%;z-index:20;display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px var(--accent-primary);pointer-events:auto;"><div style="color:black;font-weight:900;font-size:0.5rem;text-transform:uppercase;letter-spacing:1px;text-align:center;">V5 MATRIX TEST</div></div>
    <div style="position:absolute;width:230.0px;height:230.0px;border:1px dashed color-mix(in srgb,var(--slide-text) 20%,transparent);border-radius:50%;pointer-events:none;z-index:1;"></div>
    <div style="position:absolute;left:50%;top:50%;transform:rotate(0.0deg) translate(115.0px) rotate(-0.0deg);pointer-events:none;z-index:10;"><div v-click v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 200}}' style="width:90px;height:90px;margin-left:-45.0px;margin-top:-45.0px;background:color-mix(in srgb,var(--slide-bg) 90%,transparent);border:2px solid color-mix(in srgb,var(--accent-primary) 100%,transparent);border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;font-size:0.7rem;font-weight:800;box-shadow:0 0 20px color-mix(in srgb,var(--accent-primary) 30%,transparent);pointer-events:auto;backdrop-filter:blur(10px);">Step 1|Initial Setup</div></div><div style="position:absolute;left:50%;top:50%;transform:rotate(90.0deg) translate(115.0px) rotate(-90.0deg);pointer-events:none;z-index:10;"><div v-click v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 300}}' style="width:90px;height:90px;margin-left:-45.0px;margin-top:-45.0px;background:color-mix(in srgb,var(--slide-bg) 90%,transparent);border:2px solid color-mix(in srgb,var(--accent-primary) 85%,transparent);border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;font-size:0.7rem;font-weight:800;box-shadow:0 0 20px color-mix(in srgb,var(--accent-primary) 30%,transparent);pointer-events:auto;backdrop-filter:blur(10px);">Step 2|Refactor Logic</div></div><div style="position:absolute;left:50%;top:50%;transform:rotate(180.0deg) translate(115.0px) rotate(-180.0deg);pointer-events:none;z-index:10;"><div v-click v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 400}}' style="width:90px;height:90px;margin-left:-45.0px;margin-top:-45.0px;background:color-mix(in srgb,var(--slide-bg) 90%,transparent);border:2px solid color-mix(in srgb,var(--accent-primary) 70%,transparent);border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;font-size:0.7rem;font-weight:800;box-shadow:0 0 20px color-mix(in srgb,var(--accent-primary) 30%,transparent);pointer-events:auto;backdrop-filter:blur(10px);">Step 3|Inject Classes</div></div><div style="position:absolute;left:50%;top:50%;transform:rotate(270.0deg) translate(115.0px) rotate(-270.0deg);pointer-events:none;z-index:10;"><div v-click v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 500}}' style="width:90px;height:90px;margin-left:-45.0px;margin-top:-45.0px;background:color-mix(in srgb,var(--slide-bg) 90%,transparent);border:2px solid color-mix(in srgb,var(--accent-primary) 55%,transparent);border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;font-size:0.7rem;font-weight:800;box-shadow:0 0 20px color-mix(in srgb,var(--accent-primary) 30%,transparent);pointer-events:auto;backdrop-filter:blur(10px);">Step 4|Final Render</div></div>
  </div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div class="pill">V5 MATRIX TEST</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Test Chart</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">This is a visual regression test for the 'chart' layout in the Cinematic Engine V5.</div>
  <div style="flex:1;min-height:0;width:100%;margin-top:1rem;"><v-chart :option='{"backgroundColor": "transparent", "tooltip": {"trigger": "axis"}, "xAxis": {"type": "category", "data": ["A", "B", "C"], "axisLabel": {"color": "#FFFFFF"}}, "yAxis": {"type": "value", "axisLabel": {"color": "#FFFFFF"}, "splitLine": {"lineStyle": {"color": "rgba(128,128,128,0.2)"}}}, "series": [{"data": [10, 25, 15], "type": "bar", "itemStyle": {"color": "var(--accent-primary)"}, "areaStyle": null}]}' autoresize style="width:100%;height:100%;" /></div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div class="pill">V5 MATRIX TEST</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Test Table</h1>
  <div style="margin-top:1.5rem;width:100%;overflow:hidden;border-radius:12px;border:1px solid color-mix(in srgb,var(--slide-text) 10%,transparent);background:rgba(0,0,0,0.2);"><table style="width:100%;border-collapse:collapse;font-size:1.1rem;"><thead><tr style="background:color-mix(in srgb,var(--slide-text) 5%,transparent);"><th style='padding:1rem;text-align:left;border-bottom:2px solid color-mix(in srgb,var(--slide-text) 20%,transparent);text-transform:uppercase;font-size:0.8rem;'>Feature</th><th style='padding:1rem;text-align:left;border-bottom:2px solid color-mix(in srgb,var(--slide-text) 20%,transparent);text-transform:uppercase;font-size:0.8rem;'>Status</th><th style='padding:1rem;text-align:left;border-bottom:2px solid color-mix(in srgb,var(--slide-text) 20%,transparent);text-transform:uppercase;font-size:0.8rem;'>Impact</th></tr></thead><tbody><tr style='background:color-mix(in srgb,var(--slide-text) 3%,transparent);'><td style='padding:1rem;border-bottom:1px solid color-mix(in srgb,var(--slide-text) 5%,transparent);'>Design DNA</td><td style='padding:1rem;border-bottom:1px solid color-mix(in srgb,var(--slide-text) 5%,transparent);'>Passed</td><td style='padding:1rem;border-bottom:1px solid color-mix(in srgb,var(--slide-text) 5%,transparent);'>High</td></tr><tr style='background:transparent;'><td style='padding:1rem;border-bottom:1px solid color-mix(in srgb,var(--slide-text) 5%,transparent);'>Class Mapping</td><td style='padding:1rem;border-bottom:1px solid color-mix(in srgb,var(--slide-text) 5%,transparent);'>Passed</td><td style='padding:1rem;border-bottom:1px solid color-mix(in srgb,var(--slide-text) 5%,transparent);'>Critical</td></tr><tr style='background:color-mix(in srgb,var(--slide-text) 3%,transparent);'><td style='padding:1rem;border-bottom:1px solid color-mix(in srgb,var(--slide-text) 5%,transparent);'>CSS Control</td><td style='padding:1rem;border-bottom:1px solid color-mix(in srgb,var(--slide-text) 5%,transparent);'>Passed</td><td style='padding:1rem;border-bottom:1px solid color-mix(in srgb,var(--slide-text) 5%,transparent);'>Total</td></tr></tbody></table></div>
</div>

---
layout: default
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div style="display:flex;width:100%;height:100%;gap:3rem;">
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
      <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}'><div class="pill">V5 MATRIX TEST</div></div>
      <h1 v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}' style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Test Media Focus</h1>
      <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">This is a visual regression test for the 'media_focus' layout in the Cinematic Engine V5.</div>
      <a href="#" v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 300}}' style="margin-top:2rem;padding:1rem 2rem;background:var(--accent-primary);color:var(--slide-bg);font-weight:900;text-decoration:none;border-radius:50px;width:fit-content;">Learn More</a>
    </div>
    <div v-motion :initial="{opacity:0,x:50}" :enter="{opacity:1,x:0}" style="flex:1.2;padding:1rem;"><img src='https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80' style='width:100%;height:100%;object-fit:cover;border-radius:12px;' /></div>
  </div>
</div>

---
layout: center
class: style-luxury
style: |
  --slide-bg: #27272A;
  --slide-text: #FFFFFF;
  --accent-primary: #D4AF37;
  --accent-secondary: #8B7355;
  --accent-tertiary: #FFD700;
  --font-base: 'Cinzel', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <h1 v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">Test Finale</h1>
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}' style="font-size:1.5rem;opacity:0.8;"></div>
</div>
