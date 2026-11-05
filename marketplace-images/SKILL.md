---
name: marketplace-images
title: Marketplace listing images
category: marketing
description: A matching set of listing images for Amazon, Etsy, Shopify or another marketplace. Use for "listing images", "Amazon main image", "secondary images", "product infographic", "A+ content", "what's in the box image". Not for brand or social photos (product-photoshoot).
example: Make a main image and 5 secondary images for this water bottle's Amazon listing.
---

# Marketplace listing images

Shoppers compare these at thumbnail size, then swipe through them. Each image should answer one question about the product.

## Pick the set

| Set | Images |
| --- | --- |
| Main | The main image |
| Listing | Main, plus infographic, multi-angle, detail, lifestyle and what's in the box |
| A+ | Main, plus banner, problem and fix, features, materials or ingredients, results, how to use and customer proof |
| Everything | All of the above |

Any subset is fine.

## Ask first

- A clear photo of the product. This skill needs one.
- Which marketplace and product category.
- The facts for the words: features, sizes, materials or ingredients, and what is in the box. Results and customer proof need a source from the user: leave those images out if there is none.

## What each image shows

| Image | Content |
| --- | --- |
| Main | The product alone on pure white, filling about 85% of the frame. No text, badges, props or anything that is not included. This follows Amazon's rule for main images |
| Infographic | The product with three or four short callouts, each tied to the part it describes |
| Multi-angle | The same product from three or four angles on one clean background |
| Detail | Close on a material, texture or mechanism, with one short caption |
| Lifestyle | The product in use by its likely buyer, with no words |
| What's in the box | Every included item laid out and labelled, and nothing else |
| Banner | The product, the brand name and one line |
| Problem and fix | The problem on one side, the product solving it on the other |
| Features | Three or four benefits, each with a small picture and a few words |
| Materials or ingredients | The main ones, shown and named, with what each does |
| Results | Only what the user's evidence supports, with that source named |
| How to use | Up to four numbered steps with pictures |
| Customer proof | A real quote, word for word, that the customer agreed to share |

Listing images are 1:1. A+ images are wide: use 16:9 unless the marketplace gives a size.

## Models

| Job | Model |
| --- | --- |
| Images with no words | `google/nano-banana-2/edit` |
| Images with words | `openai/gpt-image-2/edit` |

Quote every word exactly in the prompt.

## Steps

1. List the plan, one line per image with what it shows and its exact words, and the total price. Wait for a yes.
2. Make the main image first and show it. Once they like it, use it with the original photo as references for the rest.
3. Repeat the same palette, type style and background words in every prompt so the set matches.
4. Read every word in each result, since image models sometimes misspell. Redo only the images with a mistake.
5. Deliver with labels, in upload order. Say that rules differ by marketplace and category, so they should check the current rules before uploading.
