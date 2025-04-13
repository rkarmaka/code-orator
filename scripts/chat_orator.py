import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  

from app.qa_chat import ask_repo_question

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Usage: python chat_orator.py <path/to/analysis.json> \"<question>\"")
    #     sys.exit(1)

    # json_path = sys.argv[1]
    json_path = "/mnt/data/code-orator/output/muse-mind_summary.json"
    question = "Which method to use to snap an image using thie repo?"
    
    answer = ask_repo_question(json_path, question)
    print("\n💬 Answer:")
    print(answer)
