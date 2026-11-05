---
name: ad-concepts
title: Static ads from research
category: marketing
description: New static ads built on real reasons to buy, found in a product page, customer reviews or competitor pages. Use for "make ads for my product", "ad ideas", "ad creative", "ads from these reviews", "what angle should I run", "Meta ads". Not for new versions of an existing ad (ad-variants).
example: Here are 40 reviews of my sleep mask. Find the strongest angles and make 3 ads for Instagram.
---

# Static ads from research

An ad works when it says a true reason to buy that the buyer already cares about. Find that before designing anything.

## Gather

- A product photo and the product's facts. If they give a page and you can read it, take the facts from it and show what you took. Otherwise ask them to paste the facts.
- What to learn from: reviews, survey answers, support messages or competitor pages.
- Where the ads run: feed (1:1 or 4:5), Stories and Reels (9:16). Brand colours and logo, if they have them.

## Find the angles

Write three to five angles and show them before making anything. For each one:

- Who it is for, and what they want or fear.
- The promise in one line, in the buyer's own words where you can.
- The proof: the quote or fact it rests on, and how often it came up in the source.

Say when an angle rests on thin evidence. On competitor pages, look for what they all say and what they leave out. Compare only on facts the user can stand behind, and do not name a competitor unless the user asks.

## Pick a format for each angle

| Format | What is on it |
| --- | --- |
| Headline and hero | One strong line, the product large |
| Benefits | The product with three or four short benefits |
| Us versus them | Two columns of true, checkable differences |
| Customer quote | A real quote, word for word, that the customer agreed to share |
| Problem and fix | The problem on one side, the product solving it on the other |
| Before and after | Only for a result the user can prove, and where the ad platform allows it |
| Offer | A real offer the user gave you, with its terms |

## Make them

| Job | Model |
| --- | --- |
| With a product photo, the default | `openai/gpt-image-2/edit` |
| No photo | `openai/gpt-image-2/text-to-image` |

Set the background, palette, type style and logo position in the first prompt and repeat those words in every ad, so that only the message changes. Quote every word that appears on the ad.

## Steps

1. Show the chosen angles, the formats, the exact words and the total price, and wait for a yes.
2. Make the first ad and show it. Then make the rest.
3. Read the words in each result, since image models sometimes misspell. Redo only what is wrong.
4. Deliver the links labelled by angle, and say which you would test first and why. For more versions of a winner, use the `ad-variants` skill.
