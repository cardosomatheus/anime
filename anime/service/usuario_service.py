from anime.interface.usuario_interface import IusuarioRepository
from anime.dto.usuario_dto import UsuarioDtoIn


class UsuarioService:

    def __init__(self, repository: IusuarioRepository):
        self.repository = repository

    def criar_usuario(self, dto: UsuarioDtoIn):
        usuario_model = UsuarioDtoIn(dto)
        self.repository.criar_usuario(dto=usuario_model)
