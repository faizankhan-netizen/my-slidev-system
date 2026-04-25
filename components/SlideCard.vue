<template>
  <div class="card" 
       v-motion
       :initial="{ opacity: 0, y: 40 }"
       :enter="{ opacity: 1, y: 0, transition: { type: 'spring', stiffness: 250, damping: 20, mass: 0.5, delay: delay } }"
       :style="borderTop ? `border-top: 4px solid ${borderTop}` : ''">
    <div v-if="stat" class="stat"
         v-motion
         :initial="{ scale: 0.5, opacity: 0 }"
         :enter="{ scale: 1, opacity: 1, transition: { type: 'spring', stiffness: 300, delay: delay + 100 } }">
      {{ stat }}
    </div>
    <div v-if="icon"
         v-motion
         :initial="{ rotate: -15, opacity: 0 }"
         :enter="{ rotate: 0, opacity: 1, transition: { type: 'spring', stiffness: 200, delay: delay + 150 } }"
         style="font-size:2rem; margin-bottom:0.8rem">
      {{ icon }}
    </div>
    <div v-if="title"
         style="font-size:1.3rem; font-weight:900; margin-bottom:0.5rem"
         :style="{ color: titleColor || 'hsl(var(--text-main))' }">
      {{ title }}
    </div>
    <div style="font-size:0.95rem; opacity:0.8">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title:      { type: String,  default: '' },
  icon:       { type: String,  default: '' },
  stat:       { type: String,  default: '' },
  titleColor: { type: String,  default: '' },
  borderTop:  { type: String,  default: '' },
  delay:      { type: Number,  default: 0  }
})
</script>
