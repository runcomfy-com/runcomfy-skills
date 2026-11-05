---
name: train-lora
title: Train a LoRA
category: training
description: Prepare a dataset and train a LoRA with AI Toolkit on RunComfy. Use for "train a LoRA", "train on my photos", "consistent character", "fine-tune a style".
example: Train a LoRA of my product from these 20 photos.
---

# Train a LoRA

## Prepare

1. Establish the purpose, the base model and the spending limit. Explaining settings alone does not need a dataset or a job.
2. Find the dataset with `list_datasets`, or create one with `create_dataset`. Keep filenames, and match each caption file's name to its image. `upload_dataset_file_from_url` imports from a link, `upload_dataset_text_file` writes a caption, and `get_dataset_upload_urls` gives upload links for local files.
3. Check `get_dataset_status` until it is ready. An accepted upload is not a ready dataset.
4. Write the complete AI Toolkit YAML. `training_folder` is `/app/ai-toolkit/output`, and the dataset `folder_path` is `/app/ai-toolkit/datasets/{dataset_name}`, using the name and not the id.
5. Show the YAML, the GPU, the dataset, the estimated cost and `get_balance`. Start only after the user approves this exact run.

## Run

- Call `submit_training_job` once and keep the job id. A timeout does not justify a second submission: check `get_training_job_status` first.
- Check progress with spacing. Use `cancel_training_job` only if the user asks or an agreed stop condition is met.
- Use `get_training_job_result` and report the real checkpoints and samples. A stopped job is not proof of a good result, so check the steps completed and the samples.
