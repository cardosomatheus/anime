# Anime API 🚀

Uma API moderna construída com **FastAPI** para gerenciamento ou consulta de informações sobre animes. O projeto utiliza **Poetry** para gerenciamento de dependências e **Docker** para facilitar o desenvolvimento e deploy.


## 🛠️ Tecnologias Utilizadas

* **[Python 3.10+](https://www.python.org/)**
* **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web de alta performance.
* **[Poetry](https://python-poetry.org/)**: Gerenciamento de pacotes e ambientes virtuais.
* **[Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)**: Containerização da aplicação.
* **[Uvicorn](https://www.uvicorn.org/)**: Servidor ASGI para produção e desenvolvimento.

```bash
.
├── anime
│   ├── controller          # Controladore / endpoints 
│   ├── db                  # Conexão com o banco
│   ├── docker_database     # Script de inicialização do banco.
│   ├── dto                 # DTOs.
│   ├── exception           # Exceções configuradas.
│   ├── interface           # Interfaces.
│   ├── model               # Modelos das tabelas.    
│   ├── repository          # repository (CRUD).
│   ├── service             # service (camada de serviço.)
│   ├── .env                # Variaveis de ambiente.
│   ├── .gitignore          # gitignore              
│   └── app.py              # Inicialização da API.
├── docker-compose.yml      # Inicialização dos containers.
├── Dockerfile.api          # Dockerfile da api.
├── Dockerfile.db           # Dockerfile do BD.
├── poetry.lock         
├── pyproject.toml
└── README.md
```

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente e testar a API localmente.

### 1. Pré-requisitos
Certifique-se de ter o [Docker](https://www.docker.com/) instalado em sua máquina.

### 2. Subindo a Aplicação
No terminal, dentro da pasta raiz do projeto, execute o seguinte comando:

```bash
docker compose up -d
```

# Acesse o swagger da api em execução
http://0.0.0.0:8000/docs

Clique no canto superior a direita em "Authorize." e preencha os seginte campos.

```bash
username: admin
password: minhasenha123
```

Clique em autorizar.
Pronto, todos os endpoints estão disponiveis para uso.


