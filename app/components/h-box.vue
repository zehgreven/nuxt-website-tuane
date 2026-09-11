<template>
  <div
    class="space-y-2 p-5 lg:py-10 rounded-2xl bg-brand-green-400 dark:bg-brand-green-500 text-white flex flex-col items-center text-center"
  >
    <UIcon :name="icon" :size="size" class="text-white" />
    <div class="lg:mt-5">
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
