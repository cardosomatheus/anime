from anime.db.database import ConexaoDB
from anime.repository.anime_repository import RepositoryAnime
from anime.service.anime_service import ServiceAnime


def myservice() -> ServiceAnime:
    session = ConexaoDB().mysession()
    repo = RepositoryAnime(session=session)
    service = ServiceAnime(repository_anime=repo)
    return service
