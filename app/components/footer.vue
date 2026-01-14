<template>
  <footer
    class="bg-gray-50 dark:bg-gray-800/50 border-t border-gray-200 dark:border-gray-700 py-12"
  >
    <div class="container max-w-4xl mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
        <div class="space-y-3">
          <div class="text-xl font-bold text-gray-900 dark:text-white">Tuane Marcela Correia</div>
          <p class="text-sm text-gray-500 dark:text-gray-400">
            Nutricionista Clínica e Esportiva.<br />
            Transformando vidas através da alimentação consciente.
          </p>
        </div>

        <div class="space-y-3">
          <h4 class="font-semibold text-gray-900 dark:text-white uppercase text-xs tracking-widest">
            Contato
          </h4>
          <ul class="text-sm space-y-2 text-gray-600 dark:text-gray-300">
            <li class="flex items-center gap-2">
              <UIcon name="i-heroicons-envelope" class="w-4 h-4" />
              contato@tuanutri.com.br
            </li>
            <li class="flex items-center gap-2">
              <UIcon name="i-heroicons-phone" class="w-4 h-4" />
              (44) 99107-5497
            </li>
          </ul>
        </div>

        <div class="space-y-3">
          <h4 class="font-semibold text-gray-900 dark:text-white uppercase text-xs tracking-widest">
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
        class="flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-gray-400"
      >
        <span>© 2026 Tuane Marcela Correia. Todos os direitos reservados.</span>
        <span>CRN-8 12345 | CNPJ: 00.000.000/0000-00</span>
      </div>
    </div>
  </footer>
</template>
