from anime.db.database import ConexaoDB
from anime.repository.usuario_repository import UsuarioRepository
from anime.service.usuario_service import UsuarioService


def myservice_usuario():
    session = ConexaoDB().mysession()
    repo = UsuarioRepository(session=session)
    service = UsuarioService(repository=repo)
    return service
