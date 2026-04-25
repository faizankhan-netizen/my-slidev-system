---
layout: split
class: style-eco
pill: SUSTAINABLE VISION
title: "The Eco Archetype"
subtitle: "Organic Aesthetics for Sustainable Storytelling"
---

<!-- 
  ECO TEMPLATE: 
  Best for environmental topics, wellness, agriculture, and organic brands.
-->

<div v-motion :initial="{ opacity:0, y:20 }" :enter="{ opacity:1, y:0, transition:{ delay:300 } }"
     style="font-size:1.1rem; line-height:1.8; color:hsl(var(--text-main) / 0.8); max-width:430px; margin-top:1.2rem;">
  Rooted in nature, this style uses soft sage palettes, organic textures, and tactile glassmorphism to create a calm, grounded experience.
</div>

<div v-click style="margin-top:2.5rem; display:flex; align-items:center; gap:1rem;">
  <carbon:agriculture-analytics style="font-size:2.5rem; color:hsl(var(--accent-primary))"/>
  <span style="font-weight:700; font-size:1.2rem;">Grow with Purpose</span>
</div>

::right::
<div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding-left:1rem;">
  <div style="position:relative; width:100%; max-width:400px; height:300px; border-radius:32px; overflow:hidden; box-shadow: 0 20px 50px hsl(var(--text-main) / 0.1);">
     <img src="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&q=80&w=800" 
          style="width:100%; height:100%; object-fit:cover;"/>
  </div>
</div>

---
layout: cards
class: style-eco
pill: NATURAL DEPTH
title: "Organic Features"
---

<SlideCard v-click title="Tactile Cards" icon="🌱" :delay="0">
  Large-radius rounded corners (24px) and soft shadows for a gentle, approachable feel.
</SlideCard>

<SlideCard v-click title="Serif Elegance" icon="📖" :delay="150">
  Lora serif typography provides an academic yet natural tone for long-form reading.
</SlideCard>

<SlideCard v-click title="Leaf Drift" icon="🍃" :delay="300">
  Subtle leaf animations and organic background blobs keep the slides feeling "alive."
</SlideCard>
