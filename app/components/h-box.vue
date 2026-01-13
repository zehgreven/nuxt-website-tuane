<template>
  <div class="space-y-2 p-5 bg-gray-700 dark:bg-gray-800 flex flex-col items-start text-start">
    <UIcon :name="icon" :size="size" class="text-gray-200 dark:text-gray-400" />
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
