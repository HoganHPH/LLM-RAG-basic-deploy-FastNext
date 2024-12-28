import os
from fastapi import APIRouter
from pydantic import BaseModel
from pathlib import Path

from langgraph.graph import START, StateGraph

from ..RAG_utils import get_embedding_model, get_vector_store, get_chat_prompt, get_chat_model
from ..RAG_utils import State



MODEL_DIR = Path("models")

embeddings_model_name = "all-MiniLM-L6-v2-Q5_K_M.gguf"
checkpoint_embeddings_model = f"{MODEL_DIR}/{embeddings_model_name}"
abs_path_embeddings_model =  os.path.abspath(checkpoint_embeddings_model)
embeddings = get_embedding_model(checkpoint=abs_path_embeddings_model)

vector_store = get_vector_store(embeddings=embeddings)

chat_model_name = "Phi-3-mini-4k-instruct-q4.gguf" 
checkpoint_chat_model = f"{MODEL_DIR}/{chat_model_name}"
abs_path_chat_model =  os.path.abspath(checkpoint_chat_model)
chat_model = get_chat_model(model_file=abs_path_chat_model)

prompt = get_chat_prompt()

class ChatMessage(BaseModel):
    message: str


def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"], k=2)
    return {"context": retrieved_docs}


def generate(state: State):
    docs_content = " ".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = chat_model.invoke(messages)
    return {"answer": response}

# Define Control flow

graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

router = APIRouter()
@router.post('/api/chat')
async def chat_endpoint(message: ChatMessage):
    user_message = message.message
    result = graph.invoke({"question": user_message})
    return {"reply": result['answer']}