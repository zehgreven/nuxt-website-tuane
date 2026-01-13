<template>
  <div class="mx-auto min-h-screen">
    <header class="sticky top-0 z-50 bg-white dark:bg-gray-900 py-5 shadow-sm">
      <div class="flex justify-between items-center px-5">
        <div class="container max-w-4xl mx-auto px-4">
          <div class="flex justify-center items-center flex-wrap sm:justify-between">
            <div class="flex items-center md:space-x-12">
              <NuxtLink to="/" class="text-center">
                <div class="text-3xl font-semibold">Tuane Marcela Correia</div>
                <div class="text-lg font-thin">Nutricionista</div>
              </NuxtLink>
            </div>
            <div class="flex gap-2 sm:justify-center">
              <ButtonSocial
                icon="pixel:logo-instagram"
                link="https://www.instagram.com/nutri.tuane/"
              />
              <ButtonSocial
                icon="pixel:logo-linkedin"
                link="https://www.linkedin.com/in/tuane-marcela-correia/"
              />
              <ButtonSocial icon="pixel:logo-whatsapp" link="http://wa.me/+554491075497" />
            </div>
          </div>
        </div>
        <ClientOnly>
          <UColorModeButton size="xl" />
        </ClientOnly>
      </div>
    </header>

    <main>
      <slot />
      <div class="fixed bottom-6 right-6 z-50">
        <UButton
          to="https://wa.me/+554491075497"
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
