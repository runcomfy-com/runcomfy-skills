---
name: remove-background
title: Remove or replace a background
category: edit
description: Cut a subject out of a video, or swap the background of an image or video. Use for "remove the background", "green screen", "put this on a white background", "change the scene behind me".
example: Remove the background from this talking-head clip and give me a file with transparency for my editor.
---

# Remove or replace a background

## Pick the model

| Job | Model | Notes |
| --- | --- | --- |
| Video, background removed | `veed/video-background-removal/video-to-video` | Best edges |
| Video, fast draft | `veed/video-background-removal/fast/video-to-video` | Cheaper and quicker, rougher edges |
| Video filmed in front of a green screen | `veed/video-background-removal/green-screen` | Only for footage that already has a green background |
| Image, new scene | `ideogram/ideogram-v3/replace-background` | Describe the new scene in the prompt |
| Image, plain colour | `google/nano-banana-2/edit` | Ask for the exact colour and to keep the subject unchanged |

## Steps

1. Get the file. For an image, ask what should be behind the subject. For a video, ask whether it was filmed in front of a green screen.
2. For video, set the output codec to vp9. That gives one WebM file with transparency, which editing software can use. With the default, h264, the result looks like the subject on black.
3. Quote it, then run it.
4. Check the output link works, then deliver.

The video models remove the background but cannot put a colour or a scene behind the subject, so they cannot make a solid green version. If the user asks for one, say so before they pay and offer the file with transparency.

The image models return a filled background, not a transparent PNG. Tell the user that before they pay if they asked for transparency.
