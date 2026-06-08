import time

class RequestMetrics:
    def __init__(self):
        self.records = []

    def log(self, start, first_token, end, tokens):
        self.records.append({
            "ttft": first_token - start,
            "total_latency": end - start,
            "tokens": tokens,
            "tokens_per_sec": tokens / (end - start)
        })

    def summary(self):
        return self.records
