from anime.interface.usuario_interface import IusuarioRepository
from anime.model.usuario_model import UsuarioModel
from anime.dto.usuario_dto import (
    UsuarioDtoIn,
    UsuarioDtoOut,
    ListUsuarioDtoOut,
    UsuarioValidaTokenDtoOut
)


class UsuarioService:

    def __init__(self, repository: IusuarioRepository):
        self.repository = repository

    def criar_usuario(self, dto: UsuarioDtoIn):
        usuario_model = UsuarioModel(
            nome=dto.username,
            criado=dto.criado_em,
            password=dto.password_hash,
            ind_admin=dto.is_admin
        )
        self.repository.criar_usuario(dto=usuario_model)
        return {"message": f"Usuario {dto.nome} Criado com sucesso."}

    def busca_usuario_by_id(self, id) -> UsuarioDtoOut:
        response = self.repository.busca_usuario_by_id(id=id)
        response = UsuarioDtoOut(
            username=response.nome,
            criado_em=response.criado,
            is_admin=response.ind_admin
        )
        return response

    def busca_all_usuarios(self) -> ListUsuarioDtoOut:
        response = self.repository.busca_all_usuarios()
        response = ListUsuarioDtoOut(
            [UsuarioDtoOut(
                username=i.nome,
                criado_em=i.criado,
                is_admin=i.ind_admin
            ) for i in response]
        )
        return response

    def _busca_usuario_by_nome(
        self,
        dto: UsuarioValidaTokenDtoOut
    ) -> UsuarioValidaTokenDtoOut:
        """ Valida se existe um usuario com mesmo nome e senha"""        

        user_auth = UsuarioModel(nome=dto.username, password=dto.password_hash)
        # Busca o usuario
        response = self.repository._busca_usuario_by_nome_e_senha(user_auth)

        if response is None:
            return None

        # Gera o DTO UsuarioValidaTokenDtoOut
        return UsuarioValidaTokenDtoOut(
            username=response.nome,
            password_hash=response.password
        )


if __name__ == "__main__":
    from anime.db.database import ConexaoDB
    from anime.repository.usuario_repository import UsuarioRepository

    repo = UsuarioRepository(ConexaoDB().mysession())
    service = UsuarioService(repository=repo)
