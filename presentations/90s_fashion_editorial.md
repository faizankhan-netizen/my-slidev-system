---
layout: center
class: style-editorial variant-red
bg_video_url: https://assets.mixkit.co/videos/preview/mixkit-fashion-model-posing-for-a-photoshoot-in-a-studio-39873-large.mp4
style: |
  --slide-bg: #E5E0D8;
  --slide-text: #1A1A1A;
  --accent-primary: #991B1B;
  --accent-secondary: #1A1A1A;
  --accent-tertiary: #F5F5DC;
  --font-base: 'Playfair Display', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700&display=swap" rel="stylesheet" />
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="content-wrapper" style="display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;">
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}'><div class="pill">EDITORIAL</div></div>
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">90s REBORN</h1>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;">The Defining Decade of Modern Fashion</div>
</div>

---
layout: center
class: style-editorial variant-red
style: |
  --slide-bg: #E5E0D8;
  --slide-text: #1A1A1A;
  --accent-primary: #991B1B;
  --accent-secondary: #1A1A1A;
  --accent-tertiary: #F5F5DC;
  --font-base: 'Playfair Display', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="content-wrapper" style="display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;">
  <div style="font-size:5rem;color:var(--accent-primary);opacity:0.5;margin-bottom:-2rem;font-family:serif;">"</div>
  <div v-motion :initial="{opacity:0}" :enter="{opacity:1}" style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;font-size:2.5rem;font-weight:700;font-style:italic;line-height:1.3;max-width:80%;">I don't design clothes. I design dreams.</div>
  <div v-motion :initial="{opacity:0,y:10}" :enter="{opacity:1,y:0}" style="margin-top:2rem;font-size:1.2rem;font-weight:600;text-transform:uppercase;letter-spacing:2px;">— Ralph Lauren</div>
</div>

---
layout: default
class: style-editorial
style: |
  --slide-bg: #FDFBF7;
  --slide-text: #1A1A1A;
  --accent-primary: #991B1B;
  --accent-secondary: #1A1A1A;
  --accent-tertiary: #F5F5DC;
  --font-base: 'Playfair Display', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="content-wrapper" style="display:flex;flex-direction:column;height:100%;">
  <div style="display:flex;width:100%;height:100%;gap:3rem;">
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
      <div v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 0}}'><div class="pill">THE AESTHETIC</div></div>
      <h1 v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 100}}' style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">The Grunge Movement</h1>
      <div v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">Anti-fashion became the highest fashion. Born in Seattle, distressed denim, flannel, and combat boots dominated the runways and the streets alike.</div>
    </div>
    <div v-motion :initial="{opacity:0,x:50}" :enter="{opacity:1,x:0}" style="flex:1.2;padding:1rem;"><img src='https://images.unsplash.com/photo-1542272201-b1ca555f8505?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80' style='width:100%;height:100%;object-fit:cover;border-radius:12px;' /></div>
  </div>
</div>

---
layout: default
class: style-editorial
style: |
  --slide-bg: #F3F0E6;
  --slide-text: #1A1A1A;
  --accent-primary: #991B1B;
  --accent-secondary: #1A1A1A;
  --accent-tertiary: #F5F5DC;
  --font-base: 'Playfair Display', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="content-wrapper" style="display:flex;flex-direction:column;height:100%;">
  <div class="pill">EVOLUTION</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">The Shift to Minimalism</h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;width:100%;margin-top:2rem;flex:1;">
    <div v-click class="card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;"><div style='font-size:3rem;margin-bottom:1rem;'>👗</div><div style='font-size:1.2rem;font-weight:800;'>80s: Neon & Shoulder Pads</div></div>
    <div v-click class="card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;"><div style='font-size:3rem;margin-bottom:1rem;'>🖤</div><div style='font-size:1.2rem;font-weight:800;'>90s: Slip Dresses & Neutral Tones</div></div>
  </div>
</div>

