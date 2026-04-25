---
theme: seriph
background: '#F8FAFC'
highlighter: shiki
lineNumbers: false
transition: slide-left
class: style-business
---

<style>
@import './styles/business.css';
</style>

<!-- SLIDE 0: PLANNING SNAPSHOT (Internal/Strategy) -->
<CategoryPill>PLANNING SNAPSHOT</CategoryPill>
<div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin-bottom:1.5rem">Strategy & Context</div>
<SlideCard>
  <div style="margin-bottom:1rem">
    <b style="color:var(--text-main)">Target Audience:</b> [Executive / Investor]
  </div>
  <div style="margin-bottom:1rem">
    <b style="color:var(--text-main)">Selected Style:</b> <code style="color:var(--accent-tertiary)">style-business</code>
  </div>
  <div>
    <b style="color:var(--text-main)">Core Motivation:</b> [Decide / ROI / Growth]
  </div>
</SlideCard>

---
layout: split
class: style-business
pill: STRATEGIC BRIEF · 2026
title: "[Business Topic]"
subtitle: "[Operational Overview & ROI Projections]"
---
<!-- SLIDE 1: CORPORATE COVER -->

::right::
<div style="display:flex; gap:2rem; padding-left:2.3rem; margin-top: 5rem;">
  <div style="border-right:1px solid #CBD5E1; padding-right:2rem">
    <div style="font-size:0.8rem; color:#94A3B8; text-transform:uppercase">Project Lead</div>
    <div style="font-size:1.1rem; font-weight:700; color:#0F172A">[Name]</div>
  </div>
  <div>
    <div style="font-size:0.8rem; color:#94A3B8; text-transform:uppercase">Status</div>
    <div style="font-size:1.1rem; font-weight:700; color:#059669">ACTIVE</div>
  </div>
</div>

---
layout: cards
class: style-business
pill: DATA INSIGHTS
title: Executive Summary
---
<!-- SLIDE 2: DATA SNAPSHOT -->
<SlideCard v-click stat="[85%]" title="[KPI Title]" style="flex:1">
  [Business impact and rationale text goes here]
</SlideCard>
<SlideCard v-click stat="[₹12M]" title="[Financial Goal]" style="flex:1">
  [Budget allocation and ROI projections]
</SlideCard>

---
class: style-business
---
<!-- SLIDE 3: DYNAMIC VISUALIZATION -->
<div class="content-wrapper">
  <CategoryPill>PROJECTIONS</CategoryPill>
  <div style="font-size:2.8rem;font-weight:800;color:#0F172A;letter-spacing:-0.02em; margin-bottom: 1rem;">Revenue Growth</div>
  
  <div v-click style="background:white; padding:1.5rem; border-radius:12px; border:1px solid #E2E8F0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
    <LiveChart :option="{
      grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
      xAxis: { type: 'category', data: ['Q1', 'Q2', 'Q3', 'Q4'] },
      yAxis: { type: 'value' },
      series: [
        {
          name: 'Target',
          type: 'bar',
          data: [120, 200, 150, 280],
          itemStyle: { color: '#1E293B', borderRadius: [4, 4, 0, 0] }
        },
        {
          name: 'Actual',
          type: 'line',
          data: [130, 180, 170, 310],
          itemStyle: { color: '#F97316' },
          symbolSize: 8,
          lineStyle: { width: 3 }
        }
      ]
    }" height="350px" />
  </div>
</div>
