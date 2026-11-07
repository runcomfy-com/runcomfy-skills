---
name: ugc-flow
title: Product review UGC
category: marketing
description: A creator-style product review, from concept and script to a finished clip. Use for "UGC video", "product review video", "tutorial ad", "TikTok ad", "creator showing my app". Not for opening a package (unboxing-ugc-skill), trying on clothes (try-on-ugc-skill), a polished video with no presenter (product-video) or an avatar reading a script with no product in hand (talking-avatar).
example: Create a 12-second review of this soda with this creator.
---

# Product review UGC

A review people stop for: one moment only this product can cause, filmed from a phone on the table, with the product in the middle of the frame and a room with a clear color idea. The speech stays plain and the physics stay real.

## Ask first

- The product: photos, and what it does for the buyer. If they give a product page and you can read it, take the facts and images from it and show what you took.
- The format, from the table below.
- The creator: their photo, or a generated person. Only use a real person who agreed.

Default to 12 seconds, 9:16 for social and 16:9 for a website. If they want several angles, keep the creator and the product the same and make one video per format or hook.

## Pick the format

| Format | What happens |
| --- | --- |
| Review | One moment with the product, the creator's real reaction, the product in use, one closing line |
| How-to | The result first, two or three steps with the product in hand, one closing line |
| App or website | A hook, the problem, the creator holding a phone or laptop showing the product, the outcome, one closing line |

For an app or website, pass a screenshot as a reference. Generated screens rarely stay readable, so keep them brief, or suggest adding a real screen recording in an editor.

## Find the moment

Pick one believable thing that happens to this product in the first four seconds: a soda that foams over when it is opened, a spray that catches the light, a lid that will not come off. Keep its size ordinary, and say how big it is in the prompt, or the model makes it huge.

## Write the script and show it

Three short spoken lines, about 20 words in all, the way a person talks. Do not claim results the user cannot back up.

## Make the images first

| Image | Model | Notes |
| --- | --- | --- |
| Product, if the user has no good photo | `openai/gpt-image-2.5/sunburst/text-to-image` | Keeps the words on the label. Ask for real materials, such as transparent glass and liquid you can see through. Flat saturated color and water drops look pasted on |
| Creator, if generated | `bytedance/seedream-5.0-pro/text-to-image` | Waist-up, plain background, sharp |
| Opening frame | `bytedance/seedream-5.0-pro/image-to-image` | Takes the product and the creator, with the framing below |

For the opening frame, describe a phone resting on the table: ultra-wide, level with the table, deep focus. The product stands in the center at about 40% of the frame's height, lit by the same light as the room, with a reflection and a contact shadow. The creator's whole head is in frame with space above it. Show this frame to the user before making video, since video costs far more.

## Make the video

Use `bytedance/seedance-2.5/reference-to-video/720p` with the opening frame, the product and the creator as `images`, in that order, and with sound on. Keep the prompt under 150 words:

- One line per shot, in order. Do not describe what the opening frame already shows.
- Put the spoken lines in quotes.
- Say that her whole face and her hand on the product stay in frame. Without it, close shots cut off the face and the product floats with no hand.
- Say how many hands she uses.
- End with natural delivery, real physics, no music and no captions.

## Check it before you deliver

Look at frames from every shot for a face cut off, extra fingers, a blurred label, or something that changed between cuts, such as a cap back on an opened bottle. If a shot is wrong, remake only those seconds instead of the whole clip, and tell the user the added price first.

## Steps

1. Show the moment, the script and the total price together, and wait for a yes.
2. Make the images and show the opening frame, then make the video with the script's exact words.
3. Deliver the clip. RunComfy has no tool for joining clips or burning in captions: if you remade part of it, hand the clips over in order, or join them with ffmpeg if you can run commands.
