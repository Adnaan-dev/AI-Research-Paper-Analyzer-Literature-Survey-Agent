@'
# 🔬 Autonomous AI Research Paper Analyzer
### Multi-Agent Literature Survey System

A production-ready, multi-agent AI system that autonomously searches, analyzes, and synthesizes research papers from arXiv and Semantic Scholar — complete with a structured literature review generator, RAG-based Q&A interface, and PDF export capability.

---

## 🚀 How to Run the Project

# 1️⃣ Clone the repository
git clone https://github.com/Adnaan-dev/AI-Research-Paper-Analyzer-Literature-Survey-Agent.git

# 2️⃣ Navigate to project
cd AI-Research-Paper-Analyzer-Literature-Survey-Agent

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run backend
python backend/app.py

# 5️⃣ Run frontend (Streamlit)
streamlit run frontend/streamlit_app.py

---

## 📌 Features

- Multi-agent architecture
- Research paper fetching (arXiv, Semantic Scholar)
- RAG-based question answering
- Automatic summarization & insights
- Vector database using ChromaDB
- **Comparison Table**: Compare multiple papers side-by-side
- **Literature Review Generator**: Auto-summarized review for topics
- **Taxonomy**: Organize papers by topics or themes
- **Reviewer Report**: Structured review output
- **PDF Export**: Download full literature review via `/search/export/pdf`
- **Live Visualization**: LangGraph nodes light up to show which agent is running

---

## 📸 Project Preview

![App UI](assets/ui.png)
![GitHub](assets/github.png)

---

## Contributors & Roles (Day 5)

- **M1:** demo_script.md  
- **M2:** requirements.txt updated  
- **M3:** QA_ANSWERS.md  
- **M4:** insight_agent.py improved JSON parser  
- **M5:** PPT deck pushed to repo  
- **M6:** /export/pdf endpoint  
- **M7:** Streamlit 6-tab UI + PDF button  
- **M8:** README final + BUGS.md final  

---

## Usage

1. Load the app and select a test topic.  
2. Navigate between tabs: Papers & Insights, Comparison Table, Literature Review, Taxonomy, Reviewer Report, RAG Q&A.  
3. Interact with AI agents and view live graph execution.  
4. Export the literature review as PDF from the button or `/search/export/pdf`.

---

## Known Bugs / Limitations

See [BUGS.md](./BUGS.md)

---

## License

MIT License
'@ | Set-Content README.md
