# RunComfy skills

Ready-made jobs for AI agents that use [RunComfy MCP](https://www.runcomfy.com/mcp). Each skill tells the agent which models to use, what to ask you and how to deliver the result. The agent shows you the plan and the total price, and spends nothing until you agree.

Browse them at [runcomfy.com/skills](https://www.runcomfy.com/skills).

## Use them

Connect RunComfy to your AI app. There is nothing to install: your agent reads the catalog with the `get_skill_instructions` tool and follows the skill that fits. Apps that show MCP prompts list them there too.

[Connection steps](https://www.runcomfy.com/mcp) cover Claude, ChatGPT, Cursor, Claude Code and other MCP apps.

These skills call RunComfy MCP tools such as `quote_model_run` and `run_model`, so they need that connection. For skills that use the RunComfy CLI instead, and for the Claude and Cursor plugin, see [runcomfy-com/skills](https://github.com/runcomfy-com/skills).

## The skills

| Category | Skills |
| --- | --- |
| Marketing | [marketing-research-to-ads](marketing-research-to-ads/SKILL.md), [marketing-adapt-video](marketing-adapt-video/SKILL.md), [marketing-headline-variants](marketing-headline-variants/SKILL.md), [marketing-resize-ads](marketing-resize-ads/SKILL.md), [ad-variants](ad-variants/SKILL.md), [marketplace-images](marketplace-images/SKILL.md), [product-photoshoot](product-photoshoot/SKILL.md), [product-video](product-video/SKILL.md), [ugc-flow](ugc-flow/SKILL.md), [unboxing-ugc-skill](unboxing-ugc-skill/SKILL.md), [try-on-ugc-skill](try-on-ugc-skill/SKILL.md) |
| Content | [faceless-explainer](faceless-explainer/SKILL.md), [talking-avatar](talking-avatar/SKILL.md), [youtube-thumbnail](youtube-thumbnail/SKILL.md) |
| Edit | [edit-image](edit-image/SKILL.md), [edit-video](edit-video/SKILL.md), [expand-image](expand-image/SKILL.md), [face-swap](face-swap/SKILL.md), [lip-sync](lip-sync/SKILL.md), [remove-background](remove-background/SKILL.md), [upscale](upscale/SKILL.md) |
| Audio | [make-audio](make-audio/SKILL.md) |
| ComfyUI | [run-comfyui-workflow](run-comfyui-workflow/SKILL.md), [setup-comfyui-workflow](setup-comfyui-workflow/SKILL.md), [start-comfyui-machine](start-comfyui-machine/SKILL.md) |
| Training | [train-lora](train-lora/SKILL.md) |

## How a skill is written

Each one is `<name>/SKILL.md`. Its frontmatter is flat `key: value` lines:

| Field | What it is for |
| --- | --- |
| `name` | The folder name, and the name agents ask for |
| `title` | The display name |
| `category` | `marketing`, `content`, `edit`, `audio`, `comfyui` or `training` |
| `description` | One sentence, then `Use for "..."` with phrases people really say. Add `Not for ... (other-skill)` when another skill is the better fit |
| `example` | A prompt someone could paste |

[`_rules.md`](_rules.md) is added to the end of every skill: the price comes first, how to write prompts, and what never to invent.

## Changing a skill

1. Edit the skill, then run `python scripts/validate.py`.
2. Check every model id against the live catalog, with `get_model` or `list_models`.
3. After merging, the MCP server picks up the change when it moves to the new commit of this repository and deploys.
4. If a name, title, category, description, example or model changed, run `python scripts/export-catalog.py` and update the website's copy.

## License

[MIT](LICENSE)
