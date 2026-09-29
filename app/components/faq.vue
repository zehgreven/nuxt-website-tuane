<template>
  <div class="w-full p-5">
    <h2 class="font-dream-avenue text-4xl font-bold mb-10">Perguntas Frequentes</h2>
    <UAccordion class="text-left" :items="items" />
  </div>
</template>

<script setup lang="ts">
import type { AccordionItem } from '@nuxt/ui';

const items: AccordionItem[] = [
  {
    label: 'É uma dieta restritiva?',
    icon: 'i-lucide-candy-off',
    content:
      'Não. O acompanhamento é individualizado, sem extremismos e sem fórmulas prontas, feito para a sua rotina.',
  },
  {
    label: 'Preciso praticar exercícios?',
    icon: 'i-lucide-dumbbell',
    content:
      'Não é obrigatório. A atividade física pode potencializar os resultados, mas o foco do acompanhamento é a alimentação.',
  },
];
</script>
