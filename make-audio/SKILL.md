---
name: make-audio
title: Make music or a voiceover
category: audio
description: Generate a song, background music or spoken audio. Use for "make a song", "background music", "jingle", "voiceover", "read this aloud", "extend this track".
example: Make a 30-second upbeat instrumental for my product video.
---

# Make music or a voiceover

## Pick the model

| Job | Model | Notes |
| --- | --- | --- |
| Music, the default | `acestep-ai/ace-step-1.5/text-to-audio` | Styles as tags, optional lyrics, very low cost |
| Polished vocals, commercial use | `elevenlabs/elevenlabs/music-generation` | Costs much more, offer it when quality matters most |
| Lengthen a track | `acestep-ai/ace-step/audio-outpaint` | Set which end grows and by how much |
| Redo one section of a track | `acestep-ai/ace-step/audio-inpaint` | Give the time range |
| Speech | `bytedance/seed-audio-1.0/text-to-audio` | Natural speech from text |
| Speech in a listed voice | `heygen/heygen-voice/text-to-audio` | Needs a voice id |

## Steps

1. Get the mood, length and use. For music with words, write the lyrics with section markers and show them first.
2. Describe music by genre, tempo, instruments and mood. Do not ask for a living artist's voice or style by name.
3. Quote it, run it, deliver the link. For a voiceover, show the exact script before running it.
