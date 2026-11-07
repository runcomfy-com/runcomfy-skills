---
name: marketing-headline-variants
title: Headline Multiplier
category: marketing
description: New versions of one static ad where only the headline changes, ready to test against each other. Use for "headline variations", "test different headlines", "A/B test this ad", "10 versions of this ad", "new copy for this ad". Not for new ad ideas from scratch (marketing-research-to-ads) or new sizes (marketing-resize-ads).
example: Create 10 versions of this ad, changing only the headline. Keep everything else unchanged.
---

# Headline Multiplier

Change only the headline, so a test shows which message works. Keep the picture, layout, fonts, colours, brand and offer exactly as they are.

## Write the headlines

- Default to 10 unless the user asks for a number.
- Spread them across angles: a benefit, a moment of use, curiosity, a problem, the flavour or feel, sharing.
- Keep each one as long as the original and in the same rhythm, so it fits the same space. If the original is two short lines, write two short lines.
- Add no claims, prices or offers the original ad does not make.

Show the list and the price, and wait for a yes.

## Make the versions

Use `openai/gpt-image-2.5/sunburst/edit` with the ad as the only image, one request per headline, at the ad's own shape:

> Change only the headline. It now reads exactly "line one" on the first line and "line two" on the second, in the same font, size, colour and position. Keep everything else in the image exactly the same. No other text.

Read every result: the words must match exactly, and nothing else may change. Remake any that do not, and say so.

## Deliver

Label each link with its headline and angle, and suggest testing them with the same audience, budget and placement, so only the headline differs.
