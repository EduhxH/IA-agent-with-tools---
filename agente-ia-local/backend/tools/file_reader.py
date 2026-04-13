import os

def read_file(path: str) -> str:
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(os.getcwd()):
        return "Acesso negado."
    if not os.path.exists(abs_path):
        return f"Ficheiro não encontrado: {path}"
    ext = os.path.splitext(path)[1].lower()
    if ext not in {'.txt', '.md', '.py', '.json', '.csv'}:
        return f"Extensão não suportada: {ext}"
    with open(abs_path, encoding='utf-8') as f:
        return f.read()[:5000]