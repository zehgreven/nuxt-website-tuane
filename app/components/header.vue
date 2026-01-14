<template>
  <header class="sticky top-0 z-50 bg-white dark:bg-gray-900 py-3 sm:py-5 shadow-sm">
    <div class="flex justify-between items-center px-5">
      <div class="container max-w-4xl mx-auto px-4">
        <div class="flex justify-between items-center flex-wrap">
          <div class="flex items-center sm:space-x-12">
            <NuxtLink to="/" class="text-center text-gray-900 dark:text-gray-200">
              <div class="text-xl sm:text-3xl font-semibold">Tuane Marcela Correia</div>
              <div class="text-sm sm:text-lg font-thin">Nutricionista</div>
            </NuxtLink>
          </div>
          <div class="flex gap-2 xm:justify-center">
            <ButtonSocial icon="app:instagram" link="https://www.instagram.com/nutri.tuane/" />
            <ButtonSocial
              class="hidden sm:block"
              icon="app:whatsapp"
              link="http://wa.me/554491075497"
            />
          </div>
        </div>
      </div>
      <ClientOnly>
        <div class="hidden h-full xs:flex items-center justify-center">
          <ColorModeSelector />
        </div>
      </ClientOnly>
    </div>
  </header>
</template>
