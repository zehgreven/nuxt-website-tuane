<template>
  <div class="mx-auto">
    <div class="container max-w-4xl justify-self-center">
      <header class="flex justify-between items-start md:items-center mt-5">
        <div class="flex items-center md:space-x-12">
          <NuxtLink to="/" class="text-center p-2">
            <div class="text-3xl font-semibold">Tuane Marcela Correia</div>
            <div class="text-lg font-thin">Nutricionista</div>
          </NuxtLink>
        </div>
        <ClientOnly>
          <UColorModeButton />
        </ClientOnly>
      </header>
    </div>
    <main class="mt-10">
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
