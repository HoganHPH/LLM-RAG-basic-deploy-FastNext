from langchain_community.document_loaders import PyPDFLoader


def load_documents(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs