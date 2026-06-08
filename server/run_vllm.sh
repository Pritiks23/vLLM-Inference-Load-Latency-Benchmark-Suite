#!/bin/bash

python -m vllm.entrypoints.openai.api_server \
  --model mistralai/Mistral-7B-Instruct-v0.2 \
  --host 0.0.0.0 \
  --port 8000 \
  --gpu-memory-utilization 0.75 \
  --max-model-len 2048