---
layout: default
class: style-editorial
style: |
  --slide-bg: #F3F0E6;
  --slide-text: #1A1A1A;
  --accent-primary: #991B1B;
  --accent-secondary: #1A1A1A;
  --accent-tertiary: #F5F5DC;
  --font-base: 'Playfair Display', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="content-wrapper" style="display:flex;flex-direction:column;height:100%;">
  <div class="pill">WARDROBE</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Iconic Staples</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">The key pieces that defined the 90s silhouette and continue to influence modern wardrobes.</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;width:100%;margin-top:1rem;flex:1;"><div v-click class="card" style="display:flex;flex-direction:column;gap:0.5rem;"><div style="font-size:2rem;">🧥</div><div style="font-weight:700;font-size:1.1rem;">Leather Jackets</div></div><div v-click class="card" style="display:flex;flex-direction:column;gap:0.5rem;"><div style="font-size:2rem;">👖</div><div style="font-weight:700;font-size:1.1rem;">Baggy Denim</div></div><div v-click class="card" style="display:flex;flex-direction:column;gap:0.5rem;"><div style="font-size:2rem;">👢</div><div style="font-weight:700;font-size:1.1rem;">Combat Boots</div></div><div v-click class="card" style="display:flex;flex-direction:column;gap:0.5rem;"><div style="font-size:2rem;">📿</div><div style="font-weight:700;font-size:1.1rem;">Choker Necklaces</div></div></div>
</div>

---
layout: default
class: style-editorial variant-red
style: |
  --slide-bg: #E5E0D8;
  --slide-text: #1A1A1A;
  --accent-primary: #991B1B;
  --accent-secondary: #1A1A1A;
  --accent-tertiary: #F5F5DC;
  --font-base: 'Playfair Display', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="content-wrapper" style="display:flex;flex-direction:column;height:100%;">
  <div style="display:flex;width:100%;height:100%;gap:3rem;">
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
      <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}'><div class="pill">ICONS</div></div>
      <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">The Supermodel Era</h1>
      <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">Naomi, Cindy, Linda, Christy, and Tatjana. The 90s saw the birth of models who were bigger than the brands they walked for.</div>
    </div>
    <div v-motion :initial="{opacity:0,x:50}" :enter="{opacity:1,x:0}" style="flex:1.2;padding:1rem;"><img src='https://images.unsplash.com/photo-1492446845049-9c50cc313f00?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80' style='width:100%;height:100%;object-fit:cover;border-radius:12px;' /></div>
  </div>
</div>

---
layout: default
class: style-editorial
style: |
  --slide-bg: #FDFBF7;
  --slide-text: #1A1A1A;
  --accent-primary: #991B1B;
  --accent-secondary: #1A1A1A;
  --accent-tertiary: #F5F5DC;
  --font-base: 'Playfair Display', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700&display=swap" rel="stylesheet" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="content-wrapper" style="display:flex;flex-direction:column;height:100%;">
  <div style="display:flex;width:100%;height:100%;gap:3rem;">
    <div style="flex:1.2;display:flex;flex-direction:column;">
      <div class="pill">SPOTLIGHT</div>
      <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Calvin Klein</h1>
      <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">Defining the aesthetic of the 90s with stark, black-and-white campaigns and a controversial focus on 'heroin chic' and raw minimalism.</div>
      <div v-click style="margin-top:auto;padding:1.5rem;background:color-mix(in srgb,var(--slide-text) 5%,transparent);border-radius:8px;border-left:4px solid var(--accent-primary);">
        <span style="font-weight:900;font-size:0.8rem;opacity:0.5;">CASE HIGHLIGHT</span><br/>
        <div style="font-size:1.1rem;font-weight:700;margin-top:0.5rem;">The campaign that introduced Kate Moss to the world and changed fashion photography.</div>
      </div>
    </div>
    <div v-click style="flex:0.8;background:color-mix(in srgb,var(--slide-text) 3%,transparent);border-radius:12px;border:1px dashed color-mix(in srgb,var(--slide-text) 10%,transparent);display:flex;align-items:center;justify-content:center;padding:2rem;">
      <div style="text-align:center;"><div style="font-size:5rem;margin-bottom:1rem;">📸</div><div style="font-weight:900;letter-spacing:2px;"><div class="stat-giant">CK</div></div><div style="opacity:0.6;font-size:0.9rem;">MINIMALISM</div></div>
    </div>
  </div>
</div>

---
layout: center
class: style-editorial variant-red
bg_video_url: https://assets.mixkit.co/videos/preview/mixkit-woman-walking-on-a-catwalk-with-a-fashion-dress-41808-large.mp4
style: |
  --slide-bg: #E5E0D8;
  --slide-text: #1A1A1A;
  --accent-primary: #991B1B;
  --accent-secondary: #1A1A1A;
  --accent-tertiary: #F5F5DC;
  --font-base: 'Playfair Display', serif;
---
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700&display=swap" rel="stylesheet" />
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>
<div class="content-wrapper" style="display:flex;flex-direction:column;height:100%;justify-content:center;align-items:center;text-align:center;">
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">Timeless.</h1>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size:1.5rem;opacity:0.8;">The decade that never truly left.</div>
</div>
