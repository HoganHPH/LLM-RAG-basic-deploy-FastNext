from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_chunks(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100, add_start_index=True
    )
    all_splits = text_splitter.split_documents(docs)
    return all_splits