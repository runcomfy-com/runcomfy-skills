---
name: remove-background
title: Remove or replace a background
category: edit
description: Cut a subject out of a video, or swap the background of an image or video. Use for "remove the background", "green screen", "put this on a white background", "change the scene behind me".
example: Remove the background from this talking-head clip and give me a green screen version.
---

# Remove or replace a background

## Pick the model

| Job | Model | Notes |
| --- | --- | --- |
| Video, background removed | `veed/video-background-removal/video-to-video` | Best edges |
| Video, fast draft | `veed/video-background-removal/fast/video-to-video` | Cheaper and quicker, rougher edges |
| Video, green screen output | `veed/video-background-removal/green-screen` | For editing software |
| Image, new scene | `ideogram/ideogram-v3/replace-background` | Describe the new scene in the prompt |
| Image, plain colour | `google/nano-banana-2/edit` | Ask for the exact colour and to keep the subject unchanged |

## Steps

1. Get the file. For an image, ask what should be behind the subject. For a video, ask whether they want it for an editor (green screen) or as a finished clip.
2. Quote it, then run it.
3. Check the output link works, then deliver.

The image models return a filled background, not a transparent PNG. Tell the user that before they pay if they asked for transparency.
