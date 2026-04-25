<template>
  <div class="slidev-layout" :class="$frontmatter.class">
    <div class="content-wrapper" style="width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center;">
      <div style="display:flex; align-items:center; gap:3rem;">
        <div style="flex:1.2">
          <CategoryPill v-if="$frontmatter.pill">{{ $frontmatter.pill }}</CategoryPill>
          <div v-if="$frontmatter.title" 
               v-motion
               :initial="{ opacity: 0, x: -30 }"
               :enter="{ opacity: 1, x: 0, transition: { type: 'spring', stiffness: 200, damping: 20, delay: 100 } }"
               style="font-size:3.5rem;font-weight:900;line-height:1.1;letter-spacing:-0.03em; margin-bottom:1rem; color:hsl(var(--text-main))">
            {{ $frontmatter.title }}
          </div>
          <div v-if="$frontmatter.subtitle" 
               v-motion
               :initial="{ opacity: 0, x: -30 }"
               :enter="{ opacity: 1, x: 0, transition: { type: 'spring', stiffness: 200, damping: 20, delay: 200 } }"
               style="font-size:1.6rem;font-weight:700;margin-bottom:2rem; color:hsl(var(--text-main) / 0.7)">
            {{ $frontmatter.subtitle }}
          </div>
          <slot name="default" />
        </div>
        <div style="flex:0.8;"
             v-motion
             :initial="{ opacity: 0, scale: 0.95 }"
             :enter="{ opacity: 1, scale: 1, transition: { type: 'spring', stiffness: 150, damping: 25, delay: 300 } }">
          <slot name="right" />
        </div>
      </div>
    </div>
  </div>
</template>
