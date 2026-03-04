# AI Document Assistant (RAG)

An AI-powered document assistant that allows users to upload PDF documents and ask questions in natural language. The system retrieves relevant sections from the document and generates answers using a Retrieval-Augmented Generation (RAG) pipeline.

This project demonstrates how to build an end-to-end AI application using embeddings, vector databases, and large language models.

---

## Features

- Upload PDF documents
- Automatic document chunking
- Embedding generation
- Semantic search using a vector database
- AI-generated answers using LLMs
- Source citations with page numbers
- Conversation memory
- Interactive Streamlit interface

---

## Architecture

The application follows a Retrieval-Augmented Generation architecture.


User Question
↓
Streamlit UI
↓
Retriever
↓
Vector Database (Chroma)
↓
Relevant Document Chunks
↓
Prompt + Context
↓
Large Language Model
↓
Answer + Citations


---

## System Workflow


Upload Document
↓
Document Loader (PyPDF)
↓
Text Chunking
↓
Embeddings Generation
↓
Vector Storage (Chroma)
↓
User Question
↓
Semantic Retrieval
↓
LLM Response Generation
↓
Answer + Source References


---

## Tech Stack

Python  
LangChain  
Streamlit  
OpenAI GPT Models  
Sentence Transformers  
Chroma Vector Database  

---

## Project Structure


rag-document-assistant
│
├── app.py # Streamlit user interface
├── ingest.py # Document ingestion pipeline
├── retrieval.py # Retrieval and answer generation
│
├── data/ # Uploaded documents (ignored by git)
├── vector_store/ # Local vector database
│
├── requirements.txt
└── README.md


---

## Installation

Clone the repository.


git clone https://github.com/YOUR_USERNAME/rag-document-assistant.git


Navigate to the project.


cd rag-document-assistant


Create environment.


conda create -n rag-ai python=3.10
conda activate rag-ai


Install dependencies.


pip install -r requirements.txt


---

## Run the Application

Start the Streamlit interface.


streamlit run app.py


Open your browser at:


http://localhost:8501


---

## Example Usage

1. Upload a PDF document
2. Click **Process Document**
3. Ask questions about the document

Example questions:


What is the document about?
Summarize the key findings.
What recommendations are mentioned?


The assistant retrieves relevant document sections and generates answers with citations.

---

## Example Output


Answer:
The report discusses the impact of transformer models on natural language processing tasks.

Sources:
Page 4
Page 7


---

## Key Concepts Demonstrated

Retrieval-Augmented Generation (RAG)  
Embeddings and semantic search  
Vector databases  
Prompt engineering  
AI application development  
LLM integration  

---

## Future Improvements

Multi-document support  
Hybrid search (keyword + vector search)  
Conversation memory across sessions  
Deployment to cloud platforms  
Advanced retrieval evaluation  

---

## Author

Vijay Vempati  
Data Engineer | AI Systems Builder



