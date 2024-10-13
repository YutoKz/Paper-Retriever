import streamlit as st

from paper_retriever.home import page_home  
from paper_retriever.ask_llm import page_ask_llm
from paper_retriever.upload import page_upload_paper


def init_page():
    st.set_page_config(
        page_title="論文検索アシスタント",
        page_icon="📖",
    )

def main():
    init_page()

    ## GitHub のリンク
    st.sidebar.page_link("https://github.com/YutoKz/Paper-Retriever/tree/develop", label="GitHub", icon="🐈️")

    page = st.sidebar.radio(
        "Navigation",
        ["Home", "Ask ChatGPT", "Upload Paper"]
    )

    if page == "Home":
        page_home()
    elif page == "Ask ChatGPT":
        page_ask_llm()
    elif page == "Upload Paper":
        page_upload_paper()
        


if __name__ == '__main__':
    main()
