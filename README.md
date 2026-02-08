# Anime API 🚀

Uma API moderna construída com **FastAPI** para gerenciamento ou consulta de informações sobre animes. O projeto utiliza **Poetry** para gerenciamento de dependências e **Docker** para facilitar o desenvolvimento e deploy.

## 🛠️ Tecnologias Utilizadas

* **[Python 3.10+](https://www.python.org/)**
* **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web de alta performance.
* **[Poetry](https://python-poetry.org/)**: Gerenciamento de pacotes e ambientes virtuais.
* **[Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)**: Containerização da aplicação.
* **[Uvicorn](https://www.uvicorn.org/)**: Servidor ASGI para produção e desenvolvimento.

.
├── anime/              # Código fonte da aplicação
│   ├── app.py          # Ponto de entrada da API
│   └── ...             # Rotas, modelos e lógica
├── pyproject.toml      # Configurações do Poetry e dependências
├── Dockerfile          # Configuração da imagem Docker
└── README.md           # Documentação

## 🚀 Como Executar o Projeto



username=os.getenv("POSTGRES_USER"),
password=os.getenv("POSTGRES_PASSWORD"),
host="localhost",
port=5433,
database=os.getenv("POSTGRES_DB"),