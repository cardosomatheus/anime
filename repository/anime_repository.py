from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from datetime import date

from anime.interface.anime_interface import IanimeRepository
from anime.model.anime_model import AnimeModel


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
        new_anime_model = AnimeModel(nome=nome,
                                     data_lancamento=data_lancamento,
                                     descricao=descricao)

        try:
            with self.session as mysession:
                mysession.add(new_anime_model)
                mysession.commit()
                mysession.refresh(new_anime_model)
        except Exception as error:
            print()
            print(f'Erro ao salvar o Anime: {nome}!')
            print(error)
        finally:
            return new_anime_model

    def busca_anime_by_id(self, id: int) -> dict:
        """ Busca o anime baseado no ID
        Args: id (int): Buscaremos o ANIME pelo ID
        dict: Retornamos o DICT do anime identificado ou None.
        """
        try:
            with self.session as mysession:
                query = select(AnimeModel).where(AnimeModel.id == id)
                return mysession.execute(query).scalar_one()
        except Exception as error:
            print(error)
            print(f'error in repositoory: {error}')

    def busca_all_animes(self) -> list[AnimeModel]:
        """ Buscamos todos os animes da base.
            Returns: Todos os animes da base
        """
        with self.session as mysession:
            query = select(AnimeModel)
            return mysession.execute(query).all()

    def deleta_anime(self, id: int) -> None:
        """ Deleta o anime informado pelo ID
            Args: id (int): ID do anime.
        """
        with self.session as mysession:
            query = delete(AnimeModel).where(AnimeModel.id == id)
            mysession.execute(query)
            mysession.commit()

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
    from anime.db.database import ConexaoDB

    sessao = ConexaoDB().mysession()
    print(type(sessao))
#    with sessao as mysession:
#        print(mysession.execute(text('select now()')).first())
#    with con_db as conexao:
#        conexao.execute(text('select now()')).first()
    # myrepo = RepositoryAnime(con_db)

    # print(myrepo.busca_all_animes())
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