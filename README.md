# The DROID Robot Platform

This repository contains the code for setting up your DROID robot platform and using it to collect teleoperated demonstration data. This platform was used to collect the [DROID dataset](https://droid-dataset.github.io), a large, in-the-wild dataset of robot manipulations.

If you are interested in using the DROID dataset for training robot policies, please check out our [policy learning repo](https://github.com/droid-dataset/droid_policy_learning).
For more information about DROID, please see the following links: 

[**[Homepage]**](https://droid-dataset.github.io) &ensp; [**[Documentation]**](https://droid-dataset.github.io/droid) &ensp; [**[Paper]**](https://arxiv.org/abs/2403.12945) &ensp; [**[Dataset Visualizer]**](https://droid-dataset.github.io/dataset.html).

![](https://droid-dataset.github.io/droid/assets/index/droid_teaser.jpg)

---------
## Setup Guide

We assembled a step-by-step guide for setting up the DROID robot platform in our [developer documentation](https://droid-dataset.github.io/droid).
This guide has been used to set up 18 DROID robot platforms over the course of the DROID dataset collection. Please refer to the steps in this guide for setting up your own robot. Specifically, you can follow these key steps:

1. [Hardware Assembly and Setup](https://droid-dataset.github.io/droid/docs/hardware-setup)
2. [Software Installation and Setup](https://droid-dataset.github.io/droid/docs/software-setup)
3. [Example Workflows to collect data or calibrate cameras](https://droid-dataset.github.io/droid/docs/example-workflows)

If you encounter issues during setup, please raise them as issues in this github repo.

in openpi repo:
uv run scripts/serve_policy.py policy:checkpoint --policy.config=pi05_droid_finetune_lora --policy.dir=checkpoints/pi05_droid_finetune_lora/three-blocks-lora/19999

in droid:
python openpi_inference.py


training:
uv run scripts/train.py pi05_droid_finetune_lora_emg (defined in openpi/train/config.py) --exp-name=three-blocks-full-lora --overwrite


after data collection:
DOCKER: /app/scripts$ python postprocess.py data_dir=/app/data --lab=NECL --do_upload=false

~/temp_droid_data/task2-1$ sudo python3 /home/chopper/droid/droid/postprocessing/util/create_language_annotation_dict.py --metadata=.

uv run examples/droid/convert_droid_data_to_lerobot.py --data_dir /home/chopper/temp_droid_data/task3-1 --repo_name jasontchan/task3-1 --push_to_hub