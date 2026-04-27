---
layout: center
class: style-school
bg_video_url: https://assets.mixkit.co/videos/preview/mixkit-slow-motion-of-water-splashing-on-a-blue-background-34444-large.mp4
style: |
  --slide-bg: #1A2570;
  --slide-text: #FFFFFF;
  --accent-primary: #22D3EE;
  --accent-secondary: #F472B6;
  --accent-tertiary: #FACC15;
  --font-base: 'Outfit', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet" />
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />
<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden"><div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div><div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div><div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div></div>
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}'><div class="pill">DAILY SUPERPOWER</div></div>
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">Sparkling Clean!</h1>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;">The Amazing Secret Benefits of Wudu</div>
</div>

---
layout: center
class: style-school
style: |
  --slide-bg: #0D1B4B;
  --slide-text: #FFFFFF;
  --accent-primary: #22D3EE;
  --accent-secondary: #F472B6;
  --accent-tertiary: #FACC15;
  --font-base: 'Outfit', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet" />
<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden"><div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div><div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div><div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div></div>
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 0}}' style="font-size:4rem;margin-bottom:1rem;">🛡️</div>
  <div v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 100}}'><div class="pill">PART 01</div></div>
  <h1 v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 200}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;text-transform:uppercase;">Our Shield</h1>
  <div v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 300}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;">How Wudu protects our body from tiny invisible monsters!</div>
</div>

---
layout: default
class: style-school
style: |
  --slide-bg: #111C55;
  --slide-text: #FFFFFF;
  --accent-primary: #22D3EE;
  --accent-secondary: #F472B6;
  --accent-tertiary: #FACC15;
  --font-base: 'Outfit', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet" />
<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden"><div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div><div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div><div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div></div>
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div class="pill">HYGIENE</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Germ-Buster!</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; max-width:60%;">Wudu washes away germs and dust from our skin 5 times a day. It's like having a deep-clean car wash for your body!</div>
  <div v-click style="margin-top:auto;padding:1.5rem;background:color-mix(in srgb,var(--slide-text) 5%,transparent);border-left:4px solid var(--accent-primary);border-radius:8px;">
    <div style="font-size:2rem;margin-bottom:0.5rem;">🧼</div>
    <div style="font-weight:700;">Invisible Cleanliness</div>
  </div>
</div>

---
layout: default
class: style-school
style: |
  --slide-bg: #1A2570;
  --slide-text: #FFFFFF;
  --accent-primary: #22D3EE;
  --accent-secondary: #F472B6;
  --accent-tertiary: #FACC15;
  --font-base: 'Outfit', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet" />
<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden"><div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div><div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div><div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div></div>
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}'><div class="pill">THE FLOW</div></div>
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">The Healthy Cycle</h1>
  <div style="flex:1;position:relative;width:100%;display:flex;align-items:center;justify-content:center;margin-top:20px;margin-bottom:40px;">
    <div v-motion :initial="{scale:0}" :enter="{scale:1,transition:{type:'spring',delay:500}}" style="width:62.99999999999999px;height:62.99999999999999px;background:var(--accent-primary);border-radius:50%;z-index:20;display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px var(--accent-primary);pointer-events:auto;"><div style="color:black;font-weight:900;font-size:0.5rem;text-transform:uppercase;letter-spacing:1px;text-align:center;">THE FLOW</div></div>
    <div style="position:absolute;width:230.0px;height:230.0px;border:1px dashed color-mix(in srgb,var(--slide-text) 20%,transparent);border-radius:50%;pointer-events:none;z-index:1;"></div>
    <div style="position:absolute;left:50%;top:50%;transform:rotate(0.0deg) translate(115.0px) rotate(-0.0deg);pointer-events:none;z-index:10;"><div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 200}}' style="width:90px;height:90px;margin-left:-45.0px;margin-top:-45.0px;background:color-mix(in srgb,var(--slide-bg) 90%,transparent);border:2px solid color-mix(in srgb,var(--accent-primary) 100%,transparent);border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;font-size:0.7rem;font-weight:800;box-shadow:0 0 20px color-mix(in srgb,var(--accent-primary) 30%,transparent);pointer-events:auto;backdrop-filter:blur(10px);">Fresh Face</div></div><div style="position:absolute;left:50%;top:50%;transform:rotate(72.0deg) translate(115.0px) rotate(-72.0deg);pointer-events:none;z-index:10;"><div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 300}}' style="width:90px;height:90px;margin-left:-45.0px;margin-top:-45.0px;background:color-mix(in srgb,var(--slide-bg) 90%,transparent);border:2px solid color-mix(in srgb,var(--accent-primary) 85%,transparent);border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;font-size:0.7rem;font-weight:800;box-shadow:0 0 20px color-mix(in srgb,var(--accent-primary) 30%,transparent);pointer-events:auto;backdrop-filter:blur(10px);">Clean Hands</div></div><div style="position:absolute;left:50%;top:50%;transform:rotate(144.0deg) translate(115.0px) rotate(-144.0deg);pointer-events:none;z-index:10;"><div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 400}}' style="width:90px;height:90px;margin-left:-45.0px;margin-top:-45.0px;background:color-mix(in srgb,var(--slide-bg) 90%,transparent);border:2px solid color-mix(in srgb,var(--accent-primary) 70%,transparent);border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;font-size:0.7rem;font-weight:800;box-shadow:0 0 20px color-mix(in srgb,var(--accent-primary) 30%,transparent);pointer-events:auto;backdrop-filter:blur(10px);">Cool Head</div></div><div style="position:absolute;left:50%;top:50%;transform:rotate(216.0deg) translate(115.0px) rotate(-216.0deg);pointer-events:none;z-index:10;"><div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 500}}' style="width:90px;height:90px;margin-left:-45.0px;margin-top:-45.0px;background:color-mix(in srgb,var(--slide-bg) 90%,transparent);border:2px solid color-mix(in srgb,var(--accent-primary) 55%,transparent);border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;font-size:0.7rem;font-weight:800;box-shadow:0 0 20px color-mix(in srgb,var(--accent-primary) 30%,transparent);pointer-events:auto;backdrop-filter:blur(10px);">Happy Feet</div></div><div style="position:absolute;left:50%;top:50%;transform:rotate(288.0deg) translate(115.0px) rotate(-288.0deg);pointer-events:none;z-index:10;"><div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 600}}' style="width:90px;height:90px;margin-left:-45.0px;margin-top:-45.0px;background:color-mix(in srgb,var(--slide-bg) 90%,transparent);border:2px solid color-mix(in srgb,var(--accent-primary) 40%,transparent);border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;font-size:0.7rem;font-weight:800;box-shadow:0 0 20px color-mix(in srgb,var(--accent-primary) 30%,transparent);pointer-events:auto;backdrop-filter:blur(10px);">Bright Eyes</div></div>
  </div>
