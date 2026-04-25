---
layout: split
class: style-luxury
pill: THE VISIONARY
title: "The Luxury Archetype"
subtitle: "Premium Aesthetics for High-Impact Statements"
---

<!-- 
  LUXURY TEMPLATE: 
  Best for keynotes, product launches, luxury brands, and visionary concepts.
-->

<div v-motion :initial="{ opacity:0, y:30 }" :enter="{ opacity:1, y:0, transition:{ delay:300 } }"
     style="font-size:1.4rem; font-style:italic; line-height:1.6; color:hsl(var(--text-main) / 0.8); max-width:480px; margin-top:2rem;">
  True luxury is not about abundance; it is about the precision of choice.
</div>

<div v-click style="margin-top:3rem;">
  <div style="font-size:0.8rem; text-transform:uppercase; letter-spacing:0.4em; color:hsl(var(--accent-primary));">ESTABLISHED 2026</div>
</div>

::right::
<div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding-left:1rem;">
  <div style="position:relative; width:100%; max-width:400px; height:300px; border: 1px solid hsl(var(--border-main) / 0.2); padding: 10px;">
     <img src="https://images.unsplash.com/photo-1550355291-bbee04a92027?auto=format&fit=crop&q=80&w=800" 
          style="width:100%; height:100%; object-fit:cover; filter: grayscale(0.2) contrast(1.1);"/>
  </div>
</div>

---
layout: cards
class: style-luxury
pill: EXCELLENCE DEFINED
title: "Premium Features"
---

<SlideCard v-click title="Midnight Obsidian" icon="💎" :delay="0">
  Deep black backgrounds with gold-dust mesh gradients for an atmospheric, cinematic depth.
</SlideCard>

<SlideCard v-click title="Garamond Serif" icon="✒️" :delay="150">
  Light-weight Cormorant Garamond typography provides a high-contrast, editorial feel.
</SlideCard>

<SlideCard v-click title="Gold Shimmer" icon="✨" :delay="300">
  Animated gold-trim top borders and silk-line background textures create a sense of movement.
</SlideCard>
