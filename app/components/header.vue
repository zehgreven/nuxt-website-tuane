<template>
  <header class="sticky top-0 z-50 bg-white dark:bg-gray-900 py-3 sm:py-5 shadow-sm">
    <div class="container max-w-4xl mx-auto px-4">
      <div class="flex justify-between items-center flex-wrap gap-3">
        <NuxtLink to="/" class="text-center text-gray-900 dark:text-gray-200">
          <div class="text-xl sm:text-3xl font-semibold">Tuane Marcela Correia</div>
          <div class="text-sm sm:text-lg font-thin">Nutricionista</div>
        </NuxtLink>
        <div class="flex items-center gap-2">
          <ButtonAcessarSistema />
          <ButtonSocial icon="logo:instagram" link="https://www.instagram.com/nutri.tuane/" />
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
