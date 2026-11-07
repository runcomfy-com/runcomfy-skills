---
name: try-on-ugc-skill
title: Try-on UGC
category: marketing
description: A creator-style try-on video that shows how an outfit looks and fits. Use for "try-on video", "outfit video", "get ready with me", "how this fits", "fashion UGC". Not for a review of a product that is not worn (ugc-flow) or for changing clothes in a photo (edit-image).
example: Create a 12-second try-on of this outfit with this creator.
---

# Try-on UGC

The change is the point: the creator shows the clothes, the viewer sees them up close, then she is wearing them and they move. The speech stays plain and the physics stay real.

## Ask first

- The outfit: a photo laid flat or on a hanger, plus anything worn with it, and what should stand out, such as the fit, the fabric or one detail.
- The creator: their photo, or a generated person. Only use a real person who agreed.

Default to 12 seconds, 9:16 for social and 16:9 for a website.

## Plan the shots

| Shot | What happens |
| --- | --- |
| Selfie at arm's length | In a plain T-shirt, she holds the top on a hanger beside her face and says one line |
| Looking down at the bed | The whole outfit is laid out with the shoes and accessories. One hand lifts a hem or touches a detail, and she says one line |
| Whole body, phone on the floor | She now wears everything. She turns so the fabric moves, then looks at the lens and gives one closing line |

## Write the script and show it

Three short spoken lines, about 15 words in all, the way a person talks. Do not claim results the user cannot back up.

## Make the images first

Make one still for each shot, so the clothes and the room stay the same. Each one costs far less than video, so show them to the user first.

| Image | Model | Notes |
| --- | --- | --- |
| Outfit, if the user has no good photo | `openai/gpt-image-2.5/sunburst/text-to-image` | A flat lay from above, with the fabric texture visible |
| Creator, if generated | `bytedance/seedream-5.0-pro/text-to-image` | Head and shoulders in a plain T-shirt, sharp |
| The three shots | `bytedance/seedream-5.0-pro/image-to-image` | Give it the outfit and the creator. Make the selfie first, then use it as a reference for the whole-body still so the room matches |

## Make the video

Use `bytedance/seedance-2.5/reference-to-video/720p` with the three stills, the outfit and the creator as `images`, in that order, and with sound on. Keep the prompt under 150 words:

- Say which image opens which shot, and give each shot its length.
- Say what moves in one line per shot. Do not describe what the stills already show.
- Put the spoken lines in quotes.
- Keep the camera still in the second and third shots.
- End with natural delivery, real physics, no music and no captions.

## Check it before you deliver

Look at frames from every shot for a head cut off, extra fingers, a detail that changed, such as buttons or a hem, or clothes that are different between shots. A mirror in the room may not show her, so keep it out of frame if that matters to the user. If a shot is wrong, remake only those seconds instead of the whole clip, and tell the user the added price first.

## Steps

1. Show the shot plan, the script and the total price together, and wait for a yes.
2. Make the images and show them, then make the video with the script's exact words.
3. Deliver the clip. RunComfy has no tool for joining clips or burning in captions: if you remade part of it, hand the clips over in order, or join them with ffmpeg if you can run commands.
