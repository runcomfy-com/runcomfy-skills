---
name: start-comfyui-machine
title: Start a ComfyUI machine
category: comfyui
description: Open one of your workflows on a ComfyUI machine, after you approve it. Use for "start a machine", "open my workflow", "run ComfyUI", "I need a GPU".
example: Start a large machine for my portrait workflow for one hour.
---

# Start a ComfyUI machine

These tools appear when the user allowed machine control while connecting. If they are missing, ask the user to reconnect RunComfy and tick it.

1. Find the workflow with `list_my_workflows`, and check `list_machines` for one already running.
2. Pick the smallest machine and time limit that fit the job. Ask if you cannot tell.
3. Call `request_machine_start`. Nothing starts yet, and you cannot approve it: the user answers on a card in the conversation, or at `approve_url` in an app that cannot show cards. Tell them the most it can cost.
4. After they answer, call `get_machine_start_request`. Once it has started, use `get_machine` to see when ComfyUI is ready, and give the user the link.

## Working on the machine

- `get_machine_nodes` lists what is installed, or one node's inputs. Read it before writing a prompt.
- `run_on_machine` queues a prompt in ComfyUI's API format. `get_machine_queue` shows what is running and `get_machine_history` gives the outputs.
- To keep the machine's nodes and models, call `save_machine_workflow`, then `get_workflow_save_status`. Do not stop the machine until it says `saved`.

Installing custom nodes and restarting ComfyUI are not available through these tools. Ask the user to do that in the ComfyUI window.

## Stopping

Machines cost money while they run. If nothing stops a machine, it runs to its time limit, even after the conversation has ended, so choose a limit that fits the job. On the last prompt of a job, pass `stop_when_done: true` to `run_on_machine`: the machine stops about a minute after its queue is empty, and the user gets an email. Leave it off while more prompts may follow, or while the user is working in the ComfyUI window, because a stopped machine loses unsaved changes and needs a new approval. Otherwise offer `stop_machine` when the work is done, which is allowed at any time.
