---
name: face-swap
title: Swap a face or character
category: edit
description: Put one person's or character's identity into an image or video. Use for "face swap", "put my face on this", "replace the actor", "same pose, different person".
example: Replace the presenter in this video with my character, keeping the motion the same.
---

# Swap a face or character

## Check consent first

Ask whether the user has the right to use both the face and the source material. Refuse a real person's likeness without their consent, anything sexual, anything involving a minor, and anything meant to deceive people about who said or did something. Remind the user that some platforms require a label on synthetic media.

## Pick the model

| Job | Model | Notes |
| --- | --- | --- |
| Video, whole character follows the source motion | `community/wan-2-2/animate/video-to-video` | Needs a reference image and a source video |
| Still image, one identity restaged | `heygen/heygen-image/identity-remix` | Keeps the face and changes pose, clothes and light |
| Still image, precise composition | `openai/gpt-image-2/edit` | Give the face and the target as references |

## Steps

1. Get the face image and the target image or video.
2. For a still edit prompt, say: keep the target's pose, framing, clothes and lighting, and take only the face from the reference.
3. Quote it, run it, deliver. Say the result is synthetic if the user plans to publish it.
