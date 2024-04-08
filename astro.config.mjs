import { defineConfig } from "astro/config";

import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  site: "https://aditya-jyoti.github.io/introduce-yourself",
  integrations: [tailwind()],
});
