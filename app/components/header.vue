<template>
  <header class="sticky top-0 z-50 bg-brand-green-500 dark:bg-gray-900 py-3 sm:py-5 shadow-sm">
    <div class="container max-w-4xl mx-auto px-4">
      <div class="flex justify-between items-center gap-2">
        <NuxtLink to="/" class="min-w-0 text-center text-brand-yellow-500 dark:text-gray-200">
          <div class="font-dream-avenue text-base xs:text-xl sm:text-3xl truncate">
            Tuane Correia
          </div>
          <div class="text-xs sm:text-lg font-futura font-thin">NUTRICIONISTA</div>
        </NuxtLink>
        <div class="flex items-center gap-1 sm:gap-2 shrink-0">
          <!-- <ButtonAcessarSistema /> -->
          <ButtonSocial icon="logo:instagram" link="https://www.instagram.com/nutrituane/" />
          <ButtonSocial
            class="hidden sm:block"
            icon="logo:whatsapp"
            link="http://wa.me/554491075497"
          />
        </div>
      </div>
    </div>
  </header>
</template>
