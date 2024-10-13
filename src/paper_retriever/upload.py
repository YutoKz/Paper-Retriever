import streamlit as st

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore 

from PyPDF2 import PdfReader
from .qdrant import load_local_qdrant


def get_pdf_texts() -> list[str]:
    uploaded_file = st.file_uploader(
        label='Upload your PDF here😇',
        type='pdf'
    )
    if uploaded_file:
        pdf_reader = PdfReader(uploaded_file)
        text = '\n\n'.join([page.extract_text() for page in pdf_reader.pages])
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            model_name="text-embedding-3-large",  # text-embedding-ada-002
            chunk_size=1000,
            chunk_overlap=0,
        )

        return text_splitter.split_text(text)
    else:
        return None
    
def upload_texts(texts: list[str], metadata: dict[str, str] = {}):
    qdrant: QdrantVectorStore = load_local_qdrant()
    qdrant.add_texts(texts, metadatas=[metadata for _ in texts]) # type: ignore


# --------------------------------------------------------------------------------------

def page_upload_paper():
    st.title("Upload Paper")
    with st.container():
        st.markdown("未実装")
        pdf_url = st.text_input("PDF URL")
        # これ以降、arxiv sumarizerから引用

    with st.container():
        pdf_texts: list[str] = get_pdf_texts()
        if pdf_texts:
            with st.spinner("Uploading..."):
                upload_texts(pdf_texts, metadata={"type": "paper"})