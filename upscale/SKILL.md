---
name: upscale
title: Upscale an image or video
category: edit
description: Make an image or video sharper and larger. Use for "upscale", "enhance", "make this 4K", "this looks blurry".
example: Upscale this product photo so it stays sharp on a large print.
---

# Upscale an image or video

## Pick the model

| Input | Model | Good for |
| --- | --- | --- |
| Image | `clarityai/crystal-upscaler` | Photos and renders, keeps detail without inventing a new subject |
| Video, short clip | `community/seedvr2/upscale/video` | Strong detail recovery, priced per second |
| Video, longer or a set output resolution | `bytedance/bytedance/upscale/video` | Priced by output length and resolution tier |

## Steps

1. Get the file and the target: how large, and what it is for. Print and web need different sizes.
2. Quote it. For video, length drives the price, so state the clip length in the quote.
3. Run it, then give back the new file. Say the output size if the result reports it.

Upscaling cannot recover text or faces that are not in the source. Say so when the input is very small.
