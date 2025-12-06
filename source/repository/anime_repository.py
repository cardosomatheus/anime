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

    def busca_anime_by_id(self, id: int) -> dict:
        """ Busca o anime baseado no ID
        Args: id (int): Buscaremos o ANIME pelo ID
        dict: Retornamos o DICT do anime identificado ou None.
        """
        try:
            with self.session as conn:
                query = select(AnimeModel).where(AnimeModel.id == id)
                return conn.execute(query).scalar_one()
        except Exception as error:
            print(error)
            print(f'error in repositoory: {error}')

    def busca_all_animes(self) -> list[AnimeModel]:
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


if __name__ == "__main__":
    from db.database import ConexaoDB

    con_db = ConexaoDB().session()
    myrepo = RepositoryAnime(con_db)

    print(myrepo.busca_all_animes())
#    myrepo.atualiza_anime(13, dddd)
#    myrepo.deleta_anime(11)

#    myrepo.cria_anime(
#        nome='Leviathan31',
#        data_lancamento=date(day=10, month=7, year=2025),
#        descricao="""É uma série steampunk adaptada do livro de Scott
#        Westerfeld. A história se passa num universo alternativo para 1914,
#        onde existem criaturas vivas (como navios dirigidos) e máquinas
#        biológicas. Dois protagonistas — um príncipe (Aleksandar) e uma
#        garota disfarçada de menino (Deryn)"""
#    )