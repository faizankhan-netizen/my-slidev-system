<script setup lang="ts">
import { ref, onMounted } from 'vue'

const props = defineProps({
  ip: { type: String, default: '127.0.0.1' },
  port: { type: Number, default: 3030 }
})

const visible = ref(false)
const remoteUrl = `http://${props.ip}:${props.port}/entry/`
const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=${encodeURIComponent(remoteUrl)}`

// Listen for Ctrl+R to toggle the remote portal
onMounted(() => {
  window.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'r') {
      visible.value = !visible.value
      e.preventDefault()
    }
  })
})
</script>

<template>
  <Teleport to="body">
    <Transition name="fade-scale">
      <div v-if="visible" class="remote-portal-overlay" @click="visible = false">
        <div class="remote-portal-card style-luxury" @click.stop>
          <button @click="visible = false" class="portal-close-icon">×</button>
          <div class="pill">REMOTE CONTROL INITIALIZED</div>
          <h2>Mission Control</h2>
          <p class="subtitle">Scan to sync your mobile device</p>
          
          <div class="qr-container">
            <img :src="qrUrl" alt="Remote QR Code" class="qr-image" />
            <div class="qr-corner-tl"></div>
            <div class="qr-corner-tr"></div>
            <div class="qr-corner-bl"></div>
            <div class="qr-corner-br"></div>
          </div>

          <div class="connection-details">
            <div class="url-box">
              <span class="label">URL</span>
              <span class="value">{{ remoteUrl }}</span>
            </div>
            <div class="status-box">
              <div class="status-dot pulsing"></div>
              <span>SERVER ACTIVE</span>
            </div>
          </div>

          <div class="instructions">
            <p>1. Ensure both devices are on the same WiFi.</p>
            <p>2. Scan the code to open the presentation on mobile.</p>
            <p>3. Navigation will be perfectly synced.</p>
          </div>

          <button @click="visible = false" class="close-btn">
            DISMISS CONTROL
          </button>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.remote-portal-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background: hsl(0 0% 0% / 0.85);
  backdrop-filter: blur(20px);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Cormorant Garamond', serif;
}

.remote-portal-card {
  width: 420px;
  background: hsl(0 0% 5% / 0.95);
  border: 1px solid hsl(45 40% 50% / 0.3);
  padding: 2.5rem;
  text-align: center;
  position: relative;
  box-shadow: 0 40px 100px hsl(0 0% 0% / 0.8);
}

.portal-close-icon {
  position: absolute;
  top: 1rem;
  right: 1.2rem;
  background: transparent;
  border: none;
  color: hsl(0 0% 100% / 0.2);
  font-size: 2rem;
  line-height: 1;
  cursor: pointer;
  z-index: 100;
  transition: color 0.2s;
}

.portal-close-icon:hover {
  color: #d4af37;
}

.remote-portal-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #d4af37, transparent);
}

.pill {
  display: inline-block;
  font-size: 10px;
  letter-spacing: 0.2em;
  color: #d4af37;
  border-bottom: 1px solid #d4af37;
  margin-bottom: 1rem;
}

h2 {
  font-size: 2.2rem;
  margin: 0;
  color: #fff;
  font-weight: 300;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.subtitle {
  color: hsl(0 0% 100% / 0.5);
  font-size: 1rem;
  margin-bottom: 2rem;
}

.qr-container {
  position: relative;
  width: 250px;
  height: 250px;
  margin: 0 auto 2rem;
  padding: 15px;
  background: #fff;
  border-radius: 4px;
}

.qr-image {
  width: 100%;
  height: 100%;
}

[class^="qr-corner-"] {
  position: absolute;
  width: 30px;
  height: 30px;
  border: 2px solid #d4af37;
}

.qr-corner-tl { top: -10px; left: -10px; border-right: none; border-bottom: none; }
.qr-corner-tr { top: -10px; right: -10px; border-left: none; border-bottom: none; }
.qr-corner-bl { bottom: -10px; left: -10px; border-right: none; border-top: none; }
.qr-corner-br { bottom: -10px; right: -10px; border-left: none; border-top: none; }

.connection-details {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2rem;
}

.url-box {
  background: hsl(0 0% 100% / 0.05);
  padding: 0.8rem;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  font-family: monospace;
  font-size: 0.9rem;
}

.url-box .label { color: #d4af37; font-weight: bold; }
.url-box .value { color: #fff; }

.status-box {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  color: hsl(0 0% 100% / 0.6);
}

.status-dot {
  width: 8px;
  height: 8px;
  background: #00ff88;
  border-radius: 50%;
}

.pulsing {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.7); }
  70% { box-shadow: 0 0 0 10px rgba(0, 255, 136, 0); }
  100% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0); }
}

.instructions {
  text-align: left;
  font-size: 0.85rem;
  color: hsl(0 0% 100% / 0.4);
  line-height: 1.6;
  margin-bottom: 2rem;
}

.close-btn {
  background: transparent;
  border: 1px solid hsl(0 0% 100% / 0.2);
  color: #fff;
  padding: 0.8rem 2rem;
  cursor: pointer;
  letter-spacing: 0.1em;
  transition: all 0.2s;
}

.close-btn:hover {
  background: #d4af37;
  color: #000;
  border-color: #d4af37;
}

.fade-scale-enter-active, .fade-scale-leave-active {
  transition: all 0.3s ease;
}
.fade-scale-enter-from, .fade-scale-leave-to {
  opacity: 0;
  transform: scale(0.95);
}
</style>
