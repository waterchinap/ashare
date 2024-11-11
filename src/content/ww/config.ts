// 1. Import utilities from `astro:content`
import { z, defineCollection } from 'astro:content';
// 2. Define your collection(s)
const wwCollection = defineCollection({ 
    type: 'content',
    schema: z.object({
        ww: z.string(),
        ru: z.string(),
        days: z.number(),
        event: z.string().optional()
    })
 });
// 3. Export a single `collections` object to register your collection(s)
//    This key should match your collection directory name in "src/content"
export const collections = {
  'ww': wwCollection,
};