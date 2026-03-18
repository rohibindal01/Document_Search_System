# 🤖 Agentic RAG Document Search System

## 📌 Project Overview

This project is an **Agentic Retrieval-Augmented Generation (RAG) system** built with a **Streamlit UI** that allows users to ask questions over a set of documents (fetched from URLs).

It processes documents, converts them into embeddings, stores them in a vector database, and uses an LLM-powered agent to retrieve and generate accurate answers.

---

## 🔄 Basic Flow of the Project

1. **Application Startup**
   - The Streamlit app (`streamlit_app.py`) initializes the UI.
   - Session state is prepared to store system state and history.

2. **System Initialization**
   - LLM is loaded using configuration settings.
   - Documents are fetched from predefined URLs.
   - Documents are split into chunks.

3. **Data Processing**
   - Processed documents are embedded.
   - Embeddings are stored in a vector database.

4. **Graph Construction (Agentic RAG)**
   - A graph-based pipeline is built using:
     - Retriever (Vector Store)
     - LLM
   - This enables intelligent query handling.

5. **User Query Flow**
   - User enters a question in the UI.
   - Query is passed to the RAG system.
   - Relevant documents are retrieved.
   - LLM generates a final answer.

6. **Response Display**
   - Answer is shown in the UI.
   - Source documents are displayed.
   - Query history is maintained.

---

## 🛠️ Technologies Used

### 👨‍💻 Frontend
- Streamlit (Interactive UI)

### 🧠 AI / ML
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Embeddings

### ⚙️ Backend Components
- Python
- Custom Modular Architecture:
  - `DocumentProcessor`
  - `VectorStore`
  - `GraphBuilder`
  - `Config`

### 📦 Data Handling
- Document chunking
- URL-based document ingestion

### 🗄️ Storage
- Vector Database (for embeddings & retrieval)

---

User (Streamlit UI)
│
▼
Query Input
│
▼
RAG Agent (GraphBuilder)
├──► Vector Store (Retriever)
│        │
│        ▼
│   Document Embeddings
│        │
│        ▼
│   Document Processor
│        │
│        ▼
│   Source URLs
│
└──► LLM (Answer Generator)
         │
         ▼
     Final Answer

---

## 📄 Detailed Project Information

### 🔧 Core Components

#### 1. Config
- Handles:
  - LLM initialization
  - Default URLs
  - Chunk size & overlap

#### 2. DocumentProcessor
- Fetches documents from URLs
- Splits into manageable chunks for embedding

#### 3. VectorStore
- Converts document chunks into embeddings
- Stores them for similarity search
- Provides retriever interface

#### 4. GraphBuilder
- Builds an **agentic pipeline**
- Connects:
  - Retriever
  - LLM
- Executes query flow using `.run()`

---

### 🔍 Key Features

- ✅ Ask questions over documents  
- ✅ Automatic document ingestion from URLs  
- ✅ Semantic search using embeddings  
- ✅ Source document transparency  
- ✅ Query history tracking  
- ✅ Fast responses with caching (`@st.cache_resource`)

---

### 🧑‍💻 User Interface

- Clean Streamlit interface
- Input form for queries
- Expandable source document viewer
- Response time tracking
- Search history display

---

## 🚀 How It Works (In Simple Terms)

1. Load documents from the internet  
2. Break them into small chunks  
3. Convert chunks into embeddings  
4. Store embeddings in a vector database  
5. When user asks a question:
   - Find similar chunks
   - Send them to the LLM
   - Generate a precise answer  
