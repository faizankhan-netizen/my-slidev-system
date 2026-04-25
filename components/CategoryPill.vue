<template>
  <span class="pill"
       v-motion
       :initial="{ opacity: 0, y: -20 }"
       :enter="{ opacity: 1, y: 0, transition: { type: 'spring', stiffness: 300, damping: 20 } }">
    <slot></slot>
  </span>
</template>

<style scoped>
.pill {
  display: inline-block;
  padding: 5px 16px;
  font-size: 10px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: 1rem;
}
</style>
