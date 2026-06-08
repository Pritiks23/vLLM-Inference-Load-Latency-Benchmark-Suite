#!/bin/bash

set -e

export CUDA_VISIBLE_DEVICES=0

# Prevent CUDA fragmentation issues
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

python -m vllm.entrypoints.openai.api_server \
  --host 0.0.0.0 \
  --port 8000 \
  --model mistralai/Mistral-7B-Instruct-v0.2 \
  --dtype float16 \
  --gpu-memory-utilization 0.60 \
  --max-model-len 1024 \
  --enforce-eager \
  --disable-log-stats
