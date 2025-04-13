from ollama import generate
from typing import Dict, Any

MODEL_NAME = "codellama:13b"


def generate_summary(file_report: Dict[str, Any]) -> str:
    prompt = build_prompt(file_report)
    try:
        response = generate(
            model=MODEL_NAME,
            prompt=prompt
        )
        return response["response"].strip()
    except Exception as e:
        raise RuntimeError(f"Ollama generate failed: {e}")



def build_prompt(file_report: Dict[str, Any]) -> str:
    """
    Build a prompt from the parsed info of a Python file.
    """
    base = f"Summarize what this Python file does, based on its structure.\n\n"
    base += f"File Path: {file_report.get('path')}\n"
    if "error" in file_report:
        return base + f"Note: Could not parse this file due to error: {file_report['error']}\n"

    base += f"Imports: {', '.join(file_report.get('imports', []))}\n\n"

    for func in file_report.get("functions", []):
        base += f"- Function `{func['name']}` takes arguments {func['args']}\n"
    for cls in file_report.get("classes", []):
        base += f"- Class `{cls['name']}`: {cls['docstring'] or 'No docstring'}\n"
        for m in cls['methods']:
            base += f"  - Method `{m['name']}` takes {m['args']}\n"

    base += "\nExplain in plain English what this file does."
    return base
