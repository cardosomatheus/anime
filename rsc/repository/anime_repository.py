from interface.anime_interface import Ianime
from db.database import ConexaoDB
from ..model.anime_model import AnimeModel
from sqlalchemy import select
from datetime import date


class RepositoryAnime(Ianime):
    def __init__(self) -> None:
        pass

    def cria_anime(self,
                   nome: str,
                   data_lancamento: date,
                   descricao: str,
                   db: ConexaoDB) -> AnimeModel:
        """_summary_

        Args:
            nome (str): Nome do anime
            data_lancamento (date): data de lancamento
            descricao (str): Descricao do anime
            db (ConexaoDB): Class ConexaoDB para acessarmos o banco de dados.

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

        with db.session() as conn:
            try:
                conn.add(new_anime_model)
                conn.commit()
                conn.refresh(new_anime_model)
            except Exception as error:
                print()
                print(f'Erro ao salvar o Anime: {nome}!')
                print(error)

        return new_anime_model

    def busca_anime_by_id(self, id: int, db: ConexaoDB) -> str:
        """_summary_
        Args:
            id (int): Buscaremos o ANIME pelo ID
            db (ConexaoDB): Class ConexaoDB para acessarmos o banco de dados.

        Raises:
            Exception: Se o ID não existir, retornamos None

        Returns:
            str: Retornamos o nome do Anime
        """
        if not isinstance(id, int):
            raise Exception('ID deve ser uma valor inteiro!!')

        with db.session() as conn:
            try:
                query = select(AnimeModel.nome).where(AnimeModel.id == id)
                for list_anime in conn.execute(query).first():
                    return list_anime
            except TypeError:
                return None

    def busca_all_animes(self, db: ConexaoDB) -> list:
        """_summary_

        Args:
            db (ConexaoDB): Class ConexaoDB para acessarmos o banco de dados.

        Returns:
            list: Retornamos em formato de lista todos os animes.
        """
        with db.session() as conn:
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


if __name__ == "__main__":
    myrepo = RepositoryAnime()
    con_db = ConexaoDB()
    # print(myrepo.busca_anime_by_id(11, con_db))
    # print(myrepo.busca_all_animes(con_db))
    myrepo.cria_anime(
        nome='Leviathan37',
        data_lancamento=date(day=10, month=7, year=2025),
        descricao="""É uma série steampunk adaptada do livro de Scott
        Westerfeld. A história se passa num universo alternativo para 1914,
        onde existem criaturas vivas (como navios dirigidos) e máquinas
        biológicas. Dois protagonistas — um príncipe (Aleksandar) e uma
        garota disfarçada de menino (Deryn)""",
        db=con_db
    )
