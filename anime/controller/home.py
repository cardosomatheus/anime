from anime.db.database import ConexaoDB
from anime.repository.anime_repository import RepositoryAnime
from anime.service.anime_service import ServiceAnime
from anime.repository.usuario_repository import UsuarioRepository
from anime.service.usuario_service import UsuarioService


def myservice() -> ServiceAnime:
    session = ConexaoDB().mysession()
    repo = RepositoryAnime(session=session)
    service = ServiceAnime(repository_anime=repo)
    return service


def myservice_usuario():
    session = ConexaoDB().mysession()
    repo = UsuarioRepository(session=session)
    service = UsuarioService(repository=repo)
    return service
