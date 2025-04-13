from app.analyzer import analyze_repository
from app.summarizer import generate_summary
from app.linker import build_dependency_graph


def analyze_and_summarize_repo(repo_path: str):
    analysis = analyze_repository(repo_path)
    
    for file_report in analysis:
        summary = generate_summary(file_report)
        file_report["summary"] = summary

    dependency_graph = build_dependency_graph(analysis, repo_path)

    return {
        "files": analysis,
        "dependency_graph": dependency_graph
    }
