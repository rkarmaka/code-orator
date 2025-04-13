# 💻 Code-Orator

**Code-Orator** is a local-first tool that helps developers quickly understand unfamiliar codebases. It parses a repository, summarizes each file using a local LLM (via Ollama), builds a file-level dependency graph, and supports interactive Q&A to answer questions like:

- "What does this repo do?"
- "Where is user authentication handled?"
- "What are the key components of this project?"

---

## 🚀 Features

- ✅ Static analysis of Python codebases
- ✅ File-level summaries using local LLMs (Code Llama, Mistral, etc.)
- ✅ Dependency graph between files
- ✅ Interactive Q&A interface powered by a chat-tuned LLM

---

## 📦 Project Structure

```
code-orator/
├── app/
│   ├── analyzer.py       # Parses Python files (functions, classes, imports)
│   ├── summarizer.py     # Calls LLM (via Ollama) to summarize code
│   ├── linker.py         # Builds file dependency graph
│   ├── orchestrator.py   # Runs the full pipeline
│   └── qa_chat.py        # Q&A over summarized repo
├── scripts/
│   ├── run_orator.py     # Analyze + summarize a repo
│   └── chat_orator.py    # Ask questions about a summarized repo
├── examples/             # Sample codebases and outputs
├── requirements.txt
└── README.md
```

---

## 🛠 Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running
- A supported local model:
  - `codellama`, `mistral`, `llama3`, `openchat`, etc.

---

## 🧪 Quickstart

### 1. Analyze and Summarize a Codebase

```bash
python scripts/run_orator.py /path/to/codebase > output.json
```

### 2. Ask Questions About the Codebase

```bash
python scripts/chat_orator.py output.json "What does this repo do?"
```

---

## 🧩 Model Suggestions

| Model      | Use Case                         |
|------------|----------------------------------|
| `codellama` | Good for code summarization     |
| `gemma3`   | Great for Q&A and natural language |

---

## 📌 Todo / Future Work

- [ ] Add function-level linking
- [ ] Visualize dependency graph with Mermaid
- [ ] Web UI
- [ ] Embedding-based search for smarter Q&A

---

## 💡 Why?

Reading code is hard. Code-Orator makes it easier to understand new projects without digging through every file manually — all powered by local LLMs, keeping your code private.

---

## 🧑‍💻 Author

Built by Ranit Karmakar  
MIT License