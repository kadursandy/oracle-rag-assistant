
# 🚀 OCI (Oracle Cloud Infrastructure) RAG Assistant
### Enterprise-Grade Agentic RAG Platform
OCI (Oracle Cloud Infrastructure) is an enterprise-grade conversational AI platform that scrapes Oracle Cloud documentation, converts it into vector embeddings, and delivers context-aware answers using Retrieval-Augmented Generation (RAG).
An enterprise-ready Retrieval-Augmented Generation (RAG) system built using FastAPI, PostgreSQL (pgvector), Docker, and modern AI architecture principles.

It helps OCI developers to quicky ask questions, get answers and understand OCI documentation
---

## 💬 Sample Conversation

See a real example here:  
👉 [Sample Chat Output](./chat-response.md)


## 🎯 Project Objective

Build a scalable conversational AI system capable of:

- Scraping Oracle Cloud Infrastructure documentation
- Generating embeddings
- Storing vectors in PostgreSQL (pgvector)
- Performing semantic similarity search
- Generating contextual responses via LLM
- Supporting session-based conversation memory
- Providing streaming API responses
- Running fully containerized

---

## 🏗 Architecture Overview

Streamlit UI  
↓  
FastAPI Backend (/chat, /chat-stream)  
↓  
Agentic RAG Engine  
↓  
Embedding Model (1536-dim vectors)  
↓  
PostgreSQL + pgvector  
↓  
LLM Response Generation

---

## 🔥 Key Features

✅ FastAPI REST APIs  
• `/chat` — Standard response  
• `/chat-stream` — Streaming token response

✅ Agentic RAG  
• Question embedding  
• Vector similarity search  
• Context assembly  
• Grounded LLM response

✅ PostgreSQL + pgvector  
• 1536-dimension embedding storage  
• Cosine similarity search

✅ Web Scraping Engine  
BASE_URL = "https://docs.oracle.com/en-us/iaas/Content/services.htm"  
MAX_DEPTH = 3

✅ Recursive Chunking  
• 800 token chunk size  
• 150 token overlap

✅ Conversation Memory  
• Session-based  
• Stored in PostgreSQL

✅ Docker Deployment  
• Multi-service docker-compose  
• DB health checks  
• Reproducible environment

---

## 🛠 Technology Stack

- Python 3.11
- FastAPI
- Streamlit
- PostgreSQL
- pgvector
- LangChain
- OpenAI API
- Docker

---

## 🚀 Getting Started

### 1️⃣ Create .env file

OPENAI_API_KEY=your_api_key_here

---

### 2️⃣ Start Services

docker-compose up --build

---

### 3️⃣ Ingest Oracle Documentation

docker exec -it oracle-rag-assistant-v12-app-1 python -m ingestion.run_ingestion

---

### 4️⃣ Access Application

Streamlit UI:  
http://localhost:8501

FastAPI Docs:  
http://localhost:8000/docs

---

## 🧠 This Project Contains

- Full end-to-end RAG implementation
- Vector database integration
- Session-based conversational memory
- Streaming API support
- Containerized deployment
- Clean modular architecture
- Production debugging & DB retry logic

---


## 👤 Sandeep R

Enterprise-focused AI engineering project demonstrating scalable backend architecture for LLM systems.
