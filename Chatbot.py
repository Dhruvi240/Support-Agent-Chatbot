from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings,OllamaEmbeddings
from langchain.chains import RetrievalQA
import streamlit as st

docs_urls=['https://segment.com/docs/',
           'https://docs.mparticle.com/',
           'https://docs.lytics.com/',
           'https://docs.zeotap.com/home/en-us/']
def load_urls(docs_urls):
    documents=[]
    for url in docs_urls:
        loader=WebBaseLoader(url)
        web_docs = loader.load()
        if isinstance(web_docs, list):
            documents.extend(web_docs)
    return documents

def extract_page_content(documents):
    return [doc.page_content for doc in documents if hasattr(doc, 'page_content')]

documents=load_urls(docs_urls)
text_data=extract_page_content(documents)

from langchain.llms import Ollama
from langchain_core.documents import Document
embeddings=OllamaEmbeddings(model='gemma:2b')
document=[Document(page_content=text) for text in text_data]
vector_db=Chroma.from_documents(document,embeddings)
retriever=vector_db.as_retriever()

model=Ollama(base_url='http://localhost:11434',model='gemma:2b')
    chain=RetrievalQA(llm=model,retriever=retriever)
    user_query = st.text_input("Ask a question about CDPs:")
    if st.button("Submit"):
        if user_query:
            response = chain.run(user_query)
            st.write("### Response:")
            st.write(response)
        else:
            st.warning("Please enter a question.")
else:
    st.error("Failed to load documents. Please check the URLs."
