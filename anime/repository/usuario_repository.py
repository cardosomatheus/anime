from anime.db.database import Session, ConexaoDB
from anime.model.usuario_model import UsuarioModel
from anime.exception.usuario_exception import UsuarioRepositoryUnique

from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone


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


if __name__ == "__main__":
    repo = UsuarioRepository(ConexaoDB().mysession())
    usuario = UsuarioModel(
        nome='matsheus',
        password="mcds123",
        criado=datetime.now(timezone.utc),
        ind_admin=True)
    repo.criar_usuario(usuario=usuario)
