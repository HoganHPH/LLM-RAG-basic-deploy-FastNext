from langchain_community.embeddings import GPT4AllEmbeddings
import os

# Load embedding model from hugging face
def get_embedding_model(checkpoint='models/all-MiniLM-L6-v2-Q5_K_M.gguf'):
    print(os.getcwd())
    embeddings =  GPT4AllEmbeddings(model_name=checkpoint, device="cpu")
    return embeddings