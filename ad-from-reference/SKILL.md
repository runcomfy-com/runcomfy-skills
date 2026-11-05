---
name: ad-from-reference
title: Video ad from a reference
category: marketing
description: An original video ad for your product that follows the structure of an ad you like. Use for "make an ad like this one", "recreate this ad for my product", "use this video as a reference", "same format, my product".
example: Use this 20-second ad as a reference and make a version for my running shoes.
---

# Video ad from a reference

Take the reference's structure and pacing, and nothing else. No footage, people, logos, words or music from it.

## Ask first

- The reference video, as a file or a public link. Up to 30 seconds is used.
- The product: photos, and what it does for the buyer.
- The length and shape. Default to 15 seconds and 9:16.

## Break the reference down

If you can see the video's frames, write the beats yourself. If you cannot, ask the user to describe it in a few lines, and do not claim you watched it.

For each beat, note the seconds, what is on screen, what is said, and its job: hook, problem, demo, proof or call to action.

Then write the new version beat for beat: the same jobs and timing, with a new script built only on the user's product facts. Show the two side by side.

## Models

| Job | Model | Notes |
| --- | --- | --- |
| Follow a reference clip, with product images | `bytedance/seedance-2.5/reference-to-video/720p` | Up to 3 clips totalling 30 seconds, and 9 images. Reference seconds are billed as well as output seconds |
| A cheap test of the idea | `minimax/minimax-h3-fast/reference-to-video` | One clip and up to 4 images, 5 to 15 seconds |
| No clip, only the beats in words | `happyhorse/happyhorse-1.0/reference-to-video` | Up to 9 images |

## Steps

1. Show the side-by-side, the shot plan and the total price, and wait for a yes. Offer the cheap test first when they are unsure.
2. In the prompt, name each input: the clip sets camera movement and rhythm only, and the image is the product. Put the exact script in the prompt, with how it is delivered.
3. Check that the product looks right and that nothing from the reference's brand came through.
4. Deliver the clip. RunComfy has no tool for joining clips or burning in captions: hand over several clips in order, or join them with ffmpeg if you can run commands.
