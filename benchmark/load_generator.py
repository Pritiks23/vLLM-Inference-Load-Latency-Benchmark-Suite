import asyncio
import time
from openai import AsyncOpenAI
from config import BASE_URL, API_KEY, MAX_TOKENS
from prompts import generate_prompt

client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

async def single_request(prompt, metrics):
    start = time.time()

    stream = await client.chat.completions.create(
        model="meta-llama/Llama-3-8B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=MAX_TOKENS,
        stream=True
    )

    first_token_time = None
    tokens = 0

    async for chunk in stream:
        if first_token_time is None:
            first_token_time = time.time()
        tokens += 1

    end = time.time()

    metrics.log(start, first_token_time or start, end, tokens)

async def run_load(concurrency, prompt_length, metrics):
    tasks = []

    for _ in range(concurrency):
        prompt = generate_prompt(prompt_length)
        tasks.append(single_request(prompt, metrics))

    await asyncio.gather(*tasks)
