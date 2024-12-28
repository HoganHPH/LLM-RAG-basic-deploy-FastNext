import os
from pathlib import Path


from document_loader import load_documents
from document_splitter import split_chunks
from embeddings_getter import get_embedding_model
from vector_store_getter import get_vector_store
from chat_model_getter import get_chat_model
from chat_prompt_getter import get_chat_prompt
from state import State
from langgraph.graph import START, StateGraph
from langchain_huggingface import HuggingFaceEmbeddings
from llama_cpp import Llama
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate


MODEL_DIR = Path("models")
embeddings_model_name = f"W:/CODE_EVERYTHING/PROJ/RAG-basic-deploy-FastNext/backend/models/all-MiniLM-L6-v2-Q5_K_M.gguf"
embeddings = get_embedding_model(checkpoint=embeddings_model_name)

vector_store = get_vector_store(embeddings=embeddings)

chat_model_name = "W:/CODE_EVERYTHING/PROJ/RAG-basic-deploy-FastNext/backend/models/Phi-3-mini-4k-instruct-q4.gguf" 
chat_model = get_chat_model(model_file=chat_model_name)


# answer = chat_model.create_chat_completion(messages)
# print(answer)

question = "When did the United States declare its independence?"


retrieved_docs = vector_store.similarity_search(question, k=1)

# print("\n\n==============")
# print(retrieved_docs)
# print("\n\n==============")

# template = """
# <|system|>
# You are a helpful assistant.<|end|>
# <|user|>
# Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum and keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
# Context: {context}
# Question: {question}
# Helpful Answer:
# <|end|>
# <|assistant|>
# """

# template = "<|user|>\nHow many days in January?<|end|>\n<|assistant|>"

# messages = [
#     {"role": "system", "content": "You are a helpful assistant"},
#     {
#         "role": "user",
#         "content": [
#             {"type" : "text", "text": "Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum and keep the answer as concise as possible. Always say 'thanks for asking!' at the end of the answer."},
#             {"type": "text", "question": question},
#             {"type": "text", "context":  retrieved_docs}
#         ]
#     }
# ]

# prompt = PromptTemplate.from_template(template)

# messages = prompt.invoke({"question": question, "context": retrieved_docs})
# print("\n\n============")
# print(messages)
# print("\n\n============")

template = """<|system|>
You are a helpful assistant.<|end|>
<|user|>
Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum and keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. Context: {context}. Question: {question}
Helpful Answer:
<|end|>
<|assistant|>
"""
prompt = PromptTemplate.from_template(template)
docs_content = " ".join(doc.page_content for doc in retrieved_docs)

# print(docs_content)



# docs_content = "My name is Hoang. I have 2 sisters. The first sister's name is Mai. The name of the second is Trang"
# question = "What is the name of the first sister?"

message = prompt.invoke({"context": docs_content, "question": question})
print(message)
response = chat_model.invoke(message)
print(response)




# prompt = get_chat_prompt()
# messages = prompt.invoke({"question": "what is the meaning of life?", "context": ""})
# answer = chat_model.create_chat_completion(messages)
# print(answer)

# results = vector_store.similarity_search(
#     "What was adopted in 1789?"
# )

# print(results)



# def retrieve(state: State):
#     retrieved_docs = vector_store.similarity_search(state["question"])
#     return {"context": retrieved_docs}


# def generate(state: State):
#     docs_content = "\n\n".join(doc.page_content for doc in state["context"])
#     messages = prompt.invoke({"question": state["question"], "context": docs_content})
#     print(messages)
#     response = chat_model.invoke(messages)
#     return {"answer": response.content}


# graph_builder = StateGraph(State).add_sequence([retrieve, generate])
# graph_builder.add_edge(START, "retrieve")
# graph = graph_builder.compile()

# result = graph.invoke({"question": "When did the United States declare its independence?"})
# print(f'\n\nAnswer: {result["answer"]}')