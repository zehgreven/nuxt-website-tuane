<template>
  <div class="mx-auto min-h-screen">
    <header class="sticky top-0 z-50 bg-white dark:bg-gray-900 py-5 shadow-sm">
      <div class="container max-w-4xl mx-auto px-4">
        <div class="flex justify-between items-start md:items-center">
          <div class="flex items-center md:space-x-12">
            <NuxtLink to="/" class="text-center">
              <div class="text-3xl font-semibold">Tuane Marcela Correia</div>
              <div class="text-lg font-thin">Nutricionista</div>
            </NuxtLink>
          </div>
          <ClientOnly>
            <UColorModeButton />
          </ClientOnly>
        </div>
      </div>
    </header>

    <main>
      <slot />
    </main>
  </div>
</template>

<script setup>
useHead({
  titleTemplate: '%s - Tuane Marcela Correia',
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
  @apply bg-white dark:bg-gray-900 text-gray-700 dark:text-gray-300;
}
</style>
