<script setup lang="ts">
const paramLst = [
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

]
</script>

<template>
  <main flex="~ col">
    <div v-for="param in paramLst">
      {{ param.name }} :
      <input :key="param.name" :value="param.default">
    </div>
    <button>Generate</button>
    <div border="~ red">
      to be continued...
    </div>
  </main>
</template>

<style scoped></style>
