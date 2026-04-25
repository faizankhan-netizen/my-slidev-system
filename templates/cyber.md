---
layout: split
class: style-cyber
pill: SYSTEM INITIALIZED
title: "The Cyber Archetype"
subtitle: "Terminal Aesthetic for High-Tech Narratives"
---

<!-- 
  CYBER TEMPLATE: 
  Best for technical demos, code logic, and AI research.
-->

<div v-motion :initial="{ opacity:0, x:-20 }" :enter="{ opacity:1, x:0, transition:{ delay:300 } }"
     style="font-size:1.1rem; line-height:1.8; color:hsl(var(--text-main) / 0.75); max-width:430px; margin-top:1.2rem;">
  Welcome to the matrix. This archetype is designed for developers, researchers, and technical visionaries who need a high-contrast, logic-first aesthetic.
</div>

<div v-click style="margin-top:2rem;">
  <code style="color:hsl(var(--accent-tertiary)); font-size:1.2rem;">$ npm install superpower</code>
</div>

::right::
<div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding-left:1rem;">
  <div style="border: 1px solid hsl(var(--border-main) / 0.3); padding: 2rem; border-radius: 4px; background: hsl(var(--bg-card) / 0.5);">
    <carbon:terminal style="font-size:8rem; color:hsl(var(--accent-primary))"/>
  </div>
</div>

---
layout: cards
class: style-cyber
pill: CORE FEATURES
title: "Technical Signatures"
---

<SlideCard v-click title="Terminal Logic" icon="💻" :delay="0">
  Mono-spaced typography (JetBrains Mono) for a code-first reading experience.
</SlideCard>

<SlideCard v-click title="Scanline Depth" icon="📟" :delay="150">
  Animated scanlines and CRT flicker effects create a nostalgic yet futuristic tech layer.
</SlideCard>

<SlideCard v-click title="Glitch Micro-accents" icon="⚡" :delay="300">
  Subtle glitch animations and terminal prompt markers on all headings and pills.
</SlideCard>
