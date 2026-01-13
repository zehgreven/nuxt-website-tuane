// @ts-check
import withNuxt from './.nuxt/eslint.config.mjs';
import prettier from 'eslint-config-prettier';

export default withNuxt(
  {
    ignores: [
      'node_modules',
      '.nuxt',
      '.output',
      '.data',
      '.nitro',
      '.cache',
      'dist',
      'logs',
      '*.log',
    ],
    rules: {
      'vue/multi-word-component-names': 'off',
      quotes: ['error', 'single'],
      semi: ['error', 'always'],
      indent: ['error', 2],
    },
  },
  prettier,
);
