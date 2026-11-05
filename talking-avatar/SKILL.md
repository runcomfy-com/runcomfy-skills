---
name: talking-avatar
title: Make a talking avatar
category: content
description: Turn a portrait and a voice into a talking video. Use for "talking head", "AI spokesperson", "avatar video", "make this photo talk", "virtual presenter".
example: Make this portrait present my 20-second product pitch in a warm voice.
---

# Make a talking avatar

Use a portrait of someone who agreed, or a generated character.

## Pick the model

| Input | Model | Notes |
| --- | --- | --- |
| Portrait and audio | `bytedance/omnihuman/v2.0` | The default, full body or portrait |
| Portrait, audio and a direction prompt | `creatify/aurora` | When the delivery needs direction |
| Portrait and speech, quick and low cost | `wan-ai/wan-2-2/speech-to-video` | Good for drafts |
| A built-in presenter and a script | `heygen/avatar-v/text-to-video` | Needs an avatar id and a voice id |

## Steps

1. Get the portrait, and the audio or script. Keep scripts short: about 2.5 words a second.
2. No audio yet: make it with `bytedance/seed-audio-1.0/text-to-audio` or `heygen/heygen-voice/text-to-audio`, and show the user the script first.
3. Quote both steps together, run them in order, deliver the final video and the audio.
