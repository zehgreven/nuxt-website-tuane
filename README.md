# Nuxt Minimal Starter

Look at the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev

# bun
bun run dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.

## Remove green screen

`scripts/remove_background.py` removes a green-screen (chroma key) background from an image. Input and output both live in `app/assets/images`; pass only the file name.

From the project root:

```bash
python3 scripts/remove_background.py your_image.jpeg
```

When the output name is omitted, the script writes `<input>_no_bg.png`. The command above creates `app/assets/images/your_image_no_bg.png`.

To choose a different output name:

```bash
python3 scripts/remove_background.py your_image.jpeg another_name.png
```

The script depends on Pillow (`from PIL import Image`).
