# =========================
# README.md
# =========================
cat > README.md << 'EOF'
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
EOF

# =========================
# BUGS.md
# =========================
cat > BUGS.md << 'EOF'
# Known Bugs & Issues — AI-Research-Paper-Analyzer-Literature-Survey-Agent

## Day 5 Updates
- Verified end-to-end functionality with pre-loaded test topic.
- No critical errors during demo simulation.
- All main features functional: PDF export, RAG Q&A, live LangGraph visualization.

## Current Known Issues
1. **Large PDF Exports**  
   - May take longer for topics with >50 papers.  
   - Workaround: Export smaller batches.

2. **RAG Q&A Latency**  
   - Queries on very large datasets may take ~5-10 seconds.  
   - Workaround: Limit query to 5–10 papers at a time.

3. **Streamlit UI Scaling**  
   - Some UI elements may overlap on smaller screens.  
   - Workaround: Use a screen width ≥ 1366px.

4. **PDF Formatting**  
   - Minor alignment issues in tables for very long entries.  
   - WeasyPrint handles most formatting correctly.

5. **Future Improvements**  
   - Add auto-pagination for PDF export.  
   - Implement caching for RAG Q&A to reduce latency.  
   - Add dark mode option for Streamlit UI.

---

## Contact / Support
For issues, contact the contributor team or open a GitHub issue.
EOF
