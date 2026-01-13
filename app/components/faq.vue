<template>
  <div class="w-full">
    <h2 class="text-4xl mb-10">Perguntas Frequentes</h2>
    <UAccordion class="text-left" :items="items" />
  </div>
</template>

<script setup lang="ts">
import type { AccordionItem } from '@nuxt/ui';

const items: AccordionItem[] = [
  {
    label: 'Quanto tempo dura o programa?',
    icon: 'i-lucide-hourglass',
    content: 'O tempo varia conforme a resposta do seu corpo, de maneira personalizada.',
  },
  {
    label: 'É uma dieta restritiva?',
    icon: 'i-lucide-candy-off',
    content: 'Não! É um programa alimentar com exames exclusivos',
  },
  {
    label: 'Preciso praticar exercícios?',
    icon: 'i-lucide-dumbbell',
    content:
      'A atividade física pode potencializar os resultados, mas o foco do programa é no ajuste metabólico e nutricional.',
  },
];
</script>
