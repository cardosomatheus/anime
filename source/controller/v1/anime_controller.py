from main import app
from source.service.anime_service import ServiceAnime
from source.repository.anime_repository import RepositoryAnime
from db.database import ConexaoDB


conn = ConexaoDB()
repo = RepositoryAnime(conn)
service = ServiceAnime(repository_anime=repo)


@app.get("/")
async def root() -> dict:
    return {"messagem": "Hello word"}


@app.get("/animes/{id_anime}")
async def litar_animes(id_anime: int) -> dict:
    return service.busca_anime_by_id(id=id)
