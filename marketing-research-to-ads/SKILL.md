---
name: marketing-research-to-ads
title: Ad Strategist
category: marketing
description: Static ads built on research into a product and its competitors, each with its own angle. Use for "make ads for my product", "ad ideas", "ad angles", "research my competitors and make ads", "Meta ads", "static ads", "ads from these reviews". Not for new headlines on an existing ad (marketing-headline-variants).
example: Research this product and its competitors, then create 5 static Meta ads with distinct angles.
---

# Ad Strategist

An ad works when it says a true reason to buy that the buyer already cares about. Research first, then design.

## Gather

- The product: a photo, a page or an ad the user already runs. If they give a page and you can read it, take the facts from it and show what you took. Otherwise ask them to paste the facts.
- The competitors: the ones the user names, or the closest products you can find. Note how they sell: their headlines, claims, colours and what they all leave out.
- Anything else they have, such as reviews or survey answers.
- Where the ads run. Default to 9:16 for Stories and Reels; use 4:5 or 1:1 for the feed.

## Find the angles

Write five angles that do not overlap, such as the main benefit or flavour, a moment of use, a pairing, a treat and a plain call to action. For each one:

- Who it is for, and what they want.
- The headline, under eight words, and one short line under it.
- The proof: the fact it rests on. Say when an angle rests on thin evidence.

Compare only on facts the user can stand behind, and do not name a competitor unless the user asks.

## Make them

| Job | Model |
| --- | --- |
| With a product photo, the default | `openai/gpt-image-2.5/sunburst/edit` |
| No photo | `openai/gpt-image-2.5/sunburst/text-to-image` |

Keep one system across the set: a big bold headline at the top, the short line under it, and a real photograph below. Give each ad its own background colour. Tell the model to keep the product exactly as in the photo, and quote every word that appears on the ad.

## Steps

1. Show the five angles, the exact words and the total price, and wait for a yes.
2. Make the ads. Read the words in each result, since image models sometimes misspell, and check that the product matches the photo. Redo only what is wrong.
3. Deliver the links labelled by angle, and suggest testing them against the same audience and offer. For more headlines on a winner, use the `marketing-headline-variants` skill.
