---
name: ugc-video
title: UGC product video
category: marketing
description: A creator-style vertical video for a product, from idea to finished clip. Use for "UGC video", "product review video", "unboxing", "try-on", "tutorial ad", "TikTok ad", "creator showing my app". Not for a polished video with no presenter (product-video).
example: Create a 15-second UGC review of this tumbler with this creator, ready for TikTok.
---

# UGC product video

It should look like a real person filmed it on a phone: handheld, natural light, an ordinary room, plain speech.

## Ask first

- The product: photos, and what it does for the buyer. If they give a product page and you can read it, take the facts and images from it and show what you took.
- The format, from the table below.
- The creator: their photo, or a generated person. Only use a real person who agreed.

Default to 9:16 and 15 seconds unless they say otherwise. If they want several angles, keep the creator and the product the same and make one video per format or hook.

## Pick the format

| Format | What happens |
| --- | --- |
| Review | A hook, the problem they had, the product in use, one call to action |
| Unboxing | The package, the reveal, close-ups of the best details, a first reaction, one call to action |
| Try-on | A hook, putting it on, how it fits and moves, one styling detail, one call to action |
| How-to | The result first, two or three steps with the product in hand, one call to action |
| App or website | A hook, the problem, the creator holding a phone or laptop showing the product, the outcome, one call to action |

For an app or website, pass a screenshot as a reference. Generated screens rarely stay readable, so keep them brief, or suggest adding a real screen recording in an editor.

## Write the script and show it

About 35 words, with the hook in the first two seconds. Write it the way a person talks. Do not claim results the user cannot back up.

## Plan the shots

Keep the plan to one or two clips. Each model call makes one clip, usually up to 15 seconds.

| Job | Model | Notes |
| --- | --- | --- |
| Creator and product together, with speech | `happyhorse/happyhorse-1.0/reference-to-video` | Takes up to 9 reference images |
| From one image of the creator holding the product | `kling/kling-3.0/pro/image-to-video` | Audio costs more, see the quote |
| Multi-angle, cinematic | `bytedance/seedance-2.0/pro` | Good for product close-ups |

If there is no image of the creator with the product, make one first with `google/nano-banana-2/edit` from the two references. Show it to the user before making video, since video costs far more.

## Steps

1. Show the script, the shot plan and the total price together, and wait for a yes.
2. Make the still first if the plan needs one, then the video. Put the script's exact words in the prompt, with the delivery style.
3. Deliver the clip. RunComfy has no tool for joining clips or burning in captions: if the plan has two clips, hand them over in order, or join them with ffmpeg if you can run commands.
