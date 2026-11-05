---
name: edit-image
title: Edit an image
category: edit
description: Change part of an existing image while keeping the rest. Use for "remove this object", "change the colour", "rewrite the headline", "fix this area", "relight this".
example: Remove the cup from the table in this photo and keep everything else the same.
---

# Edit an image

## Pick the model

| Job | Model | Notes |
| --- | --- | --- |
| General edit, up to 20 reference images | `google/nano-banana-2/edit` | The default. Keeps people and products recognisable |
| Text inside the image, layout, several references | `openai/gpt-image-2/edit` | Quote new text exactly |
| One precise change to one image | `blackforestlabs/flux-1-kontext/pro/edit` | Strong at local changes |
| An exact area, with a mask image | `tongyi-mai/z-image/turbo/inpainting` | Needs a mask link from the user |
| New lighting | `qwen/qwen-edit-2509/lora/relight` | Describe the light source and direction |

## Writing the prompt

State what must stay the same before what changes: "Keep the person, pose and framing unchanged. Replace the background with a rainy street at night." Use positions the model can follow, like "upper right" or "the cup on the left". One change per run gives more control than many at once.

## Steps

1. Get the image and the change. If the request could mean two things, ask one question.
2. Quote it, run it, deliver. For a retry, change the prompt before changing the model.
