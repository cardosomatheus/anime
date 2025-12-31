from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from anime.interface.anime_interface import IanimeRepository
from anime.model.anime_model import AnimeModel
from anime.exception.anime_exception import (
    AnimeRepositoryUnique,
    AnimeException
)


class RepositoryAnime(IanimeRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def cria_anime(self, anime: AnimeModel) -> None:
        with self.session as mysession:
            try:
                mysession.add(anime)
                mysession.commit()
                mysession.refresh(anime)

            except IntegrityError as error:
                mysession.rollback()
                if 'errors.UniqueViolation' in str(error.args):
                    raise AnimeRepositoryUnique("Anime já existe.")
                raise Exception(str(error))

            except Exception as error:
                mysession.rollback()
                raise Exception(str(error))

    def atualiza_anime(self, anime: AnimeModel) -> None:
        """ Atualiza o anime informado"""
        with self.session as mysession:

            try:
                query = update(AnimeModel)\
                        .where(AnimeModel.id == anime.id)\
                        .values(anime.to_dict())
                mysession.execute(query)
                mysession.commit()
            except Exception as error:
                mysession.rollback()
                raise AnimeException(str(error))

    def deleta_anime(self, id: int) -> None:
        """ Deleta o anime informado pelo ID"""
        with self.session as mysession:
            try:
                query = delete(AnimeModel).where(AnimeModel.id == id)
                mysession.execute(query)
                mysession.commit()
            except Exception as error:
                mysession.rollback()
                raise AnimeException(str(error))

    def busca_anime_by_id(self, id: int) -> AnimeModel:
        """ busca Anime pelo id"""
        with self.session as mysession:
            query = select(AnimeModel).where(AnimeModel.id == id)
            return mysession.execute(query).scalar_one_or_none()

    def busca_all_animes(self) -> list[AnimeModel]:
        """ busca todos os Animes"""
        with self.session as mysession:
            query = select(AnimeModel)
            return mysession.execute(query).scalars().all()
