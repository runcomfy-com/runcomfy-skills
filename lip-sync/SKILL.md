---
name: lip-sync
title: Sync lips to a voice
category: edit
description: Make a person in an existing video speak a new audio track or script. Use for "lip sync", "dub this video", "make them say this", "translate this video with matching mouth movement".
example: Dub this founder video into Spanish with the mouth matching the new audio.
---

# Sync lips to a voice

Only use footage of someone who agreed to this, and do not make a real person appear to say something they would not.

## Pick the model

| Input | Model | Notes |
| --- | --- | --- |
| Video and audio | `kling/kling/lipsync/audio-to-video` | The default, priced per second |
| Video and audio, for talking-head ads | `creatify/creatify/lipsync` | Same price, try it if the first looks off |
| Video and audio, dubbing | `pixverse/pixverse/lipsync` | Rounded up to the next second |
| Video and a script | `kling/kling/lipsync/text-to-video` | Needs a voice id from its input schema |
| More expressive face, high resolution | `sync/react-1` | Reanimates the face from the audio |

## Steps

1. Get the video and either the audio or the script. If they have a script and want a specific voice, make the audio first with `bytedance/seed-audio-1.0/text-to-audio`.
2. Price is per second of output, so state the length in the quote.
3. Run it and deliver. Tell the user to check the first and last seconds, where sync problems show first.
