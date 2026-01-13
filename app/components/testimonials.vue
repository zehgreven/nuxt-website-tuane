<template>
  <div class="py-10 bg-gray-50 dark:bg-gray-800 rounded-xl">
    <h2 class="text-center text-2xl font-bold mb-8">O que os pacientes dizem:</h2>

    <UCarousel
      v-slot="{ item }"
      :items="depoimentos"
      :ui="{
        item: 'basis-full md:basis-1/2 lg:basis-1/3 justify-center',
      }"
      indicators
      dots
      class="rounded-lg"
      autoplay
      :interval="4000"
    >
      <div class="px-4 py-2 w-full max-w-sm justify-self-center text-left">
        <div
          class="bg-[#dcf8c6] dark:bg-[#075e54] text-gray-800 dark:text-white p-4 rounded-lg shadow-md relative"
        >
          <div class="font-bold text-green-700 dark:text-green-300 text-sm mb-1">
            {{ item.nome }}
          </div>

          <p class="text-sm leading-relaxed">
            {{ item.texto }}
          </p>

          <div class="flex justify-end items-center gap-1 mt-1 text-xs opacity-60">
            <span>{{ item.data }}</span>
            <UIcon name="i-lucide-check-check" class="text-blue-500 w-4 h-4" />
          </div>

          <div
            class="absolute top-0 -left-2 w-0 h-0 border-t-10 border-t-[#dcf8c6] dark:border-t-[#075e54] border-l-10 border-l-transparent"
          ></div>
        </div>
      </div>
    </UCarousel>
  </div>
</template>

<script setup>
const depoimentos = [
  {
    nome: 'Ana Silva',
    data: '10:45',
    texto:
      'Nutri, perdi 3kg esse mês seguindo o plano! Estou muito feliz com os resultados e não passo fome. 😍',
  },
  {
    nome: 'Carlos Oliveira',
    data: '14:20',
    texto: 'Aquelas receitas de lanche prático salvaram minha semana corrida. Valeu mesmo!',
  },
  {
    nome: 'Mariana Costa',
    data: '09:15',
    texto: 'Minha disposição no treino mudou completamente. Dormindo melhor também!',
  },
  {
    nome: 'Pedro Santos',
    data: '11:30',
    texto: 'O programa ajudou muito a controlar os sintomas da minha SII. Estou muito feliz!',
  },
];
</script>
