# 🚀 AI Workflow Automation Agent  
Open-source, local LLM-powered automation agent that converts natural-language tasks into **executable workflows**:  
- email automation  
- PDF & text summarization  
- web scraping  
- Google Sheets operations  
- file operations  
- scheduled workflows  
- general multi-step automation  

Runs **fully offline** using free/open-source LLMs with GGUF models.

---

## 🌟 Features

### 🧠 Planner + Executor Architecture
- **Planner Agent** → converts NL task → structured workflow steps  
- **Executor Agent** → runs steps with validated tool calls  
- Supports long, multi-step automation with state

### 🛠️ Modular Tool Registry
- Safe, composable, sandboxed tool calls  
- Easy to extend with new tools (files, email, APIs, Selenium, Sheets etc.)

### 📄 Workflow Support
- **YAML workflows** for reusable automation  
- **Ad-hoc natural-language instructions** (no YAML required)

### 🖥️ UI + API
- Optional **Streamlit UI**  
- Minimal **REST API entrypoint** included

### 🧩 Local LLM Support
- Works with **GGUF** models via `llama-cpp-python`  
- Supports **Ollama**, **GGML**, and external endpoints  
- No paid API keys required

---

# ⚡ Quickstart (Local / VS Code)

### **1. Clone the repo**
```bash
git clone <this-repo>
cd ai-workflow-automation-agent


python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# OR
# .venv\Scripts\activate        # Windows

pip install -r requirements.txt


python main.py


streamlit run ui/app.py



Quickstart (Google Colab)
1. Upload or clone the repo
!git clone <this-repo>
%cd ai-workflow-automation-agent

2. Install dependencies
!pip install -r requirements.txt

3. Load lightweight or offline models

phi-3-mini (GGUF)

mistral-7b-instruct.gguf

llama-3-8b-instruct.gguf

or run planner heuristically for POC

Example:

from core.llm_loader import load_model
llm = load_model()