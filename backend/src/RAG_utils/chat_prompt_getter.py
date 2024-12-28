from langchain.prompts import PromptTemplate


def get_chat_prompt():
    template = """<|system|>
You are a helpful assistant.<|end|>
<|user|>
Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use only two sentences maximum and always keep the answer as concise as possible. Finish answer by saying "thanks for asking!". Context: {context}. Question: {question}
<|end|>
<|assistant|>
"""
    prompt = PromptTemplate.from_template(template)
    return prompt