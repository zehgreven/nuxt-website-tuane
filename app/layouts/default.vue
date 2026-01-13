<template>
  <div class="mx-auto min-h-dvh">
    <Header />

    <main>
      <slot />
      <Footer />
      <div class="fixed bottom-6 right-6 z-50">
        <UButton
          to="https://wa.me/554491075497"
          target="_blank"
          rel="noopener noreferrer"
          size="xl"
          color="neutral"
          variant="link"
          class="rounded-full shadow-2xl hover:scale-120 transition-transform p-4"
        >
          <template #leading>
            <Icon name="logos:whatsapp-icon" class="w-8 h-8" />
          </template>
        </UButton>
      </div>
    </main>
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
