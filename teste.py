import pathlib

def draw_tree(directory, prefix=""):
    """
    Gera uma representação visual da estrutura de pastas de um diretório.
    """
    path = pathlib.Path(directory)
    
    # Filtra e ordena o conteúdo (pastas primeiro, depois arquivos)
    # Ignora pastas de controle de versão e cache
    ignored = {".git", "__pycache__", ".pytest_cache", ".venv"}
    items = sorted(
        [p for p in path.iterdir() if p.name not in ignored],
        key=lambda p: (p.is_file(), p.name.lower())
    )

    for i, item in enumerate(items):
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        print(f"{prefix}{connector}{item.name}")
        
        if item.is_dir():
            # Se for diretório, chama a função recursivamente com novo prefixo
            extension = "    " if is_last else "│   "
            draw_tree(item, prefix + extension)

if __name__ == "__main__":
    # Define o diretório atual como raiz ou coloque o caminho completo
    root_path = "." 
    print(f".")
    draw_tree(root_path)