<template>
  <div
    class="space-y-2 p-5 bg-orange-500 dark:bg-orange-400 text-white flex flex-col items-start text-start"
  >
    <UIcon :name="icon" :size="size" class="text-white" />
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
