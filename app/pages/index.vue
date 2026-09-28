<template>
  <div class="bg-brand-yellow-500 dark:bg-brand-green-950">
    <section
      class="relative container max-w-4xl mx-auto px-4 py-20 overflow-hidden min-h-125 flex items-center"
    >
      <img
        src="../assets/images/sofa-preto.png"
        alt="Tuane Correia"
        class="absolute right-0 top-0 w-full h-full md:w-1/2 object-cover object-center opacity-20 md:opacity-100 z-0"
      />

      <div class="relative z-10 grid md:grid-cols-2 w-full">
        <div class="space-y-4 md:px-5 text-center">
          <h1 class="font-dream-avenue text-4xl font-bold text-brand-green-500 dark:text-white">
            Nutrição Humanizada
          </h1>
          <p class="text-lg text-brand-green-500 dark:text-gray-300">
            Transforme sua relação com a comida através de um acompanhamento personalizado e focado
            no seu bem-estar integral.
          </p>
          <div class="justify-self-center md:justify-self-center">
            <ButtonAgendarConsulta />
          </div>
        </div>

        <div class="hidden md:block"></div>
      </div>
    </section>

    <section
      class="bg-brand-green-500 text-brand-yellow-500 dark:bg-brand-green-950 dark:text-yellow-500"
    >
      <div class="relative container mx-auto max-w-5xl overflow-hidden px-4 py-16 md:px-6 md:py-20">
        <img
          src="../assets/images/quem-sou-eu-no-bg-2.png"
          alt="Tuane Correia, nutricionista, sentada à mesa com o notebook"
          width="576"
          height="828"
          class="absolute top-0 right-0 z-0 h-full w-full object-cover object-center opacity-20 md:w-1/2 md:object-contain md:object-bottom md:opacity-100"
        />
        <div class="relative z-10 grid w-full md:grid-cols-2">
          <div class="md:pr-16">
            <h2 class="text-center font-dream-avenue text-4xl font-bold text-balance md:text-left">
              Quem sou eu?
            </h2>
            <div
              class="mx-auto mt-6 max-w-xl space-y-4 text-center text-lg leading-relaxed md:mx-0 md:text-left"
            >
              <p>
                Sou nutricionista, pós-graduada em Nutrição Esportiva e Fisiologia do Exercício, e
                acredito que cuidar da alimentação vai muito além de seguir uma dieta.
              </p>
              <p>
                Meu propósito é ajudar você a construir uma relação mais leve e consciente com a
                comida, desenvolvendo hábitos que façam sentido para a sua rotina e que possam ser
                mantidos ao longo do tempo.
              </p>
              <p>
                Acredito em uma nutrição individualizada, baseada em ciência e sem extremismos, que
                respeita o momento, os objetivos e a realidade de cada pessoa.
              </p>
              <p>
                Seja para emagrecer, melhorar a alimentação, ter mais disposição, cuidar da saúde ou
                alcançar seus objetivos, meu papel é te orientar para que você consiga transformar
                sua rotina de forma consistente e sustentável.
              </p>
            </div>
          </div>
          <div class="hidden md:block"></div>
        </div>
      </div>
    </section>

    <section
      class="pt-20 pb-20 text-center bg-brand-yellow-500 dark:bg-brand-green-950 text-brand-green-500 dark:text-brand-green-500"
    >
      <div
        class="container max-w-4xl mx-auto px-5 flex flex-col items-center justify-center space-y-6"
      >
        <h2 class="font-dream-avenue text-4xl font-bold">Sua jornada começa aqui</h2>
        <div class="text-lg max-w-3xl text-left space-y-4 leading-relaxed">
          <p>
            Se você quer transformar sua alimentação, seus hábitos e sua relação com a comida, eu
            posso te guiar.
          </p>
          <p>
            Meu trabalho é oferecer um acompanhamento individualizado para você cuidar da sua saúde
            e construir escolhas que façam sentido para a sua rotina — de forma leve, consciente e
            sustentável.
          </p>
        </div>
        <ButtonAgendarConsulta label="QUERO AGENDAR MEU HORÁRIO" icon="logo:whatsapp" />
      </div>
    </section>

    <section
      class="py-20 px-5 text-center bg-brand-green-500 dark:bg-brand-green-950 text-brand-yellow-500 dark:text-yellow-500"
    >
      <div class="container justify-self-center flex flex-col items-center justify-center">
        <p class="text-4xl font-dream-avenue">Como funciona</p>
        <p class="text-4xl font-dream-avenue">o atendimento:</p>

        <div class="grid grid-cols-1 lg:grid-cols-5 gap-5 mt-10 mb-10">
          <HBox class="col-span-1" icon="i-lucide-clipboard-list">
            <p class="font-bold text-xl mb-5">01. Consulta inicial</p>
            <p>
              Uma avaliação completa e individualizada para entender seus hábitos, rotina,
              histórico, sintomas, exames, prática de exercícios e objetivos.
            </p>
          </HBox>

          <HBox class="col-span-1" icon="i-lucide-target">
            <p class="font-bold text-xl mb-5">02. Estratégia personalizada</p>
            <p>
              A partir dessa avaliação, construirei uma estratégia nutricional que se encaixe na sua
              rotina, preferências e necessidades — sem fórmulas prontas.
            </p>
          </HBox>

          <HBox class="col-span-1" icon="i-lucide-message-circle-heart">
            <p class="font-bold text-xl mb-5">03. Acompanhamento</p>
            <p>
              Durante o processo você conta com suporte para esclarecer dúvidas e lidar com as
              dificuldades que surgirem na prática.
            </p>
          </HBox>

          <HBox class="col-span-1" icon="i-lucide-chart-line">
            <p class="font-bold text-xl mb-5">04. Reavaliação</p>
            <p>
              Após aproximadamente 30 dias, avaliamos sua evolução, resultados, dificuldades e
              adaptação à estratégia, realizando os ajustes necessários para a próxima etapa.
            </p>
          </HBox>

          <HBox class="col-span-1" icon="i-lucide-sprout">
            <p class="font-bold text-xl mb-5">05. Continuidade</p>
            <p>
              O acompanhamento é construído de forma individualizada, respeitando seu ritmo, seus
              objetivos e o que fizer sentido para cada momento da sua jornada.
            </p>
          </HBox>
        </div>
        <p class="mt-10"></p>
      </div>
    </section>

    <section class="hidden pt-20 pb-20 text-center bg-brand-yellow-500 dark:bg-brand-green-950">
      <div class="container max-w-4xl justify-self-center">
        <Testimonials />
      </div>
    </section>

    <section
      class="pt-20 pb-20 text-center bg-brand-yellow-500 dark:bg-brand-green-950 text-brand-green-500 dark:text-brand-green-500"
    >
      <div
        class="container max-w-4xl justify-self-center flex flex-col items-center justify-center"
      >
        <Faq />
      </div>
    </section>
  </div>
</template>
