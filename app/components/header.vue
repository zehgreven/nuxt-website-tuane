<template>
  <header class="sticky top-0 z-50 bg-brand-green-500 dark:bg-gray-900 py-3 sm:py-5 shadow-sm">
    <div class="container max-w-4xl mx-auto px-4">
      <div class="flex justify-between items-center gap-2">
        <NuxtLink to="/" class="flex min-w-0 items-center gap-2.5 text-brand-yellow-500 sm:gap-3">
          <img
            src="/favicon.svg"
            alt=""
            width="163"
            height="166"
            class="h-11 w-auto shrink-0 sm:h-14"
          />
          <span class="min-w-0 text-center">
            <span class="block truncate font-dream-avenue text-base xs:text-xl sm:text-3xl">
              Tuane Correia
            </span>
            <span class="block font-futura text-xs font-thin sm:text-lg">NUTRICIONISTA</span>
          </span>
        </NuxtLink>
        <div class="flex items-center gap-1 sm:gap-2 shrink-0">
          <!-- <ButtonAcessarSistema /> -->
          <ButtonSocial icon="logo:instagram" link="https://www.instagram.com/nutrituane/" />
          <ButtonSocial class="hidden sm:block" icon="logo:whatsapp" :link="whatsappUrl" />
        </div>
      </div>
    </div>
  </header>
</template>
