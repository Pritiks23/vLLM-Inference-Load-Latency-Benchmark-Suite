# vLLM Inference Load & Latency Benchmark Suite

This project studies how LLM inference systems behave under realistic concurrent load using vLLM.

## Focus Areas

- Time-to-first-token (TTFT)
- End-to-end latency
- Throughput (tokens/sec)
- Concurrency scaling behavior
- Prompt-length sensitivity

## Why this matters

Modern LLM serving systems (CoreWeave, Lambda, etc.) are dominated by:
- batching efficiency
- KV-cache utilization
- tail latency under load

This benchmark explores how these factors interact under controlled stress tests.

## Experiment Design

We vary:
- concurrency: 1 → 32 requests
- prompt sizes: short / medium / long

We measure:
- latency
- throughput
- scaling knee points

## Run

### Start server
```bash
bash server/run_vllm.sh


# ⚡ How to run on Vast.ai (your exact setup)

1. Spin up:
- 1x RTX 4090 or A100

2. Install:
```bash
pip install vllm openai aiohttp pandas matplotlib
Start server:
bash server/run_vllm.sh
Run benchmark:
python benchmark/runner.py
