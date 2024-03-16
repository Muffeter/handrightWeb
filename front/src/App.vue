<script setup lang="ts">
import { ref } from 'vue'
const paramLst = ref([
  { name: 'text', type: 'str', default: 'Hello, world!' },
  { name: 'line_spacing', type: 'int', default: 90 },
  { name: 'fill', type: 'int', default: 0 },
  { name: 'left_margin', type: 'int', default: 30 },
  { name: 'top_margin', type: 'int', default: 0 },
  { name: 'right_margin', type: 'int', default: 30 },
  { name: 'bottom_margin', type: 'int', default: 0 },
  { name: 'word_spacing', type: 'int', default: -10 },
  { name: 'line_spacing_sigma', type: 'int', default: 1 },
  { name: 'font_size_sigma', type: 'int', default: 1 },
  { name: 'word_spacing_sigma', type: 'int', default: 1 },
  { name: 'start_chars', type: 'str', default: '“（[<' },
  { name: 'end_chars', type: 'str', default: '，。' },
  { name: 'perturb_x_sigma', type: 'int', default: 1 },
  { name: 'perturb_y_sigma', type: 'int', default: 1 },
  { name: 'perturb_theta_sigma', type: 'float', default: 0.05 },

])

const colors = [
  "badge-lg-red", "badge-lg-orange", "badge-lg-green", "badge-lg-amber", "badge-lg-yellow", "badge-lg-lime"
  , "badge-lg-red", "badge-lg-orange", "badge-lg-green", "badge-lg-amber", "badge-lg-yellow", "badge-lg-lime"
  , "badge-lg-red", "badge-lg-orange", "badge-lg-green", "badge-lg-amber", "badge-lg-yellow", "badge-lg-lime"
]

</script>

<template>
  <main flex="~ row" m-8>
    <div flex="~ col" justify-center space-y-6>
      <div v-for="(param, index) in paramLst" :class="colors[index]">
        {{ param.name }} :
        <input :key="param.name" :value="param.default" bg-dark input-border rounded>
      </div>
      <button input-border bg-red rounded w32>Generate</button>
    </div>
    <hr>
    <div border border-red>
      to be continued...
    </div>
  </main>
</template>

<style scoped></style>
