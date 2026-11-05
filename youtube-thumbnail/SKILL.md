---
name: youtube-thumbnail
title: YouTube thumbnail
category: content
description: A thumbnail or vertical cover that makes people want to click, with your face or logo if you like. Use for "YouTube thumbnail", "video cover", "Shorts cover", "thumbnail with my face", "a better thumbnail for this video".
example: Make 4 thumbnail options for my video about sailing around the world after quitting my job, using my photo.
---

# YouTube thumbnail

A thumbnail raises a question that only the video answers. It may exaggerate what is in the video, but it must not promise something the video does not deliver.

## Ask first

- The video's title or topic, and what the video really shows.
- Who appears: the user, someone else who agreed, a generated person, or nobody. If the idea needs a person, ask rather than choosing.
- How many options, defaulting to 4, and the shape: 16:9 for YouTube, 9:16 for Shorts, 4:5 for Instagram.

A logo is optional. So is a thumbnail they admire: describe its energy, layout and colours in words, and do not pass it to the model.

## Find the idea

Think of at least five ideas from this list, then offer the best ones in one line each.

| Idea | What it looks like |
| --- | --- |
| Big face | One person filling much of the frame with a clear emotion, and little behind them |
| Mid-action | One intriguing moment from the story, frozen |
| Before and after | Two states of one subject, with as much contrast as possible |
| Progress | Three stages, or a "Day 30" badge from late in the story |
| Scale | A giant thing and a tiny thing that both matter to the story |
| Too many | A frame full of one object, with a person for scale |
| The answer | The product or object that answers the title's question, large and sharp |
| Map | A highlighted route or point on a map or aerial view |
| Landscape | The place is the hero, with one small figure off-centre |
| Chart | One simple, familiar graph with one surprising point |
| Message or news | A made-up, unbranded chat bubble, review or news banner with a short true line |
| One thing exaggerated | One real element of the story made oversized, still plausible |

Test each idea: one clear subject, no clutter, and readable in under a second at about 120 pixels wide.

## Models

| Job | Model |
| --- | --- |
| With a face, logo or other reference, the default | `google/nano-banana/pro/edit` |
| No references | `google/nano-banana/pro/text-to-image` |
| Exact words in the image | `openai/gpt-image-2/edit` |

Use 2K.

## Build the prompt

In this order:

1. **Frame:** a bold, photoreal, poster-like thumbnail in the chosen shape, one continuous image unless the idea needs a split.
2. **Scene:** from what the video really contains.
3. **Text:** "No text, no watermark" by default, since YouTube already shows the title. If they want words, two to four, quoted exactly, large, and clear of the face.
4. **People:** large in the foreground, chest up, about half the frame, faces sharp. For each photo: "Keep this person's face, age and skin tone exactly as in image 1." Name the emotion exactly, such as "eyebrows raised, mouth slightly open, looking past the camera".
5. **Props:** only one or two that explain the idea.
6. **Logo:** its exact shape and colours, away from faces.
7. **Composition:** the hero on one third, a clear difference in scale, strong separation from the background.
8. **Background:** a vivid colour field or simple setting, darker at the edges.
9. **Light and colour:** strong light on the face, soft fill, a bright rim around hair and shoulders. Vivid and high contrast, unless the brief is calm or premium.

## Steps

1. Show the chosen ideas and the total price, and wait for a yes.
2. Give each option its own prompt and its own request. Do not make near-copies.
3. Look at each result when you can. Reject clutter, warped faces and anything unreadable at small size.
4. For changes, use the chosen image as the reference and change only what was asked.
5. Deliver each link with a short label naming the idea.
