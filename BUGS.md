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

### 🔴 Bug 6: Groq API Rate Limit Failure
- **Issue:** Summarizer agent failed due to API rate limits
- **Impact:** Pipeline crashed during summarization
- **Fix:** Implemented retry logic in summarizer agent

---