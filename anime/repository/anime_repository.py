from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from anime.interface.anime_interface import IanimeRepository
from anime.model.anime_model import AnimeModel


class RepositoryAnime(IanimeRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def cria_anime(self, anime: AnimeModel) -> None:
        with self.session as mysession:
            try:
                mysession.add(anime)
                mysession.commit()
                mysession.refresh(anime)
            except Exception as error:
                print(str(error))
                mysession.rollback()

    def busca_anime_by_id(self, id: int) -> AnimeModel:
        """ busca Anime pelo id"""
        with self.session as mysession:
            query = select(AnimeModel).where(AnimeModel.id == id)
            return mysession.execute(query).scalar()

    def busca_all_animes(self) -> list[AnimeModel]:
        """ busca todos os Animes"""
        with self.session as mysession:
            query = select(AnimeModel)
            return mysession.execute(query).scalars().all()

    def deleta_anime(self, id: int) -> None:
        """ Deleta o anime informado pelo ID"""
        with self.session as mysession:
            try:
                query = delete(AnimeModel).where(AnimeModel.id == id)
                mysession.execute(query)
                mysession.commit()
            except Exception:
                mysession.rollback()

    def atualiza_anime(self,
                       dict_anime: dict) -> None:
        """ Atualiza O anime informado"""
        with self.session as mysession:
            try:
                query = update(AnimeModel)\
                        .where(AnimeModel.id == dict_anime.get('id'))\
                        .values(**dict_anime)
                mysession.execute(query)
                mysession.commit()
            except Exception:
                mysession.rollback()