</div>

---
layout: default
class: style-school
style: |
  --slide-bg: #1A2570;
  --slide-text: #FFFFFF;
  --accent-primary: #22D3EE;
  --accent-secondary: #F472B6;
  --accent-tertiary: #FACC15;
  --font-base: 'Outfit', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet" />
<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden"><div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div><div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div><div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div></div>
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}'><div class="pill">BRAIN POWER</div></div>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}'><div class="stat">100%</div></div>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 200}}' style="font-size:2rem;font-weight:900;text-transform:uppercase;letter-spacing:2px;">Energy Boost</div>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 300}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;margin-top:1.5rem;">Cool water on our face tells our brain to wake up and focus! It's nature's energy drink without the sugar.</div>
</div>

---
layout: center
class: style-school
style: |
  --slide-bg: #0D1B4B;
  --slide-text: #FFFFFF;
  --accent-primary: #22D3EE;
  --accent-secondary: #F472B6;
  --accent-tertiary: #FACC15;
  --font-base: 'Outfit', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet" />
<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden"><div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div><div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div><div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div></div>
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <div style="font-size:5rem;color:var(--accent-primary);opacity:0.5;margin-bottom:-2rem;font-family:serif;">"</div>
  <div v-motion :initial="{opacity:0}" :enter="{opacity:1}" style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;font-size:2.5rem;font-weight:700;font-style:italic;line-height:1.3;max-width:80%;">Cleanliness is half of Faith.</div>
  <div v-motion :initial="{opacity:0,y:10}" :enter="{opacity:1,y:0}" style="margin-top:2rem;font-size:1.2rem;font-weight:600;text-transform:uppercase;letter-spacing:2px;">— Prophet Muhammad (PBUH)</div>
</div>

---
layout: center
class: style-school
style: |
  --slide-bg: #1A2570;
  --slide-text: #FFFFFF;
  --accent-primary: #22D3EE;
  --accent-secondary: #F472B6;
  --accent-tertiary: #FACC15;
  --font-base: 'Outfit', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet" />
<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden"><div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div><div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div><div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div></div>
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <div style="display:inline-block;padding:4px 16px;border-radius:4px;font-size:10px;font-weight:900;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.8rem;background:rgba(255,0,0,0.2);border:1px solid rgba(255,0,0,0.5);color:#ff9999;">ACTIVITY BREAK</div>
  <div style="font-size:4rem;margin-bottom:1rem;">🎯</div>
  <h1 style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">The Wudu Challenge</h1>
  <div v-click class="card" style="max-width:70%;margin:2rem auto;font-size:1.5rem;font-weight:700;">Can you name the 4 fard (mandatory) parts of Wudu? Discuss with your partner!</div>
</div>

---
layout: center
class: style-school
bg_video_url: https://assets.mixkit.co/videos/preview/mixkit-sparkles-on-a-blue-background-34443-large.mp4
style: |
  --slide-bg: #1A2570;
  --slide-text: #FFFFFF;
  --accent-primary: #22D3EE;
  --accent-secondary: #F472B6;
  --accent-tertiary: #FACC15;
  --font-base: 'Outfit', sans-serif;
---
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet" />
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />
<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden"><div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div><div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div><div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div></div>
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div style="position:relative;z-index:10;display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;pointer-events:none;">
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">Keep Sparkling!</h1>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size:1.5rem;opacity:0.8;">Wudu today, shine forever.</div>
</div>
