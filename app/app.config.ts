export default defineAppConfig({
  ui: {
    colors: {
      primary: 'brand-green',
      secondary: 'brand-yellow',
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
