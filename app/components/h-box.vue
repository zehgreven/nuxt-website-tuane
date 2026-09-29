<template>
  <div
    class="flex flex-col items-center gap-4 rounded-2xl bg-brand-yellow-500 p-6 text-center text-brand-green-500 md:p-8 dark:bg-brand-green-700 dark:text-brand-yellow-500"
  >
    <UIcon :name="icon" :size="size" class="text-brand-green-500 dark:text-brand-yellow-500" />
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
