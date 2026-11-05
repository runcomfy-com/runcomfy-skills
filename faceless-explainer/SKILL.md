---
name: faceless-explainer
title: Faceless explainer video
category: content
description: A narrated video with no presenter, from a topic or document, in a style you can pick. Use for "faceless video", "explainer", "YouTube Shorts about", "narrated story", "documentary video", "stickman video", "picture story", "children's song video", "turn this article into a video".
example: Make a 45-second faceless explainer about how the Mona Lisa became famous.
---

# Faceless explainer video

## Ask first

- The topic or source text, and the length.
- The look: offer two or three styles from the list below that suit the topic.
- The shape: 9:16 for Shorts and TikTok, 16:9 for YouTube.

## Pick the kind

| Kind | Use it for | How it is built |
| --- | --- | --- |
| Explainer | An idea or a process | One idea per scene, 8 to 10 seconds each, with simple diagrams and no rapid cuts |
| Story or documentary | History, true stories, lists | Shots of 3 to 6 seconds. Vary the distance, angle and place so neighbouring shots differ |
| Picture story | A low budget, or when they ask for stills | One still per narration beat, with slow motion added to some or all of them |
| Children's song | Only when they ask for a song | Lyrics first, with verses and a repeating chorus. Then 10-second scenes showing what the lyrics name, with no lip sync |

## Styles

Write one style description and repeat it word for word in every scene prompt, so the video looks like one piece.

| Style | Description |
| --- | --- |
| Editorial collage | Cream paper with light grain, black-and-white halftone cutouts, torn edges, one accent colour, soft paper shadows |
| Stickman | Simple black line figures with round heads on an off-white page, clear poses, one accent colour |
| Paper diorama | A miniature set of layered card, warm side light, shallow focus, a stop-motion feel |
| Pastel flat | Flat shapes in soft pastel colours, no outlines, friendly and simple |
| Hand drawn | Ink and pencil lines with a light watercolour wash and visible paper, like a sketchbook |
| Fairy tale | Painted 2D scenes, rich jewel colours, warm light against deep shadow, expressive characters |
| Mannequin | Matte clay figures with no faces, simple sets, even neutral light |
| Documentary | Photographic stills, natural light, muted colour, details true to the period |
| Children's 3D | Soft rounded characters, bright colours, simple toy-like sets |

## Plan

1. Write the script at about 2.5 words a second, with a hook in the first line. Stick to facts you can support, and say when something is uncertain.
2. Split it into scenes. For each one, write one line of narration and one line of what is on screen, showing the action the narration names. Keep words out of the pictures unless they ask for them: image models misspell.
3. List recurring characters, places and props. Give each one a short fixed description, and make a reference image for any that appear more than twice.
4. Show the script, the scene list and the total price. Video is most of the cost, so offer a picture story as a cheaper option.

## Make it

| Part | Model |
| --- | --- |
| Voiceover | `bytedance/seed-audio-1.0/text-to-audio` |
| Scene stills, same style throughout | `blackforestlabs/flux-2-klein/9b/text-to-image` |
| Scene stills that must keep a character | `google/nano-banana-2/edit` |
| Moving scenes from stills | `kling/kling-3.0/pro/image-to-video` |
| Moving scenes, lower cost | `bytedance/seedance-2.0-mini/image-to-video` |
| A song or background music | `acestep-ai/ace-step-1.5/text-to-audio` |

Make the voiceover or song first, and fit the scenes to its real length if the result reports it. Make the first scene and show it before making the rest, checking the style, framing, character and movement.

## Deliver

Give the voiceover, then the clips in order with their narration line. RunComfy has no tool for joining clips or adding captions: join them with ffmpeg if you can run commands, otherwise explain that the user can drop them into any editor in that order.
