# Support-Agent-Chatbot

Overview

This project is an AI-powered Support Agent Chatbot designed to answer "how-to" questions related to Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot extracts relevant information from official documentation using WebBaseLoader and provides structured responses.

**Features**

How-to Question Answering: Retrieves and structures answers from CDP documentation.

Web Scraping for Data Ingestion: Uses LangChain's WebBaseLoader to ingest CDP docs.

Document Indexing for Fast Retrieval: Uses ChromaDB for efficient search.

NLP-Powered Responses: Utilizes Ollama (Gemma:2B model) for conversational AI.

Streamlit UI: Provides a simple, interactive interface.

Tech Stack & Why It Was Chosen

**Backend**

LangChain: Manages document retrieval and conversational AI logic.

Ollama: Used as the LLM (Large Language Model) instead of OpenAI for local inference.

WebBaseLoader: Extracts content from web-based documentation.

ChromaDB: Serves as a vector database for efficient document indexing and retrieval.

**Frontend**
Streamlit: Provides a lightweight, interactive web-based UI for chatbot interaction.

Data Storage

Document Indexer: Structures the extracted text from documentation for faster lookups.

Vector Database (ChromaDB): Stores embeddings for similarity-based searches.

**Data Structures Used**

List of Documents (List[Document])

Stores the extracted web-based content.

**Each document contains:**

page_content: The actual text data.

metadata: Stores source URLs and other relevant information.

Dictionary for Metadata (Dict[str, Any])

Stores metadata associated with each document.

Vector Embeddings (Numpy Arrays)

Used for similarity search in ChromaDB.

Converts text into vector representations for fast retrieval.
