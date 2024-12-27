import os
from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path

from ..RAG_utils import load_documents, split_chunks, get_embedding_model, get_vector_store


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)  # Ensure the upload directory exists

MODEL_DIR = Path("models")

router = APIRouter()
@router.post('/api/indexing')
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = UPLOAD_DIR / file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        docs = load_documents(file_path)
        
        all_splits = split_chunks(docs)
        
        embeddings_model_name = "all-MiniLM-L6-v2-Q5_K_M.gguf"
        checkpoint_embeddings_model = f"{MODEL_DIR}/{embeddings_model_name}"
        abs_path =  os.path.abspath(checkpoint_embeddings_model)
        embeddings = get_embedding_model(abs_path)
        
        vector_store = get_vector_store(embeddings=embeddings)
        reset_vector_store = vector_store.collection.delete_many({})
        document_ids = vector_store.add_documents(documents=all_splits)
        
        return JSONResponse(content={"message": f"Number of documents in vector store: {len(document_ids)}"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": f"An error occurred: {e}"}, status_code=500)