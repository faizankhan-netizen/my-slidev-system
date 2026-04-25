<template>
  <div :style="{ width: width, height: height }">
    <v-chart class="chart" :option="option" autoresize />
  </div>
</template>

<script setup>
import { provide } from 'vue'
import VChart, { THEME_KEY } from 'vue-echarts'
import * as echarts from 'echarts/core'
import { BarChart, LineChart, PieChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent, GridComponent, DatasetComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'

// Register the required ECharts components
echarts.use([
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DatasetComponent,
  BarChart,
  LineChart,
  PieChart,
  CanvasRenderer
])

const props = defineProps({
  option: {
    type: Object,
    required: true
  },
  width: {
    type: String,
    default: '100%'
  },
  height: {
    type: String,
    default: '300px'
  },
  theme: {
    type: String,
    default: 'light' // can be 'dark' or 'light'
  }
})

// Provide theme for the chart
provide(THEME_KEY, props.theme)
</script>

<style scoped>
.chart {
  width: 100%;
  height: 100%;
}
</style>
