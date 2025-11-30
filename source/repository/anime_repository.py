from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from datetime import date

from interface.anime_interface import IanimeRepository
from ..model.anime_model import AnimeModel


class RepositoryAnime(IanimeRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def cria_anime(self,
                   nome: str,
                   data_lancamento: date,
                   descricao: str,
                   ) -> AnimeModel:
        """Args:
           nome (str): Nome do anime
           data_lancamento (date): data de lancamento
           descricao (str): Descricao do anime
        Raises:
            Exception: Erro no cadastro
        Returns:
            AnimeModel: Retorna o model da tabela.
        """

        if nome is None:
            raise Exception("Nome não pode ser Nulo.")

        new_anime_model = AnimeModel(nome=nome,
                                     data_lancamento=data_lancamento,
                                     descricao=descricao)

        with self.session as conn:
            try:
                conn.add(new_anime_model)
                conn.commit()
                conn.refresh(new_anime_model)
            except Exception as error:
                print()
                print(f'Erro ao salvar o Anime: {nome}!')
                print(error)

        return new_anime_model

    def busca_anime_by_id(self, id: int) -> AnimeModel:
        """ Busca o anime baseado no ID
        Args: id (int): Buscaremos o ANIME pelo ID
        str: Retornamos o AnimeModel do anime identificado ou None.
        """
        with self.session as conn:
            query = select(AnimeModel).where(AnimeModel.id == id)
            return conn.execute(query).first()

    def busca_all_animes(self) -> list:
        """ Buscamos todos os animes da base.
            Returns: Todos os animes da base
        """
        with self.session as conn:
            query = select(AnimeModel)
            return conn.execute(query).all()

    def deleta_anime(self, id: int) -> None:
        """ Deleta o anime informado pelo ID
            Args: id (int): ID do anime.
        """
        with self.session as conn:
            query = delete(AnimeModel).where(AnimeModel.id == id)
            conn.execute(query)
            conn.commit()

    def atualiza_anime(self,
                       dict_Anime_model: dict) -> None:
        """ Atualiza O anime informado
            Args: dict_Anime_model (dict): dict com novos valores
        """
        with self.session as conn:
            query = update(AnimeModel)\
                    .where(AnimeModel.id == dict_Anime_model.get('id'))\
                    .values(**dict_Anime_model)

            conn.execute(query)
            conn.commit()
