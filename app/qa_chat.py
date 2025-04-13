import json
from typing import List, Dict
import ollama  # ✅ Official client


MODEL_NAME = "gemma3:12b"  # or "llama3", "openchat", etc.


def load_analysis_json(json_path: str) -> Dict:
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_relevant_files(question: str, file_summaries: List[Dict], top_k: int = 3) -> List[str]:
    ranked = sorted(
        file_summaries,
        key=lambda x: sum(kw in question.lower() for kw in x['summary'].lower().split()),
        reverse=True
    )
    return [f"{f['path']}:\n{f['summary']}" for f in ranked[:top_k]]


def ask_repo_question(json_path: str, question: str) -> str:
    analysis_json = load_analysis_json(json_path)
    summaries = analysis_json.get("files", [])
    context = "\n\n".join(find_relevant_files(question, summaries))

    system_prompt = "You are a concise codebase assistant. Answer the question briefly and clearly using the code summaries provided."

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Repo summaries:\n{context}\n\nQuestion: {question}"}
    ]

    response = ollama.chat(model=MODEL_NAME, messages=messages)

    return response['message']['content'].strip()
