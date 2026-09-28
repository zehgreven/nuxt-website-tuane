<template>
  <NuxtLayout>
    <UApp>
      <NuxtPage />
    </UApp>
  </NuxtLayout>
</template>

<script setup>
useHead({
  viewport: 'width=device-width, initial-scale=1, viewport-fit=cover',
  link: [
    { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' },
    { rel: 'icon', href: '/favicon.ico', sizes: '32x32' },
  ],
});
</script>
