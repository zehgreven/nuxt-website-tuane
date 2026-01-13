<template>
  <div class="mx-auto min-h-dvh">
    <Header />

    <main>
      <slot />
      <Footer />
    </main>
  </div>
  <div class="fixed inset-0 h-svh pointer-events-none z-60">
    <div class="absolute right-5 bottom-5 md:bottom-6 pointer-events-auto">
      <UButton
        to="https://wa.me/554491075497"
        target="_blank"
        class="rounded-full shadow-2xl hover:scale-110 transition-transform p-0"
        variant="link"
      >
        <Icon name="logos:whatsapp-icon" class="w-14 h-14 md:w-16 md:h-16" />
      </UButton>
    </div>
  </div>
</template>

<script setup>
useHead({
  titleTemplate: 'Tuane Marcela Correia',
  link: [
    {
      rel: 'preconnect',
      href: 'https://fonts.googleapis.com',
    },
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Roboto&display=swap',
      crossorigin: '',
    },
  ],
});
</script>

<style>
@reference "../assets/css/main.css";

body {
  font-family: 'Roboto';
}

body {
  @apply bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-200;
}
</style>
