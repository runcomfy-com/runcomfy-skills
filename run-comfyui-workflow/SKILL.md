---
name: run-comfyui-workflow
title: Run a ComfyUI workflow as an API
category: comfyui
description: Publish a workflow as a Serverless API and run it. Use for "run my workflow", "deploy this workflow", "call my deployment", "serverless ComfyUI".
example: Run my portrait workflow with this prompt and give me the image.
---

# Run a ComfyUI workflow as an API

## Find or publish the deployment

1. Call `list_deployments`. Use `get_deployment` with `include_payload: true` to read the real inputs and node ids. Never guess which node holds the prompt, seed or image.
2. No deployment yet: find the workflow with `list_my_workflows`, then call `create_deployment` with its id and version, after telling the user the hardware and cost settings. `min_instances` above 0 charges while idle, so keep it at 0 unless they ask.

## Run it

1. Show the overrides you will send and the available price information. Check `get_balance`.
2. Call `submit_request` once and keep the request id. A timeout does not mean it failed: check `get_request_status` before submitting again.
3. Check `get_request_status` with spacing, then get `get_request_result` and return the output links.

These request tools are for deployments. Hosted models use `get_model_request_status` and `get_model_request_result`. Do not delete a deployment as cleanup unless the user asks.
