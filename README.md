RAG-based Question Answering System (PDF)

Overview
This project is an AI-powered Question Answering System built using Retrieval-Augmented Generation (RAG). Users can upload PDFs and ask questions about the content.
The system retrieves relevant information from the document and generates accurate, context-aware answers, along with the source text for transparency.
The application combines LangChain, semantic embeddings, Chroma vector database, and Streamlit for an interactive web interface.

Key Features
PDF Document Ingestion: Automatically parses PDFs and splits them into manageable chunks for better comprehension.

Semantic Embeddings & Vector Store: Converts text chunks into embeddings and stores them in ChromaDB for fast and accurate semantic search.

RAG Pipeline: Retrieves relevant chunks and uses a large language model to generate precise answers to user queries.

Interactive Streamlit UI: Users can type questions and receive answers in real-time with a clean and intuitive interface.

Source Document Reference: Every answer is accompanied by the original text snippets to maintain transparency and verify information.

Lightweight & Fast: Efficiently handles medium-sized documents without heavy computation requirements.

Technologies Used
Python

LangChain for RAG pipelines and text processing

HuggingFace / Google Gemini / OpenAI for embeddings and LLM

Chroma Vector Database for semantic retrieval

Streamlit for interactive web interface

PDF Parsing using LangChain PyPDFLoader and RecursiveCharacterTextSplitter


How It Works
Document Loading: PDF is loaded and split into smaller chunks.

Embedding Generation: Chunks are converted into semantic vectors for searching.

Vector Storage: Chunks are stored in ChromaDB for fast retrieval.

Query & Retrieval: User asks a question → top relevant chunks are retrieved.

Answer Generation: LLM generates an accurate answer based on retrieved chunks.

Display in UI: Answer + source text are shown to the user in Streamlit.



Potential Improvements
Support Multiple File Formats: Add CSV, TXT, DOCX support.

File Upload in UI: Allow users to upload their own PDFs dynamically.

Local Embeddings: Switch to HuggingFace embeddings to avoid API quota limits.

Vector Store Caching: Persist vector database to avoid re-generating embeddings each run.

Enhanced Prompt Engineering: Improve domain-specific answer accuracy and reduce hallucinations.

Answer Summarization: Summarize retrieved chunks for concise answers.

Pagination / Searchable Sources: Make source display more readable for long documents.

Multi-LLM Support: Allow switching between Google Gemini, OpenAI GPT, or LLaMA.

Query History in UI: Save user’s previous questions and answers for easy reference.

Advanced Features (Future):

Highlight answers directly in PDFs

Metadata-based semantic search (chapters, authors)

Multi-lingual support



Getting Started
Clone Repository

git clone <your-repo-url>
cd RagApp


Install Dependencies

pip install -r requirements.txt


Run the App

streamlit run QANDN.py


Ask Questions
Open the URL provided by Streamlit in your browser, type your questions, and get answers with sources.



✅ Outcome:
Users can quickly extract knowledge from PDFs without reading the entire document, making it perfect for learning, research, and domain-specific Q&A tasks.



