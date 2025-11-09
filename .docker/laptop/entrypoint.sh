#!/bin/bash

# # activate conda
# source ~/miniconda3/bin/activate
# conda activate robot

# # run user command
# exec "$@"

set -euo pipefail

CMD=("$@")

# Load conda into the current shell the modern way
eval "$($HOME/miniconda3/bin/conda shell.bash hook)"
conda activate robot

exec "${CMD[@]}"

