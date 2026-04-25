<script setup lang="ts">
import { useNav } from '@slidev/client'
import { ref, onMounted } from 'vue'

const { next, prev, currentSlideNo, total } = useNav()
const isMobile = ref(false)

onMounted(() => {
  // Detect if device is mobile or small screen
  isMobile.value = window.innerWidth <= 768 || /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
})
</script>

<template>
  <div v-if="isMobile" class="mobile-remote-overlay style-luxury" @click.stop>
    <button @click="isMobile = false" class="mobile-close-icon">×</button>
    <div class="remote-header">
      <div class="pill">MISSION CONTROL ACTIVE</div>
      <div class="slide-indicator">SLIDE {{ currentSlideNo }} / {{ total }}</div>
    </div>

    <div class="control-grid">
      <button @click="prev(); $event.stopPropagation()" class="control-btn prev">
        <carbon:chevron-left class="icon" />
        <span>BACK</span>
      </button>

      <button @click="next(); $event.stopPropagation()" class="control-btn next">
        <span>NEXT</span>
        <carbon:chevron-right class="icon" />
      </button>
    </div>

    <div class="remote-footer">
      <div class="haptic-hint">TAP TO NAVIGATE</div>
    </div>
  </div>
</template>

<style scoped>
.mobile-remote-overlay {
  position: fixed;
  inset: 0;
  z-index: 10000;
  background: hsl(0 0% 5%);
  display: flex;
  flex-direction: column;
  padding: 2rem;
  font-family: 'Cormorant Garamond', serif;
  user-select: none;
}

.mobile-close-icon {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background: transparent;
  border: none;
  color: hsl(0 0% 100% / 0.3);
  font-size: 2.5rem;
  line-height: 1;
  padding: 0.5rem;
  z-index: 10001;
}

.remote-header {
  text-align: center;
  margin-bottom: 2rem;
}

.pill {
  display: inline-block;
  font-size: 10px;
  letter-spacing: 0.3em;
  color: #d4af37;
  border-bottom: 1px solid #d4af37;
  margin-bottom: 1rem;
}

.slide-indicator {
  color: #fff;
  font-size: 1.8rem;
  font-weight: 300;
}

.control-grid {
  flex: 1;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 1.5rem;
}

.control-btn {
  background: hsl(0 0% 10%);
  border: 1px solid hsl(45 40% 50% / 0.2);
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  border-radius: 12px;
  transition: all 0.1s active;
}

.control-btn:active {
  background: #d4af37;
  color: #000;
  transform: scale(0.98);
}

.control-btn .icon {
  font-size: 3rem;
}

.control-btn span {
  font-size: 1.2rem;
  letter-spacing: 0.2em;
  font-weight: 700;
}

.next {
  background: linear-gradient(135deg, hsl(0 0% 12%), hsl(0 0% 8%));
  border-color: hsl(45 60% 55% / 0.4);
}

.remote-footer {
  text-align: center;
  margin-top: 2rem;
  color: hsl(0 0% 100% / 0.3);
  font-size: 0.8rem;
  letter-spacing: 0.1em;
}

.haptic-hint {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}
</style>
