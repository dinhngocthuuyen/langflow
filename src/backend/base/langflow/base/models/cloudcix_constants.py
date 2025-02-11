CLOUDCIX_MODEL_NAMES = [
    "UCCIX-v2-Llama3.1-70B-Instruct",
    "UCCIX-Instruct",
    "GPT-4o",
    "deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
]
CLOUDCIX_EMBEDDING_MODEL_NAMES = [
    "cix_question_encoder",
    "cix_chunk_encoder",
    "dragonplus_question",
    "dragonplus_vector",
    "gte-large-en-v1.5_question_encoder",
    "gte-large-en-v1.5_chunk_encoder",
    "use4",
]
CLOUDCIX_BASE_URL = "https://ml-openai.cloudcix.com"
# Backwards compatibility
MODEL_NAMES = CLOUDCIX_MODEL_NAMES
