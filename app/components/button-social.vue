<template>
  <UButton
    class="p-1 hover:scale-120 transition-transform"
    color="neutral"
    variant="ghost"
    :to="link"
    target="_blank"
  >
    <UIcon :name="icon" :class="sizeClasses[props.size]" />
  </UButton>
</template>

<script setup lang="ts">
const props = defineProps({
  icon: {
    type: String,
    required: true,
  },
  link: {
    type: String,
    required: true,
  },
  size: {
    type: String,
    default: 'md',
  },
});

const sizeClasses = {
  sm: 'text-xl md:text-2xl',
  md: 'text-3xl md:text-4xl',
  lg: 'text-5xl md:text-6xl',
};
</script>
