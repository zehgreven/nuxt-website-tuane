<template>
  <div
    class="space-y-2 p-5 lg:py-10 rounded-2xl bg-brand-yellow-500 text-brand-green-500 dark:bg-brand-green-700 dark:text-brand-yellow-500 flex flex-col items-center text-center"
  >
    <UIcon :name="icon" :size="size" class="text-brand-green-500 dark:text-brand-yellow-500" />
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
