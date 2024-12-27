import os
import urllib 
import dotenv
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient

from dotenv import load_dotenv
load_dotenv()


def get_vector_store(embeddings):
    ## Config
    MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
    MONGODB_PASSWORD = urllib.parse.quote_plus(os.getenv("MONGODB_PASSWORD"))

    MONGODB_ATLAS_CLUSTER_URI = os.getenv("MONGODB_ATLAS_CLUSTER_URI")
    MONGODB_ATLAS_CLUSTER_URI = MONGODB_ATLAS_CLUSTER_URI.format(MONGODB_USERNAME, MONGODB_PASSWORD)

    ## initialize MongoDB python client
    client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)
    
    MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")
    MONGODB_COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")
    MONGODB_VECTOR_SEARCH_INDEX_NAME = os.getenv("MONGODB_VECTOR_SEARCH_INDEX_NAME")
    MONGODB_COLLECTION = client[MONGODB_DB_NAME][MONGODB_COLLECTION_NAME]

    vector_store = MongoDBAtlasVectorSearch(
        collection=MONGODB_COLLECTION,
        embedding=embeddings,
        index_name=MONGODB_VECTOR_SEARCH_INDEX_NAME,
        relevance_score_fn="cosine",
    )

    return vector_store