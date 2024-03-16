// uno.config.ts
import { defineConfig, presetAttributify, presetUno } from 'unocss'

export default defineConfig({
  // ...UnoCSS options
  presets: [
    presetUno(),
    presetAttributify()
  ],
  shortcuts: [
    [/^badge-(.*)$/, ([, c]) => `bg-${c}4:10 text-${c}5 rounded`],
    [/^badge-xs-(.*)$/, ([, c]) => `badge-${c} text-xs px2 py0.5`],
    [/^badge-sm-(.*)$/, ([, c]) => `badge-${c} text-sm px3 py0.6`],
    [/^badge-lg-(.*)$/, ([, c]) => `badge-${c} px3 py0.8`],
    [/^badge-square-(.*)$/, ([, c]) => `badge-${c} w-7 h-7 text-lg font-200 flex flex-none items-center justify-center`],
    {
      'border-base': 'border-gray-500:10',
      'bg-base': 'bg-white dark:bg-hex-121212',
      'btn': 'px-4 py-1 inline-block bg-cyan6 hover:bg-cyan7 text-white cursor-pointer disabled:cursor-default disabled:bg-gray-600 disabled:opacity-50',
      'link': 'op50 hover:op100 hover:text-cyan6',
      'divider': 'border-b border-base',
      'input-border': 'border border-1 border-[#6b72801a]  text-[#e5e7eb]',
    },
  ],
})