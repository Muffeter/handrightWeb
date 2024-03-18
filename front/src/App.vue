<script setup lang="ts">
import { Ref, ref } from 'vue'

interface Param {
  text: { name: string, value: string },
  line_spacing: { name: string, value: number },
  fill: { name: string, value: number },
  left_margin: { name: string, value: number },
  top_margin: { name: string, value: number },
  right_margin: { name: string, value: number },
  bottom_margin: { name: string, value: number },
  word_spacing: { name: string, value: number },
  line_spacing_sigma: { name: string, value: number },
  font_size_sigma: { name: string, value: number },
  word_spacing_sigma: { name: string, value: number },
  start_chars: { name: string, value: string },
  end_chars: { name: string, value: string },
  perturb_x_sigma: { name: string, value: number },
  perturb_y_sigma: { name: string, value: number },
  perturb_theta_sigma: { name: string, value: number },
  width: { name: string, value: number },
  height: { name: string, value: number },
}

const colors = [
  "badge-lg-red", "badge-lg-orange", "badge-lg-green", "badge-lg-amber", "badge-lg-yellow", "badge-lg-lime"
  , "badge-lg-red", "badge-lg-orange", "badge-lg-green", "badge-lg-amber", "badge-lg-yellow", "badge-lg-lime"
  , "badge-lg-red", "badge-lg-orange", "badge-lg-green", "badge-lg-amber", "badge-lg-yellow", "badge-lg-lime"
]
let defaultParams = ref<Param>({
  text: { name: "text", value: "Hello, World!" },
  line_spacing: { name: "line_spacing", value: 90 },
  fill: { name: "fill", value: 0 },
  left_margin: { name: "left_margin", value: 30 },
  top_margin: { name: "top_margin", value: 0 },
  right_margin: { name: "right_margin", value: 30 },
  bottom_margin: { name: "bottom_margin", value: 0 },
  word_spacing: { name: "word_spacing", value: -10 },
  line_spacing_sigma: { name: "line_spacing_sigma", value: 1 },
  font_size_sigma: { name: "font_size_sigma", value: 1 },
  word_spacing_sigma: { name: "word_spacing_sigma", value: 1 },
  start_chars: { name: "start_chars", value: "“（[<" },
  end_chars: { name: "end_chars", value: "，。" },
  perturb_x_sigma: { name: "perturb_x_sigma", value: 1 },
  perturb_y_sigma: { name: "perturb_y_sigma", value: 1 },
  perturb_theta_sigma: { name: "perturb_theta_sigma", value: 0.05 },
  width: { name: "width", value: 3072 },
  height: { name: "height", value: 3920 },
}
)

const paramsNames = Object.keys(defaultParams.value)
const inputValues: Ref<Param> = ref(defaultParams.value)

const imgUrl = ref('')

function getValue(name: string) {
  return inputValues.value[name].value
}

function updateValue(name: string, value: string) {
  inputValues.value[name].value = value
}

async function previewParams() {
  let url = new URL("http://localhost:5000/api/generate")
  Object.keys(inputValues.value).forEach((key, index) => {
    url.searchParams.append(key, inputValues.value[key].value)
  })
  //get the image from the server http://localhost:5000/api/generate
  const result = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  })
  const blob = await result.blob()
  imgUrl.value = URL.createObjectURL(blob)
}

</script>

<template>
  <main flex="~ row" mx-16 my-16>
    <div flex="~ col nowrap" w-sm justify-center items-start space-y-6>
      <div v-for="(param, index) in paramsNames" :class="colors[index]">
        {{ param }} :
        <input :key="param" :value="getValue(param)" @input="updateValue(param, $event.target.value)" bg-dark input-border
          rounded>
      </div>
      <div flex="~ row nowrap" gap-2>
        <button input-border bg-purple rounded w32 text-white font-bold @click="previewParams">Preview</button>
        <button input-border bg-gray rounded w32 text-black font-bold>Download</button>
      </div>
    </div>
    <hr flex-shrink mx-4 my--4>
    <div basis-a flex justify-center mx-8 object-contain>
      <img v-if="imgUrl" :src="imgUrl" alt="Image" w-full h-full max-w-full max-h-auto object-contain>
    </div>
  </main>
</template>

<style scoped>
</style>
