from anime.db.database import Session
from anime.model.catergoria_anime_model import CategoriaAnimeModel
from sqlalchemy import text


class CatergoriaAnime:

    def __init__(self, session: Session):
        self.sesssion = session

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
            with self.sesssion as mysession:
                mysession.execute(statement=query, params=params)
                mysession.commit()
        except Exception as e:
            mysession.rollback()
            raise Exception(e)

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
            with self.sesssion as mysession:
                mysession.execute(statement=query, params=params)
                mysession.commit()
        except Exception as e:
            mysession.rollback()
            raise Exception(e)


if __name__ == '__main__':
    from anime.db.database import ConexaoDB

    sessao = ConexaoDB().mysession()
    repo = CatergoriaAnime(session=sessao)
    modelo = CategoriaAnimeModel(
        id_anime=2,
        id_categoria=3
    )

    # print(repo.vincula_categoria_anime(modelo))
    # print(repo.remove_categoria_anime(modelo))