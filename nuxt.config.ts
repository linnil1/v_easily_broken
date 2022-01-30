import { defineNuxtConfig } from 'nuxt3'

export default defineNuxtConfig({
  ssr: true,  // default value
  meta: {
    title: '易碎組 Easily Broken',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { name: 'twitter:card',        content: 'summary_large_image'},
      { name: 'twitter:site',        content: 'https://easily-broken.linnil1.me'},
      { name: 'twitter:description', content: '易碎組 Easily Broken'},
      { name: 'twitter:title',       content: '易碎組 Easily Broken'},
    ],
    link: [
      { rel: 'stylesheet', href: 'assets/default.css' }
    ],
    script: [
      // google analysis
      { src: "https://www.googletagmanager.com/gtag/js?id=G-6307YV711H" },
      { src: "assets/ga.js" },
    ],
  },
})
