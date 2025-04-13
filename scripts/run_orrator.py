import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  

from app.orchestrator import analyze_and_summarize_repo
from app.linker import export_mermaid_graph, export_dot_graph
import sys
import json

if __name__ == "__main__":
    # repo = sys.argv[1]
    repo = "/mnt/data/code-orator/examples/pymmcore-plus"
    repo_name = repo.split("/")[-1]
    result = analyze_and_summarize_repo(repo)

    # Save full output
    with open(f"output/{repo_name}_summary.json", "w") as f:
        json.dump(result, f, indent=2)

    # Export Mermaid graph
    mermaid = export_mermaid_graph(result["dependency_graph"])
    with open(f"output/{repo_name}_dependency_graph.mmd", "w") as f:
        f.write(mermaid)

    # Export DOT graph
    dot = export_dot_graph(result["dependency_graph"])
    with open(f"output/{repo_name}_dependency_graph.dot", "w") as f:
        f.write(dot)

    print("✔️ Code analysis complete. Graphs saved to 'output/' directory.")
