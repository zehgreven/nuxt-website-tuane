<template>
  <UButton
    class="pt-5 pb-5 pl-10 pr-10"
    label="AGENDAR CONSULTA AGORA"
    color="neutral"
    variant="soft"
    @click="agendarConsulta"
  />
</template>

<script setup lang="ts">
const agendarConsulta = () => {
  window.open('https://calendly.com/tuane-correia/30min', '_blank');
};
</script>
