MODEL_NAME = "meta-llama/Llama-3-8B-Instruct"

BASE_URL = "http://localhost:8000/v1"
API_KEY = "EMPTY"

CONCURRENCY_LEVELS = [1, 2, 4, 8, 16, 32]

PROMPT_SIZES = {
    "short": 50,
    "medium": 200,
    "long": 800
}

MAX_TOKENS = 128
