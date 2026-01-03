from anime.db.database import Session, ConexaoDB
from anime.model.usuario_model import UsuarioModel
from anime.exception.usuario_exception import UsuarioRepositoryUnique

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from typing import List


class UsuarioRepository:

    def __init__(self, session: Session):
        self.session = session

    def criar_usuario(self, usuario: UsuarioModel):
        """Criar um novo Usuario"""
        with self.session as mysession:
            try:
                mysession.add(usuario)
                mysession.commit()
                mysession.refresh(usuario)
            except IntegrityError as error:
                mysession.rollback()
                if 'errors.UniqueViolation' in str(error.args):
                    raise UsuarioRepositoryUnique("Usuario já existe.")
                raise Exception(str(error))

            except Exception as error:
                mysession.rollback()
                raise Exception(str(error))

    def busca_usuario_by_id(self, id: int) -> UsuarioModel:
        """Busca Usuario pelo ID"""
        with self.session as mysession:
            try:
                query = select(UsuarioModel).\
                        where(UsuarioModel.id == id)
                return mysession.execute(query).scalar_one_or_none()
            except Exception as error:
                raise Exception(str(error))

    def busca_all_usuarios(self) -> List[UsuarioModel]:
        """ Busca todos os Usuarios"""
        with self.session as mysession:
            try:
                query = select(UsuarioModel)
                return mysession.execute(query).scalars().all()
            except Exception as error:
                raise Exception(str(error))

 
if __name__ == "__main__":
    repo = UsuarioRepository(ConexaoDB().mysession())
    print('ois')
    print(repo.busca_all_usuarios())
    # print(repo.busca_usuario_by_id(id=1))
    # usuario = UsuarioModel(
    #   nome='marilan',
    #    password="mcds123",
    #    criado=datetime.now(timezone.utc),
    #    ind_admin=True)
    # repo.criar_usuario(usuario=usuario)
