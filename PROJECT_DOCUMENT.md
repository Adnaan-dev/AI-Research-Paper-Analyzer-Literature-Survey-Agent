# 📘 AI Research Paper Analyzer — Project Document

## 1. 📌 Problem Statement

Performing a literature review is a time-consuming and repetitive task that typically takes **40–60 hours**.  
Researchers must manually search for papers, read them, extract key insights, and compare results across multiple sources.

This process leads to:
- ⏳ High time consumption  
- 📉 Reduced productivity  
- 🤯 Information overload  

---

## 2. 🎯 Objective

The objective of this project is to build an **Autonomous Multi-Agent AI System** that:

- Automatically fetches research papers from multiple sources  
- Extracts key insights using AI  
- Generates structured literature reviews  
- Enables question-answering using RAG (Retrieval-Augmented Generation)  

---

## 3. 📊 Scope of the Project

To ensure feasibility and performance:

- Maximum **10 research papers per run**
- Focus on **recent and relevant papers**
- System optimized for **low latency**
- Supports **basic academic queries**

---

## 4. 🏗️ System Architecture

The system follows a **multi-agent pipeline architecture**:

    User Input
        ↓
    Search Agent (arXiv + Semantic Scholar)
        ↓
    Text Chunking
        ↓
    Embedding Generation
        ↓
    Vector Database (ChromaDB)
        ↓
    Summarizer Agent
        ↓
    Insight Agent
        ↓
    Reviewer Agent
        ↓
    Reviser Agent (if needed)
        ↓
    Final Literature Review + Q&A



---

## 5. ⚙️ Technologies Used

- Python  
- LangGraph (Multi-agent orchestration)  
- LangChain  
- Streamlit (Frontend UI)  
- ChromaDB (Vector Database)  
- Sentence Transformers (Embeddings)  
- arXiv API  
- Semantic Scholar API  

---

## 6. 👥 Team Roles

| Member | Role | Responsibility |
|--------|------|---------------|
| M1 | Agent Orchestration | Graph flow, coordinator |
| M2 | Search & APIs | Paper retrieval |
| M3 | RAG Pipeline | Embeddings, vector DB |
| M4 | LLM Agents | Summarization & insights |
| M5 | Review Loop | Reviewer & reviser logic |
| M6 | Output & Export | Literature generation |
| M7 | Frontend UI | Streamlit interface |
| M8 | Docs & DevOps | Documentation & repo management |

---

## 7. 🔄 Workflow Explanation

1. User enters a research topic  
2. System fetches papers from APIs  
3. Papers are split into chunks  
4. Chunks are converted into embeddings  
5. Stored in vector database  
6. LLM agents generate summaries & insights  
7. Reviewer checks quality  
8. Reviser improves output if needed  
9. Final literature review is generated  
10. User can ask questions using RAG  

---

## 8. 🚀 Expected Outcome

- Fully automated literature review generation  
- Accurate insights from real research papers  
- Interactive Q&A system  
- Exportable PDF reports  

---

## 9. 📈 Impact

- Reduces literature review time from **40–60 hours to minutes**  
- Enhances research efficiency  
- Demonstrates real-world AI application  
- Useful for students, researchers, and developers  

---

## 10. ⚠️ Limitations

- Limited to 10 papers per run  
- Dependent on API availability  
- Performance may vary based on system resources  

---

## 11. 🔮 Future Enhancements

- Support for more research databases  
- Advanced visualization (graphs, charts)  
- Improved UI/UX  
- Integration with citation managers  

---

## 12. ✅ Conclusion

This project demonstrates how **AI and multi-agent systems** can automate complex academic tasks.  
By combining retrieval, reasoning, and generation, the system significantly reduces manual effort and improves productivity.

---