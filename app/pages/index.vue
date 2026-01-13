<template>
  <div>
    <section
      class="relative container max-w-4xl mx-auto px-4 py-20 overflow-hidden min-h-125 flex items-center"
    >
      <img
        src="../assets/images/tuane.png"
        alt="Tuane Marcela Correia"
        class="absolute right-0 top-0 w-full h-full md:w-1/2 object-cover object-center opacity-20 md:opacity-100 z-0"
      />

      <div class="relative z-10 grid md:grid-cols-2 w-full">
        <div class="space-y-4 md:pr-8 text-center md:text-left">
          <h1 class="text-4xl font-bold text-gray-900 dark:text-white">Nutrição Humanizada</h1>
          <p class="text-lg text-gray-600 dark:text-gray-300">
            Transforme sua relação com a comida através de um acompanhamento personalizado e focado
            no seu bem-estar integral.
          </p>
          <div class="justify-self-center md:justify-self-start">
            <ButtonAgendarConsulta />
          </div>
        </div>

        <div class="hidden md:block"></div>
      </div>
    </section>

    <div class="border-b-8 border-b-yellow-100 dark:border-b-yellow-200"></div>

    <section class="pt-20 pb-20 text-center bg-gray-700 dark:bg-gray-800 text-white">
      <div
        class="container max-w-4xl justify-self-center flex flex-col items-center justify-center"
      >
        <div class="text-4xl mb-10">Se você…</div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-10">
          <HBox class="col-span-1" icon="pixel:health-stool">
            Não consegue parar de alternar entre diarreia e constipação
          </HBox>
          <HBox class="col-span-1" icon="pixel:design-ruler">
            Não consegue diminuir o estufamento na barriga
          </HBox>
          <HBox class="col-span-1" icon="pixel:healthy-food-dish">
            Está cansada de se sentir constrangida por causa dos sintomas da SII
          </HBox>
          <HBox class="col-span-1" icon="pixel:health-medical-notes">
            Sente que já tentou de tudo para lidar com a Síndrome do Intestino Irritável
          </HBox>
        </div>

        <div class="text-2xl mb-5">
          Saiba, <strong>você pode controlar</strong> de uma vez por todas os
          <strong>seus sintomas</strong>
        </div>
        <div class="text-lg mb-5">
          Porém, <strong>não conseguirá atingir</strong> esse resultado
          <strong>se continuar fazendo</strong> uso de <strong>dietas generalistas</strong>
        </div>
        <div class="text-lg mb-5">
          <strong>Você já deve ter pesquisado</strong> inúmeras dietas, e eu
          <strong>tenho certeza</strong> que você já <strong>tentou de tudo</strong> para aliviar os
          sintomas, <strong>mas a verdade é uma só:</strong>
        </div>

        <div class="text-2xl text-white mb-5 bg-orange-500 dark:bg-orange-400 p-5">
          NÃO É A DIETA GENERALISTA QUE VAI ALIVIAR OS SINTOMAS DA SII
        </div>

        <div class="text-2xl mb-10">
          <strong>Existe um caminho cientificamente comprovado</strong> para controlar os sintomas
          que você tem… <strong>E ele não se resume</strong> a seguir uma dieta saudável
        </div>

        <ButtonAgendarConsulta />
      </div>
    </section>

    <div class="border-b-8 border-b-yellow-100 dark:border-b-yellow-200"></div>

    <section class="pt-20 pb-20 text-center">
      <div class="container max-w-4xl justify-self-center">
        <Testimonials />
      </div>
    </section>

    <div class="border-b-8 border-b-yellow-100 dark:border-b-yellow-200"></div>

    <section class="pt-20 pb-20 text-center bg-gray-700 dark:bg-gray-800 text-white">
      <div
        class="container max-w-4xl justify-self-center flex flex-col items-center justify-center"
      >
        <Faq />
      </div>
    </section>
  </div>
</template>
