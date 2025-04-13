import ast
from pathlib import Path
from typing import List, Dict, Any


class PythonFileAnalyzer:
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.tree = None
        self.parsed = False
        self.results = {
            "path": str(filepath),
            "imports": [],
            "functions": [],
            "classes": [],
        }

    def analyze(self) -> Dict[str, Any]:
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                source = f.read()
            self.tree = ast.parse(source)
            self._extract_info()
            self.parsed = True
        except SyntaxError as e:
            self.results["error"] = f"SyntaxError: {e}"
        except Exception as e:
            self.results["error"] = f"UnknownError: {e}"
        return self.results

    def _extract_info(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                self.results["imports"].extend([alias.name for alias in node.names])
            elif isinstance(node, ast.ImportFrom):
                module = node.module if node.module else ""
                self.results["imports"].append(module)
            elif isinstance(node, ast.FunctionDef):
                self.results["functions"].append({
                    "name": node.name,
                    "args": [arg.arg for arg in node.args.args],
                    "docstring": ast.get_docstring(node),
                    "lineno": node.lineno
                })
            elif isinstance(node, ast.ClassDef):
                self.results["classes"].append({
                    "name": node.name,
                    "docstring": ast.get_docstring(node),
                    "lineno": node.lineno,
                    "methods": [
                        {
                            "name": n.name,
                            "args": [arg.arg for arg in n.args.args],
                            "docstring": ast.get_docstring(n),
                            "lineno": n.lineno
                        }
                        for n in node.body if isinstance(n, ast.FunctionDef)
                    ]
                })


def analyze_repository(repo_path: str) -> List[Dict[str, Any]]:
    path = Path(repo_path)
    print(path)
    results = []

    for file in path.rglob("*.py"):
        analyzer = PythonFileAnalyzer(file)
        results.append(analyzer.analyze())

    return results