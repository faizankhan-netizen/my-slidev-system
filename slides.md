
---
layout: center
class: style-school
style: |

  --slide-bg: #FEF08A;
  --slide-text: #1A1F5E;
  --accent-primary: #3B82F6;
  --accent-secondary: #3B82F6;
  --accent-tertiary: #3B82F6;
  --font-base: 'Outfit', 'Comic Sans MS', sans-serif;

---
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;900&display=swap" rel="stylesheet">
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden">
  <div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div>
  <div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div>
  <div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div>
</div>


<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; justify-content: center; align-items: center; text-align: center; pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}' style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">INTRO</div>
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">The Magic Cloud ☁️</h1>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; text-align: center; margin: 0 auto;"></div>
</div>



---
layout: default
class: style-school
style: |

  --slide-bg: #F3F4F6;
  --slide-text: #1A1F5E;
  --accent-primary: #3B82F6;
  --accent-secondary: #3B82F6;
  --accent-tertiary: #3B82F6;
  --font-base: 'Outfit', 'Comic Sans MS', sans-serif;

---
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;900&display=swap" rel="stylesheet">
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden">
  <div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div>
  <div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div>
  <div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div>
</div>


<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">THE SECRET</div>
  <h1 style="font-size: 2.2rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">It's Not Actually in the Sky!</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto;  max-width: 60%;">When we say 'The Cloud', we aren't talking about rain clouds. The Cloud is actually just a bunch of really powerful computers sitting in giant warehouses on Earth.</div>
  <div v-click style="margin-top: auto; padding: 1.5rem; background: color-mix(in srgb, var(--slide-text) 5%, transparent); border-left: 4px solid var(--accent-primary, cyan); border-radius: 8px;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">✨</div>
    <div style="font-weight: 700;"></div>
  </div>
</div>



---
layout: default
class: style-school
style: |

  --slide-bg: #FEF08A;
  --slide-text: #1A1F5E;
  --accent-primary: #3B82F6;
  --accent-secondary: #3B82F6;
  --accent-tertiary: #3B82F6;
  --font-base: 'Outfit', 'Comic Sans MS', sans-serif;

---
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;900&display=swap" rel="stylesheet">
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden">
  <div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div>
  <div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div>
  <div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div>
</div>


<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">HOW IT HELPS</div>
  <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">Your Backpack vs. The Cloud</h1>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; width: 100%; margin-top: 2rem; flex: 1;">
    <div v-click style="background: rgba(255,255,255,0.07); padding: 1rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); width: 100%; overflow: hidden; pointer-events: auto; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; border-color: rgba(255,0,0,0.3);">
      <div style="font-size: 3rem; margin-bottom: 1rem;">Your Backpack (Computer) </div>
      <div style="font-size: 1.2rem; font-weight: 800;"> Can only hold a few books. Gets heavy and full quickly.</div>
    </div>
    <div v-click style="background: rgba(255,255,255,0.07); padding: 1rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); width: 100%; overflow: hidden; pointer-events: auto; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; border-color: rgba(0,255,0,0.3);">
      <div style="font-size: 3rem; margin-bottom: 1rem;">The Cloud (Internet) </div>
      <div style="font-size: 1.2rem; font-weight: 800;"> A giant magical library. You don't have to carry anything, just borrow it when you need it!</div>
    </div>
  </div>
</div>



---
layout: default
class: style-school
style: |

  --slide-bg: #FFFFFF;
  --slide-text: #1A1F5E;
  --accent-primary: #3B82F6;
  --accent-secondary: #3B82F6;
  --accent-tertiary: #3B82F6;
  --font-base: 'Outfit', 'Comic Sans MS', sans-serif;

---
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;900&display=swap" rel="stylesheet">
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden">
  <div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div>
  <div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div>
  <div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div>
</div>


<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 0}}' style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">HOW IT WORKS</div>
  <h1 v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 100}}' style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">The Cloud Cycle</h1>
  <div style="flex: 1; position: relative; width: 100%; display: flex; align-items: center; justify-content: center; margin-top: 20px; margin-bottom: 40px;">
    <div v-motion :initial="{scale:0}" :enter="{scale:1, transition:{type:'spring', delay:500}}" 
         style="width:62.99999999999999px; height:62.99999999999999px; background:var(--accent-primary); border-radius:50%; z-index:20; display:flex; align-items:center; justify-content:center; box-shadow:0 0 40px var(--accent-primary); pointer-events:auto;">
      <div style="color:black; font-weight:900; font-size:0.5rem; text-transform:uppercase; letter-spacing:1px; text-align:center;">HOW IT WORKS</div>
    </div>
    <div style="position:absolute; width:230.0px; height:230.0px; border:1px dashed color-mix(in srgb, var(--slide-text) 20%, transparent); border-radius:50%; pointer-events:none; z-index:1;"></div>
    
