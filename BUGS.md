# 🐞 BUG TRACKING LOG

This document tracks all bugs, issues, and fixes encountered during the development of the AI Research Paper Analyzer system.

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

## 📌 Notes

- Bugs are tracked daily for transparency and debugging
- Each issue is documented with cause and solution
- Helps maintain project stability and reliability

---

## 📅 Day 3 Bugs

### 🔴 Bug 4: Duplicate Papers from APIs
- **Issue:** Same paper fetched from arXiv and Semantic Scholar
- **Impact:** Redundant data in results
- **Fix:** Deduplication logic needed

---

### 🔴 Bug 5: Embedding Slow on CPU
- **Issue:** Sentence transformer model slow
- **Impact:** Delay in response
- **Fix:** Optimization planned

---

### 🔴 Bug 6: Chunk Size Issue
- **Issue:** Improper chunk size affects context
- **Impact:** Poor RAG answers
- **Fix:** Adjust chunk size and overlap