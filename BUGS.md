# 🐞 BUG TRACKING LOG

This document tracks all bugs, issues, and fixes encountered during the development of the AI Research Paper Analyzer system.

---

## 📅 Day 1 Bugs

### 🔴 Bug 0: Git Setup Confusion
- **Issue:** Initial confusion in Git setup, cloning repository, and branch workflow
- **Impact:** Delay in starting development work
- **Fix:** Configured Git properly and followed standard GitHub workflow

---

## 📅 Day 2 Bugs

### 🔴 Bug 1: arXiv API Timeout
- **Issue:** arXiv API sometimes takes too long to respond
- **Impact:** Delay in fetching research papers
- **Fix:** Added retry logic and timeout handling (planned)

---

### 🔴 Bug 2: Import Errors in Modules
- **Issue:** Some modules failed due to incorrect import paths
- **Impact:** Application did not run initially
- **Fix:** Corrected relative import paths

---

### 🔴 Bug 3: Streamlit UI Not Loading
- **Issue:** Streamlit app failed to launch on first run
- **Impact:** UI not visible for demo
- **Fix:** Verified dependencies and corrected run command

---

## 📅 Day 3 Bugs

### 🔴 Bug 4: ChromaDB Collection Initialization Failure
- **Issue:** ChromaDB crashed on first run because collection did not exist
- **Impact:** System failed to store embeddings
- **Fix:** Replaced `get_collection` with `get_or_create_collection`

---

## 📌 Notes

- Bugs are tracked daily for transparency and debugging
- Each issue is documented with cause and solution
- Helps maintain project stability and reliability

---

## 📅 Day 4 Bugs

### 🔴 Bug 5: Infinite Loop in Reviewer-Reviser Cycle
- **Issue:** Reviewer and Reviser loop kept running infinitely
- **Impact:** System got stuck and never reached final output
- **Fix:** Added maximum revision limit (2 iterations)

---



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
'@ | Set-Content BUGS.md

### 🔴 Bug 6: Groq API Rate Limit Failure
- **Issue:** Summarizer agent failed due to API rate limits
- **Impact:** Pipeline crashed during summarization
- **Fix:** Implemented retry logic in summarizer agent

---
