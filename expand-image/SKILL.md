---
name: expand-image
title: Expand an image to a new shape
category: edit
description: Extend an image beyond its edges or change its aspect ratio without cropping. Use for "outpaint", "make this square image wide", "fit this to 16:9", "add more space around it".
example: Turn this square product shot into a 16:9 banner by extending the background.
---

# Expand an image to a new shape

## Pick the model

| Job | Model | Notes |
| --- | --- | --- |
| A new size or ratio, same scene | `ideogram/ideogram-v3/reframe` | Set the target resolution |
| Directed extension ("more sky above") | `google/nano-banana-2/edit` | Say which side grows and what appears there |
| Text in the image must stay exact | `openai/gpt-image-2/edit` | Quote the text in the prompt |

## Steps

1. Get the image and the target shape, or where it will be used. Ask only if it is unclear.
2. In an edit prompt, say what stays unchanged first, then what is added and on which side.
3. Quote it, run it, deliver. If the new area looks wrong, offer one retry with a more specific description before changing model.
