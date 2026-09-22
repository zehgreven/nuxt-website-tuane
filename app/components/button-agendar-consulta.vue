<template>
  <UButton
    class="pt-5 pb-5 pl-10 pr-10 rounded-full text-lg"
    size="lg"
    color="primary"
    variant="solid"
    :to="whatsappUrl"
    target="_blank"
  >
    {{ label }}
    <UIcon v-if="icon" :name="icon" class="size-6 ml-3" />
  </UButton>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    label?: string;
    icon?: string;
  }>(),
  {
    label: 'AGENDAR CONSULTA AGORA',
    icon: undefined,
  },
);
</script>
