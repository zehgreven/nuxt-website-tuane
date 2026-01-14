<template>
  <button
    @click="toggleMode"
    :icon="nextModeIcon"
    class="flex items-center justify-center w-10 h-10 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors"
  >
    <Icon :name="nextModeIcon" size="30" class="" />
  </button>
</template>

<script setup>
const colorMode = useColorMode();
const modes = ['light', 'dark'];

const nextModeIcons = {
  light: 'i-heroicons-sun',
  dark: 'i-heroicons-moon',
};

const nextMode = computed(() => {
  const currentModeIndex = modes.indexOf(colorMode.preference);
  const nextModeIndex = (currentModeIndex + 1) % modes.length;
  return modes[nextModeIndex];
});

const nextModeIcon = computed(() => nextModeIcons[nextMode.value]);

const toggleMode = () => (colorMode.preference = nextMode.value);
</script>
