---
name: product-photoshoot
title: Product photoshoot
category: marketing
description: Brand-quality product images from a product photo or description. Use for "product photo", "studio shot", "lifestyle image", "hero banner", "Pinterest pin", "carousel", "someone holding my product", "model wearing my product", "floating product", "restyle this image". Not for a marketplace listing set (marketplace-images) or ads built around a message (marketing-research-to-ads).
example: Make 3 lifestyle shots of this bottle for my online store.
---

# Product photoshoot

Keeping the real product recognisable matters more than a striking picture. Always use the user's product photo as a reference when there is one.

## Pick the shot

Go by what the image is for. If two fit, take the more specific one: a pin of a product on a kitchen counter is a pin, and a banner showing the product in use is a banner.

| They want | Shot | Shape |
| --- | --- | --- |
| Catalog, plain background, store page | Studio | 1:1 |
| A real place, in use, atmosphere | Lifestyle | 4:5 |
| Hands holding it, applying it, close on skin | Close-up with a person | 4:5 |
| Pinterest, moodboard | Pin | 2:3 |
| Website or email header, campaign banner | Banner | 16:9 |
| A swipeable post of connected slides | Carousel | 4:5 |
| Worn or used by a model, lookbook | On a model | 3:4 |
| Floating, splash, frozen motion, surreal, CGI look | Concept | 1:1 |
| An existing image in a new mood or season | Restyle | Same as the image |

Stories and Reels are 9:16. Use another shape when the user asks for it.

## Ask only what is missing

- **A photo and "make me images":** how many (1, 3 or 5), which look (studio, lifestyle, with a model, concept), and where they will be used (store, Instagram, Pinterest, website).
- **A photo and a named use:** how many, and the mood or offer to get across.
- **No photo:** ask for one first, since the result will be much closer to the real product. Without one, ask for the category, packaging, colours and exact label text.
- **An image to redo:** which aesthetic (quiet luxury, cottagecore, Y2K, Scandinavian minimal, something else), any season or event, and what must not change.
- **On a model:** what kind of person (suggest two or three that suit the buyer), the setting (studio, street, outdoors, home), and the framing (full body, waist up, close on the product).
- **A vague request:** what the product is, the goal (sell, awareness, website), and any image they like.

## Models

| Job | Model |
| --- | --- |
| With a product photo, the default | `openai/gpt-image-2/edit` |
| Several references, such as the product and a model | `google/nano-banana-2/edit` |
| No product photo, description only | `openai/gpt-image-2/text-to-image` |

Use 2K for images they will publish. Medium quality is enough unless they ask for more: high costs several times as much.

## Prompts

With a reference, start with: "Keep the product's shape, label and colours exactly as in the reference." Then:

- **Studio:** seamless [colour] background, soft key light from the left, gentle contact shadow, centred, label sharp and readable, commercial catalog photography.
- **Lifestyle:** name the place, the time of day and one simple action, like hands placing the product on a kitchen counter in morning light. Keep the product in the foreground with the background softly out of focus.
- **Close-up with a person:** a tight crop on hands or part of a face, natural skin texture, the product in sharp focus and unobstructed.
- **Pin:** a vertical styled flat lay or shelf, airy light, a restrained palette, clear space near the top for a title.
- **Banner:** the product on one third, calm empty space on the other side for a headline, no text unless asked.
- **Carousel:** one idea per slide, such as hook, problem, product, proof, call to action. Set the background, palette and light in the first prompt and repeat those words in every slide. Quote any slide text exactly.
- **On a model:** the person's age range and style, how they wear or hold it, the setting and the framing. Only use a real person who agreed.
- **Concept:** one idea only, such as splashes of the ingredient frozen in the air or the product floating over a pastel gradient. Studio light, high-end CGI look.
- **Restyle:** say what stays (the product, the framing), then what changes (background, palette, props, season).

## Steps

1. Get the product photo. If there is none, ask for the name, the colours and any label text.
2. Show the plan in one line each, with the total price, and wait for a yes.
3. Run each image as its own request. Make each one differ by setting, angle, light or palette.
4. Check that label text is correct when you can see the images. Give back the links as a short list.
