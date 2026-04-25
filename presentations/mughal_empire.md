---
theme: default
css: unocss
highlighter: shiki
title: The Mughal Empire
info: |
  A cinematic journey through the Mughal Empire — from Babur's conquest to Aurangzeb's zenith.
transition: fade
---

<!-- ============================================================ -->
<!-- SLIDE 0: PLANNING SNAPSHOT (Internal — not presented)        -->
<!-- ============================================================ -->
<CategoryPill>PLANNING SNAPSHOT</CategoryPill>
<div style="font-size:1.8rem; font-weight:800; color:hsl(var(--text-main)); margin-bottom:1.5rem">Strategy & Context</div>
<SlideCard>
  <div style="margin-bottom:1rem"><b style="color:hsl(var(--text-main))">Audience:</b> Students, History Enthusiasts</div>
  <div style="margin-bottom:1rem"><b style="color:hsl(var(--text-main))">Style:</b> <code style="color:hsl(var(--accent-primary))">style-school</code> — Neon Cosmos</div>
  <div><b style="color:hsl(var(--text-main))">Goal:</b> Educate · Inspire · Showcase new engine features</div>
</SlideCard>

---
layout: split
class: style-school
pill: 1526 – 1857 CE
title: "The Mughal Empire"
subtitle: "From Kabul to the Deccan"
---

<!-- ============================================================ -->
<!-- SLIDE 1: CINEMATIC COVER                                     -->
<!-- Tests: split layout, v-motion, generated WebP, HSL text      -->
<!-- ============================================================ -->

<div v-motion :initial="{ opacity:0, y:20 }" :enter="{ opacity:1, y:0, transition:{ delay:300 } }"
     style="font-size:1.1rem; line-height:1.8; color:hsl(var(--text-main) / 0.75); max-width:430px; margin-top:1.2rem;">
  For over three centuries, the Mughals forged one of the largest and wealthiest empires in human history — uniting diverse peoples under a legacy of art, architecture, and philosophy that still defines South Asia today.
</div>

::right::
<div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding-left:1rem;">
  <img src="/cover_mughals.webp"
       style="width:100%; max-height:420px; object-fit:cover; border-radius:20px;
              box-shadow: 0 25px 60px hsl(0 0% 0% / 0.5), 0 0 0 1px hsl(0 0% 100% / 0.08);"/>
</div>

---
layout: cards
class: style-school
pill: THE SIX GREATS
title: "The Grand Emperors"
---

<!-- ============================================================ -->
<!-- SLIDE 2: SIX EMPERORS — 2×3 GRID                            -->
<!-- Tests: cards layout, staggered :delay prop, glassmorphism    -->
<!-- ============================================================ -->

<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.8rem; width:100%;">
  <SlideCard v-click title="Babur" icon="⚔️" :delay="0">
    1526 · Founded the empire at Panipat
  </SlideCard>
  <SlideCard v-click title="Humayun" icon="🌙" :delay="80">
    1555 · Reclaimed the throne from exile
  </SlideCard>
  <SlideCard v-click title="Akbar" icon="🌟" :delay="160">
    1556 · Architect of a unified empire
  </SlideCard>
  <SlideCard v-click title="Jahangir" icon="🎨" :delay="240">
    1605 · Patron of Mughal miniature art
  </SlideCard>
  <SlideCard v-click title="Shah Jahan" icon="🕌" :delay="320">
    1627 · Builder of the Taj Mahal
  </SlideCard>
  <SlideCard v-click title="Aurangzeb" icon="🗺️" :delay="400">
    1658 · Greatest territorial extent
  </SlideCard>
</div>

---
layout: split
class: style-school
pill: TERRITORIAL EXPANSION
title: "An Empire of Scale"
subtitle: "Territorial growth across three centuries"
---

<!-- ============================================================ -->
<!-- SLIDE 3: LIVECHART — DYNAMIC EXPANSION GRAPH                 -->
<!-- Tests: LiveChart, split layout, HSL dynamic opacity shadow   -->
<!-- ============================================================ -->

<div v-motion :initial="{ opacity:0, y:15 }" :enter="{ opacity:1, y:0, transition:{ delay:350 } }"
     style="margin-top:1rem; font-size:1.05rem; line-height:1.8; color:hsl(var(--text-main) / 0.7); max-width:400px">
  At its peak under Aurangzeb, the empire stretched across 4 million km² — home to over 150 million people and generating nearly 25% of global GDP.
</div>

::right::
<div v-click style="border-radius:16px; overflow:hidden; box-shadow: 0 20px 50px hsl(0 0% 0% / 0.4); border: 1px solid hsl(0 0% 100% / 0.1);">
  <LiveChart :option="{
    backgroundColor: 'transparent',
    grid: { left:'5%', right:'5%', bottom:'8%', top:'10%', containLabel:true },
    tooltip: { trigger:'axis', backgroundColor:'rgba(0,0,0,0.7)', borderColor:'rgba(255,255,255,0.1)', textStyle:{ color:'#fff' } },
    xAxis: {
      type: 'category',
      data: ['Babur\n1526','Humayun\n1555','Akbar\n1600','Jahangir\n1627','Shah Jahan\n1650','Aurangzeb\n1700'],
      axisLabel: { color:'rgba(255,255,255,0.6)', fontSize:9 },
      axisLine: { lineStyle: { color:'rgba(255,255,255,0.15)' } }
    },
    yAxis: {
      type: 'value',
      name: 'Million km²',
      nameTextStyle: { color:'rgba(255,255,255,0.4)', fontSize:9 },
      axisLabel: { color:'rgba(255,255,255,0.5)', fontSize:9 },
      splitLine: { lineStyle: { color:'rgba(255,255,255,0.07)', type:'dashed' } }
    },
    series: [{
      type: 'line',
      smooth: true,
      data: [0.9, 0.8, 3.0, 3.4, 3.5, 4.0],
      itemStyle: { color:'#22D3EE' },
      lineStyle: { width:3, color:'#22D3EE' },
      areaStyle: {
        color: { type:'linear', x:0, y:0, x2:0, y2:1,
          colorStops:[{ offset:0, color:'rgba(34,211,238,0.35)' },{ offset:1, color:'rgba(34,211,238,0.02)' }]
        }
      },
      symbolSize: 9,
      label: { show:false }
    }]
  }" height="280px" />
