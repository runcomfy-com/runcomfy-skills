---
name: ad-variants
title: Ad variants
category: marketing
description: Turn one ad into several versions to test, such as a new language, a new scene or a new opening for a video. Use for "more variations", "localise this ad", "translate this ad", "new hooks for this video", "change the outfit in this ad". Not for new ideas from scratch (marketing-research-to-ads), headline versions (marketing-headline-variants) or new sizes (marketing-resize-ads).
example: Translate this ad into Spanish and German, and keep the layout and claims the same.
---

# Ad variants

Change one thing at a time so a test shows what worked. If they have results from an earlier test, ask what won and build on that.

| Variant | Model | How |
| --- | --- | --- |
| A new language | `openai/gpt-image-2/edit` | Translate for meaning, then quote the words. Keep claims the same |
| A new scene, same product | `google/nano-banana-2/edit` | Keep the product and logo unchanged |
| A new opening for a video | `happyhorse/happyhorse-1.0/reference-to-video` | Use frames from the ad as references |
| A new outfit, person, product or place in a video ad | `kling/kling-v4/video-edit` | Change only that one thing. Keep the motion, framing, timing and sound |
| A video in a new shape | `bytedance/seedance-2.0-mini/video-to-video` | It regenerates the clip, so check the product and any text |

## Steps

1. Get the ad, what to vary and how many. For new video openings, offer three hooks written from different angles: a problem, a result, a surprise. For headlines or sizes alone, use the marketing-headline-variants or marketing-resize-ads skill.
2. Show the list and the total price, and wait for a yes.
3. Run one request per variant. Read the text in each result when you can see it: image models sometimes misspell.
4. Deliver the links labelled by what changed. RunComfy has no tool for joining clips: give a new video opening as its own clip, or join it with ffmpeg if you can run commands.

Do not invent discounts, prices or claims that are not in the original ad.
