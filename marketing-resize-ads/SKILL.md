---
name: marketing-resize-ads
title: Ad Resizer
category: marketing
description: One static ad rebuilt for other placements and shapes, such as 1:1 and 4:5 for the feed, 9:16 for Stories and Reels or 16:9 for a banner, with the layout rearranged instead of cropped. Use for "resize this ad", "make this ad for Stories", "other aspect ratios", "adapt it for placements", "banner size". Not for new headlines (marketing-headline-variants).
example: Adapt this static ad for 1:1, 4:5, and 9:16 placements, keeping the copy and branding clear.
---

# Ad Resizer

Rebuild the layout for each shape so the product, headline and call to action stay clear. Never just crop or stretch the original.

## Ask first

- The ad, and which placements. Default to 1:1 and 4:5 for the feed and 9:16 for Stories and Reels.

Show the sizes and the price, and wait for a yes.

## Make each size

Use `openai/gpt-image-2.5/sunburst/edit` with the ad as the only image and `aspect_ratio` set to the placement, one request per size:

> Recompose this ad as a vertical 9:16 story ad. Keep the product, the photograph's look and every word exactly as they are, in the same fonts and colours; rearrange the layout to suit the new shape instead of cropping, and keep all text and the product well inside the edges. No other text.

For 9:16, say where things go: the logo near the top, the product in the middle and the text in the lower third, clear of the bars Stories draw over the top and bottom.

## Check before you deliver

Read every word in each size against the original, and check nothing touches an edge. Remake any size that drops or changes a word, and say so.

## Deliver

Label each link by placement, and suggest checking each one in the platform's preview before launch.
