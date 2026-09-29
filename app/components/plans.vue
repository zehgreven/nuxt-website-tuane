<template>
  <section class="bg-brand-yellow-500 px-5 py-20 text-brand-green-500 dark:bg-brand-green-950">
    <div class="mx-auto flex w-full max-w-6xl flex-col items-center">
      <h2 class="text-center font-dream-avenue text-4xl font-bold">Planos</h2>

      <ul class="mt-12 grid w-full grid-cols-1 items-stretch gap-6 lg:grid-cols-3">
        <li
          v-for="plan in plans"
          :key="plan.name"
          class="flex h-full flex-col rounded-2xl bg-brand-green-500 p-6 text-left text-brand-yellow-500 md:p-8 dark:bg-brand-green-800"
        >
          <h3 class="font-dream-avenue text-3xl font-bold leading-tight text-balance">{{ plan.name }}</h3>
          <p class="mt-4 text-base leading-relaxed">{{ plan.forWhom }}</p>

          <p class="mt-6 font-semibold">Você recebe</p>
          <ul class="mt-3 flex flex-col gap-2 text-base leading-snug">
            <li v-for="item in plan.includes" :key="item" class="flex gap-2">
              <UIcon name="i-lucide-check" class="mt-0.5 size-4 shrink-0" aria-hidden="true" />
              <span>{{ item }}</span>
            </li>
          </ul>

          <p class="mt-6 text-sm leading-relaxed">{{ plan.note }}</p>

          <div class="mt-auto pt-8">
            <ButtonAgendarConsulta
              class="w-full justify-center !text-brand-green-500"
              label="QUERO ESTE PLANO"
              color="secondary"
              :message="plan.message"
            />
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<script setup lang="ts">
const plans = [
  {
    name: 'Consulta Avulsa',
    forWhom:
      'Para quem busca uma orientação nutricional individualizada e deseja começar com mais clareza e estratégia.',
    includes: [
      'Consulta nutricional individualizada de 1h a 1h30',
      'Avaliação da rotina, hábitos e objetivos',
      'Estratégia nutricional personalizada',
      'Materiais de apoio em PDF',
      'Guia de suplementos, quando pertinente ao seu caso',
      'Suporte pontual pelo WhatsApp durante 30 dias',
    ],
    note: 'A Consulta Avulsa não inclui consulta de retorno ou reavaliação.',
    message:
      'Olá, Tuane. Entrei em contato pelo site e gostaria de saber mais sobre a Consulta Avulsa.',
  },
  {
    name: 'Acompanhamento nutricional',
    forWhom:
      'Para quem quer um primeiro período de acompanhamento, colocar as mudanças em prática e avaliar a evolução.',
    includes: [
      'Consulta inicial de 1h a 1h30',
      'Consulta de reavaliação de 40min a 1h',
      'Estratégia nutricional personalizada',
      'Ajustes de acordo com a evolução e as necessidades',
      'Materiais de apoio em PDF',
      'Guia de suplementos, quando pertinente ao seu caso',
      'Suporte pontual pelo WhatsApp durante 45 dias',
    ],
    note: 'Duração de até 45 dias, contados a partir da primeira consulta.',
    message:
      'Olá, Tuane. Entrei em contato pelo site e gostaria de saber mais sobre o Acompanhamento nutricional.',
  },
  {
    name: 'Acompanhamento trimestral',
    forWhom:
      'Para quem quer ir além de uma orientação pontual e construir, com acompanhamento, uma relação mais leve e consciente com a alimentação.',
    includes: [
      '1ª consulta de 1h a 1h30',
      '2ª consulta de 40min a 1h',
      '3ª consulta de 40min a 1h',
      'Acompanhamento e ajustes ao longo dos 90 dias',
      'Materiais educativos em PDF',
      'Guia de suplementos, quando pertinente ao seu caso',
      'Suporte pontual pelo WhatsApp durante o período do plano',
    ],
    note: 'Três consultas em até 90 dias, a partir da primeira consulta. Consultas não realizadas nesse período são consideradas expiradas, sem extensão automática do plano.',
    message:
      'Olá, Tuane. Entrei em contato pelo site e gostaria de saber mais sobre o Acompanhamento trimestral.',
  },
];
</script>
