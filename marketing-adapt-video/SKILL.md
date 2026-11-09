---
name: marketing-adapt-video
title: Ad Recreator
category: marketing
description: An original video ad for your product, built on the story and sales structure of a reference ad. Use for "make an ad like this one", "recreate this ad for my product", "use this video as a reference", "same structure, my product", "adapt this ad". Takes no footage, people, words or logos from the reference.
example: Create an original ad for my product using this reference video's persuasion structure.
---

# Ad Recreator

Keep the reference's structure: the order of its shots, their length, framing and camera moves, and the job each one does. Take nothing else from it: no footage, people, places, words, logos or music.

## Ask first

- The reference video, as a file or a public link, 2 to 30 seconds.
- The product: a clean photo, and what it is.
- Where it should be set and who should be in it, if they care. Otherwise pick a new place and new people that suit the product.

## Break the reference down

Look at its frames and write each shot: the seconds, what is on screen and its job, such as the hook on the product, a hand reaching for it, the product in use, a close-up with a person or a closing shot. Then write the new version shot for shot, with the same jobs and timing.

## Make a first frame for each shot

Make one still per shot before any video, with the product exactly as in its photo. Each costs far less than video, so show them first.

| Still | Model | Notes |
| --- | --- | --- |
| Shots with people | `bytedance/seedream-5.0-pro/image-to-image` | Give it the product photo, and the earlier still of the same person so the face stays the same. Ask for a frame from a 35 mm film commercial, real people with natural skin, light film grain and no big smiles. Polished, smooth faces read as fake |
| The product alone | `openai/gpt-image-2.5/sunburst/edit` | Keeps the words on the label exact |

## Make the video

Use `bytedance/seedance-2.5/reference-to-video/720p` with the reference clip in `videos`, and in `images` the first frames in shot order followed by the product photo. With a reference clip, both the reference seconds and the output seconds are billed, so quote it first. Keep the prompt to about 180 words:

- Name the product image, and say the video is a reference for the shots, their order, length, framing and camera moves only, with no people, places, product, words or logos taken from it.
- Say which image opens which shot, and give each shot its length and one line of action.
- End with real people, real physics, the sound you want, no voiceover and no captions.

## Check it before you deliver

Look at frames from every shot: the product and its label unchanged, no extra hands or fingers, and nothing from the reference's brand. If one shot is wrong, remake only that shot, and tell the user the added price first.

## Steps

1. Show the shot-by-shot breakdown, the stills plan and the total price, and wait for a yes.
2. Make the stills and show them, then make the video.
3. Deliver the clip with the breakdown beside it, and offer to change the opening or the offer.