<div style="position:absolute; left:50%; top:50%; transform:rotate(0.0deg) translate(115.0px) rotate(-0.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 200}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:color-mix(in srgb, var(--slide-bg) 90%, transparent); border:2px solid color-mix(in srgb, var(--accent-primary) 100%, transparent); border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px color-mix(in srgb, var(--accent-primary) 30%, transparent); pointer-events:auto; backdrop-filter:blur(10px);">
    1. You click 'Play'
  </div>
</div>

<div style="position:absolute; left:50%; top:50%; transform:rotate(72.0deg) translate(115.0px) rotate(-72.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 300}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:color-mix(in srgb, var(--slide-bg) 90%, transparent); border:2px solid color-mix(in srgb, var(--accent-primary) 85%, transparent); border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px color-mix(in srgb, var(--accent-primary) 30%, transparent); pointer-events:auto; backdrop-filter:blur(10px);">
    2. Signal flies to space!
  </div>
</div>

<div style="position:absolute; left:50%; top:50%; transform:rotate(144.0deg) translate(115.0px) rotate(-144.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 400}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:color-mix(in srgb, var(--slide-bg) 90%, transparent); border:2px solid color-mix(in srgb, var(--accent-primary) 70%, transparent); border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px color-mix(in srgb, var(--accent-primary) 30%, transparent); pointer-events:auto; backdrop-filter:blur(10px);">
    3. Lands in the Cloud
  </div>
</div>

<div style="position:absolute; left:50%; top:50%; transform:rotate(216.0deg) translate(115.0px) rotate(-216.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 500}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:color-mix(in srgb, var(--slide-bg) 90%, transparent); border:2px solid color-mix(in srgb, var(--accent-primary) 55%, transparent); border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px color-mix(in srgb, var(--accent-primary) 30%, transparent); pointer-events:auto; backdrop-filter:blur(10px);">
    4. Cloud finds the video
  </div>
</div>

<div style="position:absolute; left:50%; top:50%; transform:rotate(288.0deg) translate(115.0px) rotate(-288.0deg); pointer-events:none; z-index:10;">
  <div v-click v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 600}}' 
       style="width:90px; height:90px; margin-left:-45.0px; margin-top:-45.0px; background:color-mix(in srgb, var(--slide-bg) 90%, transparent); border:2px solid color-mix(in srgb, var(--accent-primary) 40%, transparent); border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px color-mix(in srgb, var(--accent-primary) 30%, transparent); pointer-events:auto; backdrop-filter:blur(10px);">
    5. Beams it back to you
  </div>
</div>

  </div>
</div>



---
layout: default
class: style-school
style: |

  --slide-bg: #FEF08A;
  --slide-text: #1A1F5E;
  --accent-primary: #3B82F6;
  --accent-secondary: #3B82F6;
  --accent-tertiary: #3B82F6;
  --font-base: 'Outfit', 'Comic Sans MS', sans-serif;

---
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;900&display=swap" rel="stylesheet">
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden">
  <div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div>
  <div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div>
  <div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div>
</div>


<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div style="display: flex; width: 100%; height: 100%; gap: 3rem;">
    <div style="flex: 1.2; display: flex; flex-direction: column;">
      <div style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">FUN FACT</div>
      <h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Giant Data Centers</h1>
      <div style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">These warehouses are called Data Centers. They are so big that people ride scooters inside them!</div>
      <div v-click style="margin-top: auto; padding: 1.5rem; background: color-mix(in srgb, var(--slide-text) 5%, transparent); border-radius: 8px; border-left: 4px solid var(--accent-primary, cyan);">
        <span style="font-weight: 900; font-size: 0.8rem; opacity: 0.5;">CASE HIGHLIGHT</span><br/>
        <div style="font-size: 1.1rem; font-weight: 700; margin-top: 0.5rem;">Size of the Cloud</div>
      </div>
    </div>
    <div v-click style="flex: 0.8; background: color-mix(in srgb, var(--slide-text) 3%, transparent); border-radius: 12px; border: 1px dashed color-mix(in srgb, var(--slide-text) 10%, transparent); display: flex; align-items: center; justify-content: center; padding: 2rem;">
      <div style="text-align: center;">
         <div style="font-size: 5rem; margin-bottom: 1rem;">🏢</div>
         <div style="font-weight: 900; letter-spacing: 2px;">10,000+</div>
         <div style="opacity: 0.6; font-size: 0.9rem;">Servers in one building</div>
      </div>
    </div>
  </div>
