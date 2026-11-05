---
name: setup-comfyui-workflow
title: Set up a ComfyUI workflow
category: comfyui
description: Have RunComfy install a ComfyUI workflow's custom nodes and models and save it to My Workflows. Use for "set up this workflow", "will this workflow run", "what's missing", "make this workflow work".
example: Set up this workflow JSON on RunComfy and tell me when it's ready to run.
---

# Set up a ComfyUI workflow

1. Get the workflow JSON from the user. A large file: ask them to use `open_upload_window`, then pass the link as `workflow_url`.
2. Call `analyze_workflow`. It is free. Tell the user which custom nodes and models it needs and what is missing. If they only asked what is missing, stop here.
3. Call `start_workflow_setup` without `confirmed_price_usd` to get the quote. Tell the user the price, and that setup usually takes 30 to 60 minutes, or 2 to 3 hours if it needs a different machine type.
4. After they agree, call it again with `confirmed_price_usd` set to the quoted price. Call it once. If a call ends without an answer, check `list_workflow_setups` before trying again.
5. Do not keep polling. Tell the user they can do other things and that RunComfy emails them when it is done. If they stay, call `get_workflow_setup_status` no sooner than its `check_again_in_minutes`.
6. When it is `ready`, offer the next step with the workflow id and version: `create_deployment` to publish it as an API, or the `start-comfyui-machine` skill to open it on a machine. If it is `rejected`, explain the reason and what to change.
