#!/bin/bash

python -m vllm.entrypoints.openai.api_server \
  --model microsoft/Phi-3-mini-4k-instruct \
  --host 0.0.0.0 \
  --port 8000 \
  --gpu-memory-utilization 0.50 \
  --max-model-len 1025
