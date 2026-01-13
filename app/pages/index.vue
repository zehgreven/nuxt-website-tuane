<template>
  <div>
    <section class="bg-rose-400 dark:bg-rose-900 pt-20 pb-20">
      <div class="container max-w-4xl justify-self-center grid grid-cols-1 md:grid-cols-2">
        <div class="col-span-1">
          <h2 class="text-4xl text-center md:text-left text-white mb-10">
            <strong>Controle os sintomas</strong> da SII de uma vez <strong>por todas</strong>!
          </h2>
          <h2 class="text-2xl text-center md:text-left text-white mb-10">
            Tenha a chance de ser tratada com um método cientificamente comprovado com um protocolo
            pouco conhecido, porém altamente eficaz
          </h2>
          <ButtonAgendarConsulta />
        </div>
      </div>
    </section>
    <div class="border-b-8 border-b-yellow-100 dark:border-b-yellow-200"></div>
    <section class="bg-amber-900 dark:bg-amber-950 pt-20 pb-20 text-center text-white">
      <div class="container max-w-4xl justify-self-center">
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

        <div class="text-2xl mb-5 bg-amber-950 p-5">
          NÃO É A DIETA GENERALISTA QUE VAI ALIVIAR OS SINTOMAS DA SII
        </div>

        <div class="text-2xl mb-10">
          <strong>Existe um caminho cientificamente comprovado</strong> para controlar os sintomas
          que você tem… <strong>E ele não se resume</strong> a seguir uma dieta saudável
        </div>

        <ButtonAgendarConsulta />
      </div>
    </section>
  </div>
</template>
