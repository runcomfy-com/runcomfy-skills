---
name: unboxing-ugc-skill
title: Unboxing UGC
category: marketing
description: A creator-style unboxing video with a clear reveal and close-up details. Use for "unboxing video", "opening the package", "first look at my product". Not for a review of a product already out of its box (ugc-flow) or a polished reveal with no presenter (product-video).
example: Create a 12-second unboxing of this box of mochi with this creator.
---

# Unboxing UGC

A closed package, a reveal, one close look and an honest first reaction, filmed on a phone close to the table in a place with character. The speech stays plain and the physics stay real.

## Ask first

- The product and its packaging: photos of both if they have them, and what the presenter should point out.
- The creator: their photo, or a generated person. Only use a real person who agreed.

Default to 12 seconds, 9:16 for social and 16:9 for a website.

## Plan the shots

| Shot | What happens |
| --- | --- |
| High angle, looking down | Her hands rest on either side of the closed package, and she looks up and says one line |
| Table height | She opens it or slides the product out, and reacts |
| Chest-up | With one hand she holds the product beside her cheek and says one line |
| Closer | She uses it: a bite, a pour, a first try |
| Chest-up again | She looks into the lens and gives one closing line |

## Write the script and show it

Three short spoken lines, about 15 words in all, the way a person talks. Do not claim results the user cannot back up.

## Make the images first

| Image | Model | Notes |
| --- | --- | --- |
| Product and packaging, if the user has no good photo | `openai/gpt-image-2.5/sunburst/text-to-image` | Keeps the words on the box. Ask for real materials, such as matte printed cardboard and a clear film window |
| Creator, if generated | `bytedance/seedream-5.0-pro/text-to-image` | Waist-up, plain background, sharp |
| Opening frame | `bytedance/seedream-5.0-pro/image-to-image` | Takes the package and the creator, framed as the first shot above |

Show the opening frame to the user before making video, since video costs far more.

## Make the video

Use `bytedance/seedance-2.5/reference-to-video/720p` with the opening frame, the package and the creator as `images`, in that order, and with sound on. Keep the prompt under 150 words:

- One line per shot, in order. Do not describe what the opening frame already shows.
- Put the spoken lines in quotes.
- Say that her whole face stays in frame and that she holds the product with one hand. With two hands, close shots hide her face behind her fingers.
- End with natural delivery, real physics, no music and no captions.

## Check it before you deliver

Look at frames from every shot for a face cut off, extra fingers, a blurred label, a bite or pour that looks wrong, or something that changed between cuts. If a shot is wrong, remake only those seconds instead of the whole clip, and tell the user the added price first.

## Steps

1. Show the shot plan, the script and the total price together, and wait for a yes.
2. Make the images and show the opening frame, then make the video with the script's exact words.
3. Deliver the clip. RunComfy has no tool for joining clips or burning in captions: if you remade part of it, hand the clips over in order, or join them with ffmpeg if you can run commands.
