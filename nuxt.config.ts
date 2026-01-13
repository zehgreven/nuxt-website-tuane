// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxt/ui', '@nuxt/eslint', '@nuxt/icon'],
  colorMode: {
    classSuffix: '',
  },
  postcss: {
    plugins: {
      '@tailwindcss/postcss': {},
    },
  },
  css: ['~/assets/css/main.css'],
  icon: {
    customCollections: [
      {
        prefix: 'app',
        dir: './app/assets/icons',
      },
      {
        prefix: 'pixel',
        dir: './app/assets/icons/pixel',
      },
    ],
  },
});
