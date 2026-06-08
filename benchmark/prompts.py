import random

def generate_prompt(length: int):
    words = [
        "system", "latency", "throughput", "GPU", "inference",
        "batching", "memory", "attention", "token", "server",
        "scaling", "architecture", "optimization"
    ]
    return " ".join(random.choices(words, k=length))
