from anime.db.database import Session
from anime.model.catergoria_anime_model import CategoriaAnimeModel
from anime.model.categoria_model import Categoria_model
from sqlalchemy import text, select
from sqlalchemy.exc import SQLAlchemyError


class CatergoriaAnimeRepository:

    def __init__(self, session: Session):
        self.session = session

    def busca_all_categorias(self) -> list[Categoria_model]:
        """ busca todos os Animes"""
        with self.session as mysession:
            query = select(Categoria_model)
            return mysession.execute(query).scalars().all()

    def vincula_categoria_anime(
        self,
        categoria_anime_model: CategoriaAnimeModel
    ):
        # Fazemos a criação do vinculo de anime e categroia via procedure.
        params = {
            "idAnime": categoria_anime_model.id_anime,
            "idCategoria": categoria_anime_model.id_categoria
        }

        query = text("call proc_vinc_anime_categoria(:idAnime, :idCategoria)")

        try:
            with self.session as mysession:
                mysession.execute(statement=query, params=params)
                mysession.commit()
        except SQLAlchemyError as error:
            if hasattr(error.orig, 'pgcode'):
                message = error.orig.diag.message_primary
            else:
                mysession.rollback()
                message = "Ocorreu um erro inesperado no banco de dados."

            raise Exception(message)

        except Exception as error:
            mysession.rollback()
            raise Exception(error)

    def remove_categoria_anime(
            self,
            categoria_anime_model: CategoriaAnimeModel
    ):
        # Fazemos a remoção de vinculo de anime e categroia via procedure.
        params = {
            "idAnime": categoria_anime_model.id_anime,
            "idCategoria": categoria_anime_model.id_categoria
        }

        query = text("call proc_rem_anime_categoria(:idAnime, :idCategoria)")

        try:
            with self.session as mysession:
                mysession.execute(statement=query, params=params)
                mysession.commit()
        except SQLAlchemyError as error:
            if hasattr(error.orig, 'pgcode'):
                message = error.orig.diag.message_primary
            else:
                mysession.rollback()
                message = "Ocorreu um erro inesperado no banco de dados."

            raise Exception(message)

        except Exception as e:
            mysession.rollback()
            raise Exception(e)
