---
name: edit-video
title: Edit a video
category: edit
description: Change something in an existing clip, restyle it, or make it longer. Use for "change the jacket in this video", "remove this from the video", "restyle this clip", "change this video to 9:16", "make this video longer". Not for swapping a person (face-swap) or new speech (lip-sync).
example: In this clip, change the white teapot to a red one and keep everything else the same.
---

# Edit a video

## Pick the model

| Job | Model | Notes |
| --- | --- | --- |
| Change or remove one thing, the default | `kling/kling-v4/video-edit` | A source of 3 to 30 seconds. Call it @Video1 in the prompt |
| A new style, outfit or object, with reference images | `happyhorse/happyhorse-1.0/video-edit` | Up to 5 reference images |
| A new shape, or a low-cost rework | `bytedance/seedance-2.0-mini/video-to-video` | It regenerates the clip, so check the product and any text |
| Longer, continuing from the last frame | `google-deepmind/veo-3-1/fast/extend-video` | Audio costs more |
| Longer, as a low-cost draft | `pixverse/pixverse-v6/extend` | Good for testing the direction |

## Writing the prompt

Name the one change, then what stays: "Change only the jacket to dark green. Keep the person, the movement, the background, the light and the camera." Say what should happen to the sound. To make a clip longer, describe what happens next.

## Steps

1. Get the clip and the change. If the request could mean two things, ask one question.
2. State the source length and the output length in the quote. Most of these bill both, so a long source costs more even for a short result.
3. Offer 720p as a cheaper first pass where the model has it.
4. Deliver, and tell the user to check hands, faces and text first, where edits show.
