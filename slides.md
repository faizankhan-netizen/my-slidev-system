---
theme: default
background: black
highlighter: shiki
lineNumbers: false
transition: fade
canvasWidth: 900
title: Al-Andalus V3 Test
---


---
layout: center
class: style-luxury
---
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-cyan-400 w-4' : 'bg-white/20']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; justify-content: center; align-items: center; text-align: center; pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}' style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">CORE</div>
  <h1 v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">AL-ANDALUS V3</h1>
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;">Testing the Cinematic Multi-Element Engine</div>
</div>



---
layout: default
class: style-luxury
bg_video_url: https://v3.cdnpk.net/videvo_files/video/free/2019-11/large_watermarked/190828_27_SuperTrees_16_preview.mp4
---
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-cyan-400 w-4' : 'bg-white/20']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">VIDEO</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">VIDEO BG TEST</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto;  max-width: 60%;"></div>
  <div v-click style="margin-top: auto; padding: 1.5rem; background: rgba(255,255,255,0.05); border-left: 4px solid var(--accent-primary, cyan); border-radius: 8px;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">✨</div>
    <div style="font-weight: 700;">The background video is reactive to GUI edits.</div>
  </div>
</div>



---
layout: default
class: style-luxury
---
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-cyan-400 w-4' : 'bg-white/20']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}' style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">LIFECYCLE</div>
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size: 2.2rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">The Andalusian Cycle (1/2)</h1>
  <div style="flex: 1; position: relative; width: 100%; display: flex; align-items: center; justify-content: center; margin-top: 20px; margin-bottom: 40px;">
    <div v-motion :initial="{scale:0}" :enter="{scale:1, transition:{type:'spring', delay:500}}" 
         style="width:62.99999999999999px; height:62.99999999999999px; background:var(--accent-primary, #00f2fe); border-radius:50%; z-index:20; display:flex; align-items:center; justify-content:center; box-shadow:0 0 40px var(--accent-primary, #00f2fe); pointer-events:auto;">
      <div style="color:black; font-weight:900; font-size:0.5rem; text-transform:uppercase; letter-spacing:1px; text-align:center;">LIFECYCLE</div>
    </div>
    <div style="position:absolute; width:210.0px; height:210.0px; border:1px dashed rgba(255,255,255,0.1); border-radius:50%; pointer-events:none; z-index:1;"></div>
    
<div style="position:absolute; left:50%; top:50%; transform:rotate(0.0deg) translate(105.0px) rotate(-0.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 200}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:rgba(0,0,0,0.8); border:2px solid #00f2fe; border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px #00f2fe44; pointer-events:auto; backdrop-filter:blur(10px);">
    Conquest (711)
  </div>
</div>

<div style="position:absolute; left:50%; top:50%; transform:rotate(90.0deg) translate(105.0px) rotate(-90.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 300}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:rgba(0,0,0,0.8); border:2px solid #4facfe; border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px #4facfe44; pointer-events:auto; backdrop-filter:blur(10px);">
    Emirate (756)
  </div>
</div>

<div style="position:absolute; left:50%; top:50%; transform:rotate(180.0deg) translate(105.0px) rotate(-180.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 400}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:rgba(0,0,0,0.8); border:2px solid #38f9d7; border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px #38f9d744; pointer-events:auto; backdrop-filter:blur(10px);">
    Caliphate (929)
  </div>
</div>

<div style="position:absolute; left:50%; top:50%; transform:rotate(270.0deg) translate(105.0px) rotate(-270.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 500}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:rgba(0,0,0,0.8); border:2px solid #6a11cb; border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px #6a11cb44; pointer-events:auto; backdrop-filter:blur(10px);">
    Taifas (1031)
  </div>
</div>

  </div>
</div>



---
layout: default
class: style-luxury
---
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-cyan-400 w-4' : 'bg-white/20']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}' style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">LIFECYCLE</div>
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size: 2.2rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">The Andalusian Cycle (2/2)</h1>
  <div style="flex: 1; position: relative; width: 100%; display: flex; align-items: center; justify-content: center; margin-top: 20px; margin-bottom: 40px;">
    <div v-motion :initial="{scale:0}" :enter="{scale:1, transition:{type:'spring', delay:500}}" 
         style="width:62.99999999999999px; height:62.99999999999999px; background:var(--accent-primary, #00f2fe); border-radius:50%; z-index:20; display:flex; align-items:center; justify-content:center; box-shadow:0 0 40px var(--accent-primary, #00f2fe); pointer-events:auto;">
      <div style="color:black; font-weight:900; font-size:0.5rem; text-transform:uppercase; letter-spacing:1px; text-align:center;">LIFECYCLE</div>
    </div>
    <div style="position:absolute; width:210.0px; height:210.0px; border:1px dashed rgba(255,255,255,0.1); border-radius:50%; pointer-events:none; z-index:1;"></div>
    
