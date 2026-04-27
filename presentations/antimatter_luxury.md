---
theme: seriph
background: '#050505'
highlighter: shiki
lineNumbers: false
transition: fade
title: Antimatter — The Ultimate Luxury
canvasWidth: 900
---

<style>
/* LUXURY THEME OVERRIDES */
.slidev-layout {
  background: radial-gradient(circle at 0% 0%, hsl(45 60% 55% / 0.05) 0%, transparent 50%),
              radial-gradient(circle at 100% 100%, hsl(45 30% 20% / 0.1) 0%, transparent 50%),
              #050505 !important;
  color: #f5f5f0 !important;
  font-family: 'Cormorant Garamond', serif !important;
  padding: 4rem !important;
}

.luxury-title {
  font-family: 'Cormorant Garamond', serif;
  font-weight: 300;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #D4AF37;
}

.luxury-card {
  background: rgba(20, 20, 20, 0.6);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(212, 175, 55, 0.2);
  padding: 2rem;
  border-radius: 4px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  position: relative;
  overflow: hidden;
}

.luxury-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; width: 100%; height: 1px;
  background: linear-gradient(90deg, transparent, #D4AF37, transparent);
}

.gold-text {
  color: #D4AF37;
}

.pill {
  display: inline-block;
  border-bottom: 1px solid rgba(212, 175, 55, 0.5);
  padding: 4px 0;
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: #D4AF37;
  margin-bottom: 2rem;
}

.stat-giant {
  font-size: 5rem;
  font-weight: 300;
  color: #D4AF37;
  line-height: 1;
}
</style>

<!-- SLIDE 1: COVER -->
<div class="flex flex-col h-full justify-center">
  <div class="grid grid-cols-2 gap-12 items-center">
    <div>
      <div class="pill">The rarest substance in existence</div>
      <h1 class="luxury-title text-6xl leading-tight mb-6">Antimatter.</h1>
      <p class="text-xl italic opacity-80 mb-8">The Mirror of Creation and the Peak of Cosmic Engineering.</p>
      <div class="h-px w-24 bg-gold-500 opacity-50 mb-8"></div>
      <p class="text-sm tracking-widest uppercase opacity-60">A Visionary Exploration</p>
    </div>
    <div class="relative">
      <div class="absolute -inset-4 border border-gold-500/20 rounded-lg"></div>
      <img src="/antimatter_luxury.png" class="rounded shadow-2xl relative z-10 w-full" />
    </div>
  </div>
</div>

---
layout: default
---
<!-- SLIDE 2: THE CONCEPT -->
<div class="pill">The Mirror Principle</div>
<h2 class="luxury-title text-4xl mb-12">The Symmetry of Existence</h2>

<div class="grid grid-cols-2 gap-12">
  <div v-click class="luxury-card">
    <h3 class="gold-text text-2xl mb-4">Cosmic Reflection</h3>
    <p class="opacity-80 leading-relaxed">For every particle of matter that builds our world, there exists an antimatter twin—identical in mass but opposite in charge.</p>
  </div>
  <div v-click class="luxury-card">
    <h3 class="gold-text text-2xl mb-4">Total Annihilation</h3>
    <p class="opacity-80 leading-relaxed">When matter meets its mirror, they vanish in a flash of pure, perfect energy. It is the most efficient reaction known to physics.</p>
  </div>
</div>

<div v-click class="mt-12 text-center italic opacity-60">
  "The universe is not only stranger than we imagine, it is stranger than we can imagine."
</div>

---
layout: default
---
<!-- SLIDE 3: MEDICAL APPLICATION -->
<div class="pill">Precision Medicine</div>
<h2 class="luxury-title text-4xl mb-12">The Healing Flash</h2>

<div class="flex gap-12 items-center">
  <div class="flex-1">
    <div v-click class="mb-8">
      <h3 class="gold-text text-xl mb-2">Positron Emission Tomography</h3>
      <p class="opacity-70">Antimatter particles (positrons) are used every day in hospitals to detect cancer with unparalleled precision.</p>
    </div>
    <div v-click class="mb-8 border-l-2 border-gold-500/30 pl-6">
      <h3 class="text-lg mb-2">Molecular Insight</h3>
      <p class="opacity-70 text-sm">By tracking antimatter annihilation inside the body, doctors can visualize metabolic processes in real-time.</p>
    </div>
  </div>
  <div v-click class="flex-1 luxury-card text-center">
    <div class="stat-giant mb-4">PET</div>
    <p class="uppercase tracking-tighter opacity-50">Standard of Excellence</p>
  </div>
</div>

---
layout: default
---
<!-- SLIDE 4: PROPULSION -->
<div class="pill">Interstellar Voyage</div>
<h2 class="luxury-title text-4xl mb-12">The Fuel of the Gods</h2>

<div class="grid grid-cols-3 gap-6">
  <div v-click class="luxury-card">
    <div class="text-3xl mb-4">🚀</div>
    <h4 class="gold-text mb-2">Ultimate Density</h4>
    <p class="text-xs opacity-70">1,000 times more powerful than nuclear fission.</p>
  </div>
  <div v-click class="luxury-card">
    <div class="text-3xl mb-4">🌌</div>
    <h4 class="gold-text mb-2">Mars in Weeks</h4>
    <p class="text-xs opacity-70">Reducing travel time to months, not years.</p>
  </div>
  <div v-click class="luxury-card">
    <div class="text-3xl mb-4">✨</div>
    <h4 class="gold-text mb-2">Clean Energy</h4>
    <p class="text-xs opacity-70">Zero waste. Only pure light remain.</p>
  </div>
</div>

<div v-click class="mt-12 p-6 border border-gold-500/10 bg-gold-500/5 rounded">
  <p class="text-center italic text-lg gold-text">"Antimatter is the key to unlocking the stars."</p>
</div>

---
layout: default
---
<!-- SLIDE 5: THE COST -->
<div class="pill">Exclusivity Defined</div>
<h2 class="luxury-title text-4xl mb-12">The $62 Trillion Gram</h2>

<div class="flex flex-col items-center justify-center h-48">
  <div v-click class="stat-giant">$62.5T</div>
  <div v-click class="uppercase tracking-widest text-sm opacity-60 mt-4">Per Single Gram</div>
</div>

<div class="grid grid-cols-2 gap-12 mt-12">
  <div v-click>
    <p class="opacity-80">Producing just <span class="gold-text">one gram</span> would take the entire world's energy production for a year.</p>
  </div>
  <div v-click>
    <p class="opacity-80">It is preserved in magnetic traps—suspended in a vacuum to prevent it from ever touching reality.</p>
  </div>
</div>

---
layout: default
---
<!-- SLIDE 6: CONCLUSION -->
<div class="flex flex-col h-full justify-center items-center text-center">
  <div class="pill">The Grand Finale</div>
  <h2 class="luxury-title text-6xl mb-8">The Future is Rare.</h2>
  <div class="w-32 h-px bg-gold-500 mb-8"></div>
  <p class="text-2xl italic max-w-2xl opacity-80 leading-relaxed">
    Antimatter is not just a fuel or a medical tool. It is the signature of the universe's most profound secret—a reminder that for every light, there is a shadow.
  </p>
  <div v-click class="mt-16 luxury-card inline-block">
    <p class="gold-text uppercase tracking-widest text-xs">Thank You for Your Time</p>
  </div>
</div>
