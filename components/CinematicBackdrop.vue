<template>
  <div v-if="url" class="absolute inset-0 z-[-1] overflow-hidden">
    <!-- YouTube Embed -->
    <iframe v-if="isYouTube"
      :src="embedUrl"
      class="absolute inset-0 w-full h-full border-none opacity-40"
      :style="{ pointerEvents: showControls ? 'auto' : 'none' }"
      allow="autoplay; encrypted-media"
    ></iframe>
    
    <!-- Direct Video -->
    <video v-else
      :src="url"
      :controls="showControls"
      autoplay loop muted playsinline
      class="absolute inset-0 w-full h-full object-cover opacity-40"
    ></video>

    <!-- Guerrilla GUI -->
    <div class="fixed bottom-12 right-4 z-[100] opacity-0 hover:opacity-100 transition-opacity flex flex-col gap-2 bg-black/90 p-4 border border-white/20 rounded-xl shadow-2xl backdrop-blur-xl">
      <div class="text-[9px] font-black tracking-widest text-cyan-400 uppercase mb-1">Media Commander</div>
      <input 
        :value="url" 
        @input="$emit('update:url', $event.target.value)"
        placeholder="Paste Video/YouTube URL..." 
        class="bg-white/5 border border-white/10 rounded-lg px-3 py-2 text-[10px] text-white w-64 outline-none focus:border-cyan-500 transition-colors" 
      />
      <label class="flex items-center gap-2 text-[10px] text-white/60 uppercase font-bold tracking-wider cursor-pointer hover:text-white mt-1">
        <input type="checkbox" v-model="showControls" class="accent-cyan-500" /> 
        Show Playback Controls
      </label>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  url: String
})

const emit = defineEmits(['update:url'])

const showControls = ref(false)

const isYouTube = computed(() => {
  return props.url && (props.url.includes('youtube.com') || props.url.includes('youtu.be'))
})

const embedUrl = computed(() => {
  if (!isYouTube.value) return ''
  // Robust YouTube ID extraction
  const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/
  const match = props.url.match(regExp)
  const id = (match && match[2].length === 11) ? match[2] : null
  
  if (!id) return ''
  return `https://www.youtube.com/embed/${id}?autoplay=1&mute=1&loop=1&playlist=${id}&controls=${showControls.value ? 1 : 0}&showinfo=0&rel=0&iv_load_policy=3&modestbranding=1`
})
</script>
