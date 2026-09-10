export default defineAppConfig({
  ui: {
    colors: {
      primary: 'brand-dark-green',
      secondary: 'green',
      neutral: 'no-color',
    },
    carousel: {
      slots: {
        dot: 'bg-gray-400',
      },
      variants: {
        active: {
          true: {
            dot: 'data-[state=active]:bg-orange-500',
          },
        },
      },
    },
  },
});
