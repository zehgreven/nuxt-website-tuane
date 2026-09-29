<template>
  <UButton
    class="pt-5 pb-5 pl-10 pr-10 rounded-full text-lg"
    size="lg"
    variant="solid"
    :color="color"
    :to="to"
    target="_blank"
  >
    {{ label }}
    <UIcon v-if="icon" :name="icon" class="size-6 ml-3" />
  </UButton>
</template>

<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    label?: string;
    icon?: string;
    message?: string;
    color?: 'primary' | 'secondary';
  }>(),
  {
    label: 'AGENDAR CONSULTA AGORA',
    icon: undefined,
    message: undefined,
    color: 'primary',
  },
);

const to = computed(() => (props.message ? buildWhatsappUrl(props.message) : whatsappUrl));
</script>
