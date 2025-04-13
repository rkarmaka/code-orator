from pathlib import Path
from typing import List, Dict, Any
import os


def build_dependency_graph(file_reports: List[Dict[str, Any]], repo_path: str) -> Dict[str, List[str]]:
    """
    Constructs a file-level dependency graph from analyzed file reports.
    Returns: Dict of {file_path: [list of dependent file paths]}
    """
    # Map module names (e.g. 'utils.helpers') to actual file paths
    module_to_file = {}
    file_to_deps = {}

    repo_path = Path(repo_path).resolve()

    for report in file_reports:
        full_path = Path(report["path"]).resolve()
        rel_path = full_path.relative_to(repo_path)
        module_path = ".".join(rel_path.with_suffix("").parts)
        module_to_file[module_path] = str(rel_path)
        file_to_deps[str(rel_path)] = []

    # Go over each file and link it to others based on imports
    for report in file_reports:
        source_file = str(Path(report["path"]).resolve().relative_to(repo_path))
        imports = report.get("imports", [])

        for imp in imports:
            imp_base = imp.split('.')[0]
            for mod, target_file in module_to_file.items():
                if mod.startswith(imp) or imp.startswith(mod):
                    if target_file != source_file and target_file not in file_to_deps[source_file]:
                        file_to_deps[source_file].append(target_file)

    return file_to_deps

def export_mermaid_graph(dep_graph: Dict[str, List[str]]) -> str:
    lines = ["graph TD"]
    for src, targets in dep_graph.items():
        for tgt in targets:
            lines.append(f'  "{src}" --> "{tgt}"')
    return "\n".join(lines)


def export_dot_graph(dep_graph: Dict[str, List[str]]) -> str:
    lines = ["digraph CodeGraph {"]
    for src, targets in dep_graph.items():
        for tgt in targets:
            lines.append(f'  "{src}" -> "{tgt}";')
    lines.append("}")
    return "\n".join(lines)
