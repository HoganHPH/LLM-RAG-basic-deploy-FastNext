import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# from llama_cpp import Llama
from langchain_community.llms.llamacpp import LlamaCpp


def get_chat_model(model_file="Phi-3-mini-4k-instruct-q4.gguf"):
    chat_model = LlamaCpp(
        model_path=model_file,
        max_tokens=100,
        top_p=1,
        verbose=False
    )
    return chat_model