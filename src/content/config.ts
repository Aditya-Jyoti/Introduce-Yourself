import { z, defineCollection } from "astro:content";

const introductionCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(),
    interests: z.string(),
    description: z.string(),
    github: z.string().url(),
    image: z.boolean().optional(),
  }),
});

export const collections = {
  introductions: introductionCollection,
};
