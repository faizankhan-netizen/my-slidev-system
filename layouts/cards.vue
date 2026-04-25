<template>
  <div class="slidev-layout" :class="$frontmatter.class">
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: flex-start; overflow: hidden;">
      <CategoryPill v-if="$frontmatter.pill">{{ $frontmatter.pill }}</CategoryPill>
      <div v-if="$frontmatter.title" 
           v-motion
           :initial="{ opacity: 0, y: 20 }"
           :enter="{ opacity: 1, y: 0, transition: { type: 'spring', stiffness: 200, damping: 20, delay: 100 } }"
           style="font-size:2.4rem; font-weight:900; letter-spacing:-0.02em; margin-bottom: 1.5rem; color:hsl(var(--text-main))">
        {{ $frontmatter.title }}
      </div>
      <div style="display: flex; gap: 16px; width: 100%; align-items: stretch; flex: 1;">
        <slot />
      </div>
    </div>
  </div>
</template>
