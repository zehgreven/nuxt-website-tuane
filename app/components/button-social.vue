<template>
  <UButton
    class="p-1 hover:scale-120 transition-transform"
    color="neutral"
    variant="ghost"
    :to="link"
    target="_blank"
  >
    <UIcon :name="icon" class="text-3xl" />
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
});
</script>
