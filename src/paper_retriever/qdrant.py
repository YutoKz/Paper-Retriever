
import streamlit as st

from langchain.docstore.document import Document
from langchain_core.runnables import RunnablePassthrough # type: ignore
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate

from langchain_qdrant import QdrantVectorStore 
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

QDRANT_PATH = "./local_qdrant"
COLLECTION_NAME = "papers"


def load_local_qdrant(qdrant_path: str = QDRANT_PATH, collection_name: str = COLLECTION_NAME) -> QdrantVectorStore:
    client = QdrantClient(path=qdrant_path)

    # すべてのコレクション名を取得
    collections = client.get_collections().collections
    collection_names = [collection.name for collection in collections]

    # コレクションが存在しなければ作成
    if collection_name not in collection_names:
        # コレクションが存在しない場合、新しく作成します
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=3072, distance=Distance.COSINE),
        )
        print('collection created')

    return QdrantVectorStore(
        client=client,
        collection_name=collection_name, 
        embedding=OpenAIEmbeddings(model="text-embedding-3-large")
    )
