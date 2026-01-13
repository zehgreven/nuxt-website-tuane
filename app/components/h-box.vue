<template>
  <div class="space-y-2 p-5 border flex flex-col items-start">
    <UIcon :name="icon" :size="size" />
    <div>
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  icon: {
    type: String,
    default: 'i-heroicons-calendar',
  },
  size: {
    type: String,
    default: '40',
  },
});
</script>
