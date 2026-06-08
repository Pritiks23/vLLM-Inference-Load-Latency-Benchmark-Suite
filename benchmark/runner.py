import asyncio
import pandas as pd
from metrics import RequestMetrics
from load_generator import run_load
from config import CONCURRENCY_LEVELS, PROMPT_SIZES

async def main():
    all_results = []

    for size_name, length in PROMPT_SIZES.items():
        for c in CONCURRENCY_LEVELS:

            print(f"Running: {size_name}, concurrency={c}")

            metrics = RequestMetrics()

            await run_load(c, length, metrics)

            for r in metrics.summary():
                r["concurrency"] = c
                r["prompt_size"] = size_name
                all_results.append(r)

    df = pd.DataFrame(all_results)
    df.to_csv("results/raw_results.csv", index=False)

if __name__ == "__main__":
    asyncio.run(main())
