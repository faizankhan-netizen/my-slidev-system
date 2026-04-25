---
theme: seriph
background: '#020617'
highlighter: shiki
lineNumbers: false
transition: slide-left
class: style-school
---

<style>
@import './styles/school.css';

/* GLOW ACCENTS */
.slidev-layout.style-school::before {
  content:""; position:absolute; border-radius:50%;
  width:500px; height:500px; top:-200px; right:-200px;
  background: radial-gradient(circle, rgba(139,92,246,0.15) 0%, transparent 70%);
  z-index:0; pointer-events:none;
}
</style>

<!-- SLIDE 0: PLANNING SNAPSHOT (Internal/Strategy) -->
<CategoryPill>PLANNING SNAPSHOT</CategoryPill>
<div style="font-size:2rem; font-weight:900; color:#22D3EE; margin-bottom:1.5rem">Strategy & Context</div>
<SlideCard borderTop="#8B5CF6">
  <div style="margin-bottom:1rem">
    <b style="color:white">Target Audience:</b> [Students / Youth]
  </div>
  <div style="margin-bottom:1rem">
    <b style="color:white">Selected Style:</b> <code style="color:#22D3EE">style-school</code>
  </div>
  <div>
    <b style="color:white">Core Motivation:</b> [Inspire / Learn / Wonder]
  </div>
</SlideCard>

---
layout: split
class: style-school
pill: CATEGORY · TOPIC
title: "[Main Title]"
subtitle: "[Sub-Heading Here]"
---
<!-- SLIDE 1: COVER -->
<div style="font-size:1.05rem;color:#94A3B8;line-height:1.5; max-width:400px">[Brief engaging description for students]</div>

::right::
<div style="border-radius:30px; overflow:hidden; border:1px solid rgba(139,92,246,0.5)">
  <img src="https://images.unsplash.com/photo-1614728263952-84ea206f99b6?w=800" style="width:100%; height:280px; object-fit:cover" />
</div>

---
layout: cards
class: style-school
pill: THE MISSION
title: "[Key Question?]"
---
<!-- SLIDE 2: CORE CONCEPT -->
<SlideCard v-click title="[Point 1]" titleColor="#22D3EE" borderTop="#22D3EE" style="flex:1">
  [Explanation text here]
</SlideCard>
<SlideCard v-click title="[Point 2]" titleColor="#EC4899" borderTop="#EC4899" style="flex:1">
  [Explanation text here]
</SlideCard>
