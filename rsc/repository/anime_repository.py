from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from datetime import date

from interface.anime_interface import Ianime
from ..model.anime_model import AnimeModel


class RepositoryAnime(Ianime):
    def __init__(self, session: Session) -> None:
        self.session = session

    def cria_anime(self,
                   nome: str,
                   data_lancamento: date,
                   descricao: str,
                   ) -> AnimeModel:
        """
        Args:
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

    def busca_anime_by_id(self, id: int) -> list:
        """
        Args:
            id (int): Buscaremos o ANIME pelo ID
        Raises:
            Exception: Se o ID não existir, retornamos None

        Returns:
            str: Retornamos o nome do Anime
        """
        if id is not None and not isinstance(id, int):
            raise Exception('ID deve ser uma valor inteiro!!')

        with self.session as conn:
            try:
                query = select(AnimeModel.nome).where(AnimeModel.id == id)
                return conn.execute(query).first()

            except TypeError:
                return [None]

    def busca_all_animes(self) -> list:
        """
        Returns:
            list: Retornamos em formato de lista todos os animes.
        """
        with self.session as conn:
            try:
                query = select(
                               AnimeModel.id,
                               AnimeModel.nome,
                               AnimeModel.data_lancamento,
                               AnimeModel.descricao
                            )

                return conn.execute(query).all()
            except Exception:
                return []

    def deleta_anime(self, id: int) -> bool:
        """Faz a deleção do anime pelo ID
        Args:
            id (int): id do anime
        Raises:
            Exception: ID deve ser inteiro
            Exception: ID não deve ser Nulo
        """
        if not isinstance(id, int):
            raise Exception('ID deve ser uma valor inteiro!!')

        if id is None:
            raise Exception('Passe o ID (valor Inteiro)')

        with self.session as conn:
            try:
                query = delete(AnimeModel).where(AnimeModel.id == id)
                conn.execute(query)
                conn.commit()
                return True
            except Exception as error:
                print(error)
                return False

    def atualiza_anime(self,
                       id: int,
                       dict_Anime_model: dict) -> AnimeModel:
        """Atualizamos campos contidos no model de anime
        Args:
            id (int): id do anime
        Raises:
            Exception: ID deve ser inteiro
        Returns:
            AnimeModel: _description_
        """
        if not isinstance(id, int):
            raise Exception('ID deve ser uma valor inteiro!!')

        dict_atualizar_campos = {
            key: value for key, value in dict_Anime_model.items()
        }

        with self.session as conn:
            try:
                query = update(AnimeModel)\
                        .where(AnimeModel.id == id)\
                        .values(**dict_atualizar_campos)

                conn.execute(query)
                conn.commit()
            except Exception as error:
                print(error)


if __name__ == "__main__":
    from db.database import ConexaoDB

    con_db = ConexaoDB().session()
    myrepo = RepositoryAnime(con_db)
    dddd = {'nome': 'Leviathan', 'idade': '19'}

    print(myrepo.busca_anime_by_id(13))
    print(myrepo.busca_all_animes())
    myrepo.atualiza_anime(13, dddd)
    myrepo.deleta_anime(11)

#    myrepo.cria_anime(
#        nome='Leviathan31',
#        data_lancamento=date(day=10, month=7, year=2025),
#        descricao="""É uma série steampunk adaptada do livro de Scott
#        Westerfeld. A história se passa num universo alternativo para 1914,
#        onde existem criaturas vivas (como navios dirigidos) e máquinas
#        biológicas. Dois protagonistas — um príncipe (Aleksandar) e uma
#        garota disfarçada de menino (Deryn)"""
#    )