</div>

---
layout: cards
class: style-school
pill: CULTURAL LEGACY
title: "Arts, Architecture & Intellect"
---

<!-- ============================================================ -->
<!-- SLIDE 4: CULTURAL LEGACY                                     -->
<!-- Tests: cards layout, semantic HSL tokens, no hardcoded hex   -->
<!-- ============================================================ -->

<SlideCard v-click title="Architecture" icon="🏛️" :delay="0">
  Taj Mahal, Red Fort, Fatehpur Sikri — defining monuments of world heritage still standing today.
</SlideCard>
<SlideCard v-click title="Miniature Art" icon="🖌️" :delay="120">
  Jahangir's court elevated painting to an imperial art form — portraits of startling realism and botanical precision.
</SlideCard>
<SlideCard v-click title="Din-i-Ilahi" icon="☯️" :delay="240">
  Akbar's syncretic philosophy blending Islam, Hinduism, Christianity & Zoroastrianism into a universal court culture.
</SlideCard>

---
layout: cards
class: style-school
pill: ECONOMIC POWER
title: "The Wealthiest Empire on Earth"
---

<!-- ============================================================ -->
<!-- SLIDE 5: KPI STATS                                          -->
<!-- Tests: stat prop on SlideCard, HSL-powered stat colour       -->
<!-- ============================================================ -->

<SlideCard v-click stat="25%" title="of Global GDP" :delay="0">
  At peak, Mughal India produced a quarter of total world economic output — surpassing all of Western Europe combined.
</SlideCard>
<SlideCard v-click stat="150M" title="Population" :delay="150">
  The empire governed an estimated 150 million subjects — the largest ruled population of the 17th century.
</SlideCard>
<SlideCard v-click stat="4M km²" title="Territory" :delay="300">
  From Kabul in the north-west to Bengal in the east, and the Deccan plateau in the south.
</SlideCard>

---
layout: default
class: style-school
---

<!-- ============================================================ -->
<!-- SLIDE 6: CINEMATIC CONCLUSION                                -->
<!-- Tests: v-motion spring scale, hsl opacity subtitle           -->
<!-- ============================================================ -->

<div style="display:flex; flex-direction:column; align-items:center; justify-content:center; height:100%; text-align:center;">
  <div v-motion
       :initial="{ opacity:0, scale:0.85 }"
       :enter="{ opacity:1, scale:1, transition:{ type:'spring', stiffness:180, damping:14 } }"
       style="font-size:3.8rem; font-weight:900; color:hsl(var(--accent-primary));
              letter-spacing:-0.03em; margin-bottom:1.2rem;
              text-shadow: 0 0 60px hsl(var(--accent-primary) / 0.35);">
    "A River of Dynasties"
  </div>
  <div v-motion
       :initial="{ opacity:0, y:20 }"
       :enter="{ opacity:1, y:0, transition:{ type:'spring', delay:200 } }"
       style="font-size:1.4rem; color:hsl(var(--text-main) / 0.65); max-width:580px; line-height:1.7;">
    The Mughals did not merely rule — they synthesised. Their empire remains the most vivid proof that civilisations reach their zenith when they dare to borrow from one another.
  </div>
  <div v-motion
       :initial="{ opacity:0 }"
       :enter="{ opacity:1, transition:{ delay:500 } }"
       style="margin-top:2.5rem; display:flex; gap:2rem;">
    <div style="text-align:center;">
      <div style="font-size:1.8rem; font-weight:900; color:hsl(var(--accent-secondary));">331</div>
      <div style="font-size:0.8rem; color:hsl(var(--text-main) / 0.5); text-transform:uppercase; letter-spacing:0.1em">Years</div>
    </div>
    <div style="width:1px; background:hsl(var(--text-main) / 0.1);"></div>
    <div style="text-align:center;">
      <div style="font-size:1.8rem; font-weight:900; color:hsl(var(--accent-secondary));">19</div>
      <div style="font-size:0.8rem; color:hsl(var(--text-main) / 0.5); text-transform:uppercase; letter-spacing:0.1em">Emperors</div>
    </div>
    <div style="width:1px; background:hsl(var(--text-main) / 0.1);"></div>
    <div style="text-align:center;">
      <div style="font-size:1.8rem; font-weight:900; color:hsl(var(--accent-secondary));">1526</div>
      <div style="font-size:0.8rem; color:hsl(var(--text-main) / 0.5); text-transform:uppercase; letter-spacing:0.1em">Founded</div>
    </div>
  </div>
</div>
