<template>
  <footer
    class="bg-brand-green-500 dark:bg-brand-green-800/50 border-t border-gray-200 dark:border-gray-700 py-12"
  >
    <div class="container max-w-4xl mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
        <div class="space-y-3">
          <div
            class="font-dream-avenue text-xl font-bold text-brand-yellow-500 dark:text-brand-yellow-500"
          >
            Tuane Correia
          </div>
          <p class="text-sm text-brand-yellow-500 dark:text-brand-yellow-500">
            Nutricionista Clínica e Esportiva.<br />
            Transformando vidas através da alimentação consciente.
          </p>
        </div>

        <div class="space-y-3">
          <h4
            class="font-semibold text-brand-yellow-500 dark:text-brand-yellow-500 uppercase text-xs tracking-widest"
          >
            Contato
          </h4>
          <ul class="text-sm space-y-2 text-brand-yellow-500 dark:text-brand-yellow-500">
            <li class="flex items-center gap-2">
              <UIcon name="i-heroicons-envelope" class="w-4 h-4" />
              nutrituanecorreia@gmail.com
            </li>
            <li class="flex items-center gap-2">
              <UIcon name="i-heroicons-phone" class="w-4 h-4" />
              (44) 99107-5497
            </li>
          </ul>
        </div>

        <div class="space-y-3">
          <h4
            class="font-semibold text-brand-yellow-500 dark:text-brand-yellow-500 uppercase text-xs tracking-widest"
          >
            Siga-me
          </h4>
          <div class="flex gap-4">
            <ButtonSocial
              icon="logo:instagram"
              size="sm"
              link="https://www.instagram.com/nutri.tuane/"
            />
            <ButtonSocial icon="logo:whatsapp" size="sm" link="http://wa.me/554491075497" />
          </div>
        </div>
      </div>

      <hr class="my-8 border-gray-200 dark:border-gray-700" />

      <div
        class="flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-brand-yellow-500"
      >
        <span>© 2026 Tuane Marcela Correia. Todos os direitos reservados.</span>
        <span>CRN-8 20647</span>
      </div>
    </div>
  </footer>
</template>
