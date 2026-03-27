# 🔬 Autonomous Multi-Agent AI Research Paper Analyzer & Literature Survey System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-0.2-yellow?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Persistent-purple?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-black?style=for-the-badge&logo=openai)
![Groq](https://img.shields.io/badge/Groq-API-black?style=for-the-badge&logo=groq)

*A multi-agent AI system that autonomously searches, analyzes, and synthesizes academic research papers into structured literature reviews with RAG-based Q&A.*

</div>

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Multi-Agent Architecture](#-multi-agent-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup & Installation](#-setup--installation)
- [Running the Project](#-running-the-project)
- [Features](#-features)
- [Example Usage](#-example-usage)
- [Team](#-team)

---

## 🧠 Project Overview

This system acts as an intelligent research assistant that:

1. Accepts a **research topic** from the user
2. Automatically searches papers from **arXiv API** and **Semantic Scholar API**
3. Retrieves top relevant papers (title, abstract, link, authors)
4. Analyzes papers using a **multi-agent pipeline**
5. Generates a **structured literature review** with APA-style citations
6. Allows users to **ask questions** about the papers via a RAG-based chat interface

---

## 🤖 Multi-Agent (7+) Architecture

```
User Input (Topic)
       │
       ▼
┌─────────────────────┐
│  Coordinator Agent  │  ← Orchestrates the entire pipeline
└─────────┬───────────┘
          │
    ┌─────▼──────┐
    │Search Agent│  ← Fetches from arXiv + Semantic Scholar
    └─────┬──────┘
          │
  ┌───────▼────────┐
  │Summarizer Agent│  ← Generates concise paper summaries
  └───────┬────────┘
          │
  ┌───────▼───────┐
  │ Insight Agent │  ← Extracts: problem, method, dataset, models, results
  └───────┬───────┘
          │
  ┌───────▼──────────┐
  │ Comparison Agent │  ← Compares multiple papers side-by-side
  └───────┬──────────┘
          │
  ┌───────▼──────────────┐
  │Literature Review Agent│  ← Generates full structured review
  └───────┬──────────────┘
          │
  ┌───────▼──────┐
  │   QA Agent   │  ← RAG-based Q&A using ChromaDB vector store
  └──────────────┘
```

| Agent | Responsibility |
|---|---|
| **Search Agent** | Fetches & deduplicates papers from arXiv and Semantic Scholar |
| **Summarizer Agent** | Generates 3-5 sentence plain-English summaries |
| **Insight Agent** | Extracts structured fields (problem, method, dataset, models, results) |
| **Comparison Agent** | Produces a side-by-side comparative analysis in Markdown |
| **Literature Review Agent** | Writes a full academic literature survey with APA citations |
| **QA Agent** | Answers user questions using vector similarity search (RAG) |
| **Coordinator Agent** | Orchestrates all 6 stages in the correct order |

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.10, FastAPI, Uvicorn |
| **AI / LLM** | OpenAI GPT-4o-mini via LangChain |
| **Embeddings** | Sentence Transformers (`all-MiniLM-L6-v2`) — free, local |
| **Vector DB** | ChromaDB (persistent on disk) |
| **Paper Sources** | arXiv API, Semantic Scholar Graph API |
| **Frontend** | Streamlit |
| **Env Management** | python-dotenv |
| **Resilience** | Tenacity (retry with exponential backoff) |

---

## 📁 Project Structure

```
research-paper-agent/
│
├── backend/
│   ├── main.py                          # FastAPI app entry point
│   ├── config.py                        # All env vars & constants
│   │
│   ├── agents/
│   │   ├── search_agent.py              # Multi-source paper search & dedup
│   │   ├── summarizer_agent.py          # LLM-based paper summarization
│   │   ├── insight_agent.py             # Structured insight extraction
│   │   ├── comparison_agent.py          # Multi-paper comparative analysis
│   │   ├── literature_agent.py          # Literature review generator
│   │   ├── qa_agent.py                  # RAG-based Q&A
│   │   └── coordinator_agent.py         # Pipeline orchestrator
│   │
│   ├── services/
│   │   ├── arxiv_service.py             # arXiv Atom feed client
│   │   ├── semantic_scholar_service.py  # Semantic Scholar API client
│   │   ├── pdf_loader.py                # PDF download & text extraction
│   │   ├── text_chunker.py              # Sentence-boundary text splitting
│   │   ├── embedding_service.py         # Local HuggingFace embeddings
│   │   └── vector_store.py              # ChromaDB store + retriever
│   │
│   └── routes/
│       ├── search_route.py              # POST /api/search
│       └── query_route.py               # POST /api/query
│
├── frontend/
│   └── streamlit_app.py                 # 4-tab Streamlit UI
│
├── data/
│   ├── papers/                          # Downloaded paper files (optional)
│   └── chroma_db/                       # Persistent vector store (auto-created)
│
├── export_db.py                         # Utility: export ChromaDB contents
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites

- **Python 3.10** (strictly required — use `py -3.10` on Windows)
- An **OpenAI API key** → [Get one here](https://platform.openai.com/api-keys) , if you have no credits then use Groq API (its free)
- Git

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/<your-username>/research-paper-agent.git
cd research-paper-agent
```

---

### Step 2 — Create a Virtual Environment (Python 3.10)

> ⚠️ **Important:** This project requires Python 3.10 specifically.

**Windows:**
```bash
py -3.10 -m venv venv
```

**macOS / Linux:**
```bash
python3.10 -m venv venv
```

---

### Step 3 — Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

---

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

> First-time install will download the `all-MiniLM-L6-v2` embedding model (~90 MB). This is a one-time download.

---

### Step 5 — Configure Environment Variables

```bash
cp .env.example .env
```

Open `.env` and fill in your keys:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here   , if you have no credits then use Groq API (its free)
SEMANTIC_SCHOLAR_API_KEY=          # optional, leave blank for free tier
BACKEND_URL=http://localhost:8000
CHROMA_PERSIST_DIR=./data/chroma_db
MAX_PAPERS_PER_SOURCE=5
```

> 💡 Semantic Scholar API key is **optional** — the free tier works without it (rate-limited to ~100 req/5 min).

---

## 🚀 Running the Project

Open **two separate terminals**, both with the virtual environment activated.

### Terminal 1 — Run the Backend (FastAPI)

```bash
venv\Scripts\activate

cd backend
python main.py
```

Backend will start at → `http://localhost:8000`  
API docs available at → `http://localhost:8000/docs`

---

### Terminal 2 — Run the Frontend (Streamlit)

```bash
venv\Scripts\activate

cd frontend
streamlit run streamlit_app.py
```

Frontend will open at → `http://localhost:8501`

---

### Export the Vector Database (Optional)

To inspect or export all stored paper chunks from ChromaDB:

```bash
python export_db.py
```

This will dump all stored documents and metadata to a JSON file in the `data/` directory.

---

## ✨ Features

- 🔍 **Topic-based paper search** across arXiv and Semantic Scholar simultaneously
- 📝 **Automatic summarization** of each paper in plain English
- 🔬 **Structured insight extraction** — problem, methodology, datasets, models, results
- 🆚 **Multi-paper comparison** — themes, differences, trade-offs, research gaps
- 📖 **Full literature review generation** with APA-style citations and reference list
- 💬 **RAG-based chat interface** — ask anything about the analyzed papers
- 💾 **Persistent vector storage** — previous sessions are remembered across restarts
- 📥 **Download literature review** as a `.md` file

---

## 🎯 Example Usage

### Research Topics to Try

```
attention mechanisms in transformers
large language model hallucination detection
graph neural networks for drug discovery
reinforcement learning from human feedback
vision transformers for medical image segmentation
contrastive learning self-supervised representation
```

### Example Q&A Questions (after searching)

```
What datasets were most commonly used across these papers?
Which paper achieved the best performance and how?
What are the main limitations of the proposed methods?
How do the methodologies differ from each other?
What future research directions are suggested?
Which models were used most frequently?
```

---

## 👥 Team

| Name | GitHub |
|---|---|
| Jan Adnan Farooq | [@adnanfarooq](https://github.com/adnaan-dev) |
| Abhishek | [@Abhishek-134](https://github.com/Abhishek-134) |
| Akeem Ali | [@Akeem786](https://github.com/Akeem786) |
| Mohammad Aakib Bhat | [@bhataakib02](https://github.com/bhataakib02) |
| Mayank Mihir | [@mayankkmk77](https://github.com/mayankkmk77) |
| Saqib Mokhtar | [@saqibmokhtar884](https://github.com/saqibmokhtar884) |
| Satakshik Chaurasia | [@satakshik-chaurasia](https://github.com/satakshik-chaurasia) |
| Sradha Ram | [@Sradha2474](https://github.com/Sradha2474) |

---

## 📄 License

This project is developed as part of an academic group project at **C.V. Raman Global University**.

---

<div align="center">
  <i>Built with ❤️ by the team — powered by LangChain, OpenAI, ChromaDB, and Streamlit</i>
</div>
