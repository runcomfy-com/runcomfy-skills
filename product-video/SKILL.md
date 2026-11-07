---
name: product-video
title: Product video
category: marketing
description: A polished video of a product with no presenter, such as a showcase, a reveal or a TV-style spot. Use for "product video", "product commercial", "TV ad", "animate this product photo", "cinematic shot of my product". Not for a creator talking to camera (ugc-flow).
example: Turn this perfume photo into a 10-second cinematic reveal with a slow camera move.
---

# Product video

## Pick the style

| Style | What it looks like | Length |
| --- | --- | --- |
| Showcase | One slow camera move around the product, a clean background, light travelling across it | 5 to 10 seconds |
| Reveal | Starts hidden or closed, ends on a hero shot | 5 to 10 seconds |
| In use | Hands or a setting showing the product working | 5 to 15 seconds |
| TV-style spot | Two or three shots, a voiceover or music, a closing shot of the product | 15 to 30 seconds |

## Models

| Job | Model | Notes |
| --- | --- | --- |
| From one product photo, the default | `kling/kling-3.0/pro/image-to-video` | Audio costs more, see the quote |
| A set first and last frame | `bytedance/seedance-2.5/first-last-frame/720p` | For reveals and transformations. Make both frames first |
| Several references, several shots in one clip | `bytedance/seedance-2.0/pro` | Good for close-ups |
| A low-cost draft | `bytedance/seedance-2.0-mini/image-to-video` | Try the idea before paying for the final |
| Voiceover | `bytedance/seed-audio-1.0/text-to-audio` | Show the exact words first |
| Music | `acestep-ai/ace-step-1.5/text-to-audio` | Very low cost |

If the photo is plain or poor, make a better frame first with the `product-photoshoot` skill.

## Prompts

Describe the movement, not the picture: the camera (slow push-in, orbit left, tilt up) and what moves (steam rising, liquid pouring, fabric lifting). Use one camera move per shot. Add: "The product keeps its exact shape and label." Labels can warp in motion, and slow moves and short shots help.

## Steps

1. Get the photo, what the video is for, and the shape: 9:16 for social, 16:9 for a website.
2. Write the shot list, with any voiceover word for word, and show it with the total price.
3. For more than one shot, make the first and show it. Then make the rest.
4. Deliver the links in order. RunComfy has no tool for joining clips or mixing audio: join them with ffmpeg if you can run commands, otherwise explain that the user can drop them into any editor in that order.