<div style="position:absolute; left:50%; top:50%; transform:rotate(0.0deg) translate(105.0px) rotate(-0.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 200}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:rgba(0,0,0,0.8); border:2px solid #00f2fe; border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px #00f2fe44; pointer-events:auto; backdrop-filter:blur(10px);">
    Almoravids (1086)
  </div>
</div>

<div style="position:absolute; left:50%; top:50%; transform:rotate(180.0deg) translate(105.0px) rotate(-180.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 300}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:rgba(0,0,0,0.8); border:2px solid #4facfe; border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px #4facfe44; pointer-events:auto; backdrop-filter:blur(10px);">
    Nasrids (1230)
  </div>
</div>

  </div>
</div>



---
layout: default
class: style-luxury
---
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-cyan-400 w-4' : 'bg-white/20']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">DEMOGRAPHICS</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Population Growth</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">The rapid urbanization of the Iberian Peninsula under the Caliphate of Cordoba.</div>
  <div style="flex: 1; min-height: 0; width: 100%; margin-top: 1rem;">
    <v-chart :option='{"backgroundColor": "transparent", "tooltip": {"trigger": "axis"}, "xAxis": {"type": "category", "data": ["750 AD", "850 AD", "950 AD", "1050 AD"], "axisLabel": {"color": "rgba(255,255,255,0.6)"}}, "yAxis": {"type": "value", "axisLabel": {"color": "rgba(255,255,255,0.6)"}, "splitLine": {"lineStyle": {"color": "rgba(255,255,255,0.1)"}}}, "series": [{"data": [4.5, 6.2, 8.8, 9.5], "type": "line", "itemStyle": {"color": "var(--accent-primary, #00f2fe)"}, "areaStyle": {"opacity": 0.3}}]}' autoresize style="width: 100%; height: 100%;" />
  </div>
</div>



---
layout: default
class: style-luxury
---
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-cyan-400 w-4' : 'bg-white/20']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">CITIES</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Urban Superiority</h1>
  <div style="margin-top: 1.5rem; width: 100%; overflow: hidden; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); background: rgba(0,0,0,0.2);">
    <table style="width: 100%; border-collapse: collapse; font-size: 1.1rem;">
      <thead><tr style="background: rgba(255,255,255,0.05);"><th style='padding: 1rem; text-align: left; border-bottom: 2px solid rgba(255,255,255,0.2); text-transform: uppercase; font-size: 0.8rem;'>City</th><th style='padding: 1rem; text-align: left; border-bottom: 2px solid rgba(255,255,255,0.2); text-transform: uppercase; font-size: 0.8rem;'>Region</th><th style='padding: 1rem; text-align: left; border-bottom: 2px solid rgba(255,255,255,0.2); text-transform: uppercase; font-size: 0.8rem;'>Population</th><th style='padding: 1rem; text-align: left; border-bottom: 2px solid rgba(255,255,255,0.2); text-transform: uppercase; font-size: 0.8rem;'>Library Count</th></tr></thead>
      <tbody><tr style='background: rgba(255,255,255,0.03);'><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>Cordoba</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>Al-Andalus</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>500,000+</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>70+</td></tr><tr style='background: transparent;'><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>London</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>England</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>~20,000</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>0</td></tr><tr style='background: rgba(255,255,255,0.03);'><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>Paris</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>France</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>~30,000</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>1</td></tr><tr style='background: transparent;'><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>Rome</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>Italy</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>~40,000</td><td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>5</td></tr></tbody>
    </table>
  </div>
</div>



---
layout: default
class: style-luxury
---
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-cyan-400 w-4' : 'bg-white/20']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div style="display: flex; width: 100%; height: 100%; gap: 3rem;">
    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center;">
      <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}' style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">VISUALS</div>
      <h1 v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}' style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Architectural Zenith</h1>
      <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">The intricate details of the Alhambra represent the pinnacle of Nasrid craftsmanship and geometric precision.</div>
      <a href="https://www.alhambra-patronato.es/" v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 300}}' style="margin-top: 2rem; padding: 1rem 2rem; background: var(--accent-primary, cyan); color: black; font-weight: 900; text-decoration: none; border-radius: 50px; width: fit-content;">EXPLORE THE PALACE</a>
    </div>
    <div v-motion :initial="{opacity:0, x:50}" :enter="{opacity:1, x:0}" style="flex: 1.2; padding: 1rem;"><img src='/alhambra.png' style='width: 100%; height: 100%; object-fit: cover; border-radius: 12px;' /></div>
  </div>
</div>



---
layout: center
class: style-luxury
---
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-cyan-400 w-4' : 'bg-white/20']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; justify-content: center; align-items: center; text-align: center; pointer-events:none;">
  <h1 v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 0}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">V3 VALIDATED</h1>
  <div v-motion :initial='{"opacity": 0, "x": -30}' :enter='{"opacity": 1, "x": 0, "transition": {"duration": 500, "delay": 100}}' style="font-size: 1.5rem; opacity: 0.8;">Multi-modal engine is now operational.</div>
</div>