</div>



---
layout: center
class: style-school
style: |

  --slide-bg: #F3F4F6;
  --slide-text: #1A1F5E;
  --accent-primary: #3B82F6;
  --accent-secondary: #3B82F6;
  --accent-tertiary: #3B82F6;
  --font-base: 'Outfit', 'Comic Sans MS', sans-serif;

---
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;900&display=swap" rel="stylesheet">
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden">
  <div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div>
  <div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div>
  <div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div>
</div>


<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; justify-content: center; align-items: center; text-align: center; pointer-events:none;">
  <div style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto; background: rgba(255,0,0,0.2); border-color: rgba(255,0,0,0.5); color: #ff9999;">ACTIVITY BREAK</div>
  <div style="font-size: 4rem; margin-bottom: 1rem;">🎮</div>
  <h1 style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">Rent-a-Supercomputer</h1>
  <div v-click style="background: rgba(255,255,255,0.07); padding: 1rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); width: 100%; overflow: hidden; pointer-events: auto; max-width: 70%; margin: 2rem auto; font-size: 1.5rem; font-weight: 700;">
    If you could rent a supercomputer for 1 hour, what game would you play or what world would you build?
  </div>
</div>



---
layout: default
class: style-school
style: |

  --slide-bg: #FFFFFF;
  --slide-text: #1A1F5E;
  --accent-primary: #3B82F6;
  --accent-secondary: #3B82F6;
  --accent-tertiary: #3B82F6;
  --font-base: 'Outfit', 'Comic Sans MS', sans-serif;

---
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;900&display=swap" rel="stylesheet">
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden">
  <div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div>
  <div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div>
  <div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div>
</div>


<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;">
  <div style="display: flex; width: 100%; height: 100%; gap: 3rem;">
    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center;">
      <div v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 0}}' style="display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;">INSIDE LOOK</div>
      <h1 v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 100}}' style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; ">Inside a Data Center</h1>
      <div v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 200}}' style="font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; ">This is what the 'Cloud' actually looks like. Thousands of blinking lights and giant cooling fans!</div>
      <a href="#" v-motion :initial='{"opacity": 0, "y": 20}' :enter='{"opacity": 1, "y": 0, "transition": {"duration": 800, "delay": 300}}' style="margin-top: 2rem; padding: 1rem 2rem; background: var(--accent-primary); color: var(--slide-bg); font-weight: 900; text-decoration: none; border-radius: 50px; width: fit-content;">Look around!</a>
    </div>
    <div v-motion :initial="{opacity:0, x:50}" :enter="{opacity:1, x:0}" style="flex: 1.2; padding: 1rem;"><iframe src='https://www.youtube.com/embed/XZmGGAbHqa0?controls=1&rel=0' style='width: 100%; height: 100%; border: none; border-radius: 12px;'></iframe></div>
  </div>
</div>



---
layout: center
class: style-school
style: |

  --slide-bg: #FEF08A;
  --slide-text: #1A1F5E;
  --accent-primary: #3B82F6;
  --accent-secondary: #3B82F6;
  --accent-tertiary: #3B82F6;
  --font-base: 'Outfit', 'Comic Sans MS', sans-serif;

---
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;900&display=swap" rel="stylesheet">
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />

<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden">
  <div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div>
  <div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div>
  <div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div>
</div>


<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']">
  </div>
</div>


<div style="position:relative; z-index:10; height:100%; display:flex; flex-direction:column; justify-content: center; align-items: center; text-align: center; pointer-events:none;">
  <h1 v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 0}}' style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; text-align: center;">You Are A Cloud Master! ⚡</h1>
  <div v-motion :initial='{"opacity": 0, "y": 50, "scale": 0.9}' :enter='{"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15, "delay": 100}}' style="font-size: 1.5rem; opacity: 0.8;">Next time you watch YouTube, remember the giant warehouses doing all the hard work.</div>
</div>

