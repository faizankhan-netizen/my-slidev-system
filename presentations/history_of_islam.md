---
theme: default
css: unocss
highlighter: shiki
title: History of Islam
info: |
  A cinematic journey through the History of Islam.
transition: fade
---

<!-- SLIDE 0: PLANNING SNAPSHOT -->
<CategoryPill>PLANNING SNAPSHOT</CategoryPill>
<div style="font-size:1.8rem; font-weight:800; color:var(--text-main); margin-bottom:1.5rem">Strategy & Context</div>
<SlideCard>
  <div style="margin-bottom:1rem">
    <b style="color:var(--text-main)">Target Audience:</b> Students & Academic Audience
  </div>
  <div style="margin-bottom:1rem">
    <b style="color:var(--text-main)">Selected Style:</b> <code style="color:var(--accent-tertiary)">style-business</code>
  </div>
  <div>
    <b style="color:var(--text-main)">Core Motivation:</b> Educate / Document / Preserve
  </div>
</SlideCard>

---
layout: split
class: style-business
pill: HISTORICAL OVERVIEW
title: "History of Islam"
subtitle: "From Revelation to the Golden Age"
---
<!-- SLIDE 1: COVER -->
<div style="font-size:1.1rem; line-height:1.6; color:#64748B; max-width: 450px; margin-top:1rem;">
  Spanning over 1,400 years, the history of Islam is a profound narrative of spiritual revelation, rapid global expansion, and an unparalleled golden age of science, art, and philosophy.
</div>

::right::
<div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
  <img src="/cover_islam.webp" style="width:100%; max-height:400px; object-fit:cover; border-radius:16px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1);" />
</div>

---
layout: cards
class: style-business
pill: DEMOGRAPHICS
title: "Global Impact & Reach"
---
<!-- SLIDE 2: DEMOGRAPHICS -->
<SlideCard v-click stat="1.9B+" title="Global Population" style="flex:1">
  Muslims make up roughly 24% of the global population, spanning diverse cultures from Indonesia to Morocco.
</SlideCard>
<SlideCard v-click stat="1,400+" title="Years of History" style="flex:1" :delay="150">
  A continuous intellectual and spiritual tradition beginning in the 7th century Arabian Peninsula.
</SlideCard>

---
layout: cards
class: style-business
pill: MILESTONES
title: "The Four Major Caliphates"
---
<!-- SLIDE 3: CALIPHATES -->
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem; width:100%">
  <SlideCard v-click title="1. Rashidun" icon="🕌">
    The "Rightly Guided" caliphs who solidified the community post-revelation.
  </SlideCard>
  <SlideCard v-click :delay="100" title="2. Umayyad" icon="⚔️">
    Rapid territorial expansion reaching from Spain to India.
  </SlideCard>
  <SlideCard v-click :delay="200" title="3. Abbasid" icon="📚">
    The architects of the Islamic Golden Age and the House of Wisdom.
  </SlideCard>
  <SlideCard v-click :delay="300" title="4. Ottoman" icon="🏛️">
    A resilient transcontinental empire bridging Europe, Asia, and Africa.
  </SlideCard>
</div>

---
layout: split
class: style-business
pill: THE GOLDEN AGE
title: "Scientific Flourishing"
subtitle: "The House of Wisdom (Bayt al-Hikmah)"
---
<!-- SLIDE 4: THE GOLDEN AGE -->
<div style="font-size:1.1rem; line-height:1.6; color:#64748B; max-width: 450px; margin-top:1rem;">
  During the Abbasid Caliphate, Baghdad became the world's center for intellectual pursuit. Scholars from across the globe gathered to translate classical knowledge and innovate in mathematics, medicine, and astronomy.
</div>

::right::
<div v-click style="background:white; padding:1.5rem; border-radius:12px; border:1px solid #E2E8F0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
  <div style="font-size:0.9rem; font-weight:700; color:#0F172A; text-align:center; margin-bottom:1rem; text-transform:uppercase; letter-spacing:0.05em">Translations & Discoveries (Index)</div>
  <LiveChart :option="{
    grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
    xAxis: { type: 'category', data: ['8th C', '9th C', '10th C', '11th C', '12th C'], boundaryGap: false },
    yAxis: { type: 'value', splitLine: { lineStyle: { type: 'dashed' } } },
    series: [
      {
        name: 'Scientific Output',
        type: 'line',
        smooth: true,
        data: [10, 80, 250, 400, 380],
        itemStyle: { color: '#F97316' },
        areaStyle: {
          color: {
            type: 'linear',
            x: 0, y: 0, x2: 0, y2: 1,
            colorStops: [{ offset: 0, color: 'rgba(249, 115, 22, 0.5)' }, { offset: 1, color: 'rgba(249, 115, 22, 0)' }]
          }
        },
        symbolSize: 8,
        lineStyle: { width: 4 }
      }
    ]
  }" height="300px" />
</div>

---
layout: default
class: style-business
---
<!-- SLIDE 5: CONCLUSION -->
<div style="display:flex; flex-direction:column; align-items:center; justify-content:center; height:100%; text-align:center;">
  <div v-motion :initial="{ opacity:0, scale:0.9 }" :enter="{ opacity:1, scale:1, transition: { type:'spring', damping:15 } }" style="font-size:4rem; font-weight:900; color:#0F172A; letter-spacing:-0.03em; margin-bottom:1rem">
    A Legacy of Innovation
  </div>
  <div v-motion :initial="{ opacity:0, y:20 }" :enter="{ opacity:1, y:0, transition: { delay:200 } }" style="font-size:1.5rem; color:#64748B; max-width:600px">
    The history of Islam is not just a study of the past, but a continuous dialogue that shaped the modern world.
  </div>
</div>
