import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../results/raw_results.csv")

# Latency vs concurrency
for size in df["prompt_size"].unique():
    subset = df[df["prompt_size"] == size]
    grouped = subset.groupby("concurrency")["total_latency"].mean()

    plt.plot(grouped.index, grouped.values, label=size)

plt.xlabel("Concurrency")
plt.ylabel("Latency (s)")
plt.title("vLLM Latency vs Concurrency")
plt.legend()
plt.show()
