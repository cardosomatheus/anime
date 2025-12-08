from anime.repository.anime_repository import RepositoryAnime
from anime.model.anime_model import AnimeModel
from datetime import date

class ServiceAnime:
    def __init__(self, repository_anime: RepositoryAnime) -> None:
        self.repository_anime = repository_anime

    def __valida_anime_encontrado(self, anime: dict) -> None:
        if anime is None:
            raise Exception('Anime não identificado.')  

    def __valida_existencia_anime(self, id: int) -> None:
        """ Confirma a existencia do anime pelo ID
        Args: id (int): ID do anime
        Raises: Exception: Anime não existe
        """
        if self.repository_anime.busca_anime_by_id(id=id) is None:
            raise Exception('Anime não encontrado.')

    def __valida_id_nulo_inteiro(self, id: int) -> None:
        """ Valida se o ID é nulo ou não é inteiro.
        Args: id (int): ID do anime
        Raises:
            ValueError: ID não Nulo?
            Exception: ID não inteir?
        """
        if id is None:
            raise ValueError("ID não informado.")

        if not isinstance(id, int):
            raise Exception('ID Precisa ser um numero inteiro!!')

    def __identifica_campos_anime(self, dict_columns: dict) -> dict:
        """Filtra apenas Chaves(colnas) contidos na AnimeModel.
        Args: dict_columns (dict): Coluna: novo valor
        Returns: Apenas campos contidos na AnimeModel.
        """
        return {
            key: value for key, value in dict_columns.items()
            if key in AnimeModel.__table__.columns.keys()
        }

    def __valida_criacao_anime(self,
                               nome: str,
                               data_lancamento: date,
                               descricao: str) -> None:
        """Validações simples para criar um anime.
        Args:
            nome (str): nome
            data_lancamento (date): data de lançamento
            descricao (str): descricao
        Raises:
            Exception: data_lancamento é um date?
            Exception: nome é um str?
            Exception: descricao é um str?
        """

        if not isinstance(data_lancamento, date):
            raise Exception('A data incorreta.')

        if not isinstance(nome, str):
            raise Exception('O nome deve ser string.')

        if descricao is not None and not isinstance(descricao, str):
            raise Exception('O nome deve ser string.')

    def busca_anime_by_id(self, id: int) -> dict:
        """ Retorna a consulta do repository
        Args:  id (int): ID do anime
        Returns: dict: sucess and message
        """

        try:
            self.__valida_id_nulo_inteiro(id=id)
            byanime = self.repository_anime.busca_anime_by_id(id=id)
            self.__valida_anime_encontrado(anime=byanime)          
            return {"sucess": True,
                    "type": "Anime",
                    "Info": byanime.to_dict()}

        except Exception as error:
            print(error)
            return {"sucess": False, "message": str(error)}

    def busca_all_animes(self) -> dict:
        """ Retorna a consulta do repository
        Args:  id (int): ID do anime
        Returns: dict: sucess and message
        """
        try:
            all_anime_model = self.repository_anime.busca_all_animes()
            return {
                "sucess": True,
                "type": "Anime",
                "Info": all_anime_model
            }
            # [anime.to_dict() for anime in all_anime_model]
        except Exception as error:
            return {"sucess": False, "message": str(error)}

    def deleta_anime(self, id: int) -> dict:
        """ Deleta anime pelo repository
        Args:  id (int): ID do anime
        Returns: dict: sucess and message
        """

        try:
            self.__valida_id_nulo_inteiro(id=id)
            self.__valida_existencia_anime(id=id)
            self.repository_anime.deleta_anime(id=id)
            return {"sucess": True, "type": "Anime", "Info": "anime deletado."}
        except Exception as error:
            return {"sucess": False, "message": str(error)}

    def atualiza_anime(self,
                       dict_Anime_model: dict) -> dict:
        """ Atualiza anime pelo repository
        Args:  id (int): ID do anime
        Returns: dict: sucess and message
        """
        try:
            dict_Anime_model = self.__identifica_campos_anime(
                dict_columns=dict_Anime_model
            )
            self.__valida_id_nulo_inteiro(id=dict_Anime_model.get('id'))
            self.__valida_existencia_anime(id=dict_Anime_model.get('id'))

            self.repository_anime.atualiza_anime(
                dict_Anime_model=dict_Anime_model
            )

            return {"sucess": True, "type": "Anime", "Info": "Anime editado"}
        except Exception as error:
            return {"sucess": False, "message": str(error)}

    def cria_anime(self,
                   nome: str,
                   data_lancamento: date,
                   descricao: str) -> dict:
        """Cria novo anime pelo repository
        Args:
            nome (str): nome
            data_lancamento (date): data lançamento
            descricao (str): descricao
        Returns: dict: sucess and message
        """
        try:
            self.__valida_criacao_anime(
                nome=nome,
                data_lancamento=data_lancamento,
                descricao=descricao
            )

            new_anime = self.repository_anime.cria_anime(
                nome=nome,
                data_lancamento=data_lancamento,
                descricao=descricao
                )

            return {
                    "sucess": True,
                    "type": "Anime",
                    "Info": f"Anime {new_anime.nome} cadastrado com sucesso."
                    }
        except Exception as error:
            return {"sucess": False, "message": str(error)}


if __name__ == "__main__":
    from anime.db.database import ConexaoDB

    con_db = ConexaoDB().session()
    myrepo = RepositoryAnime(con_db)
    service = ServiceAnime(repository_anime=myrepo)

    # print(service.busca_anime_by_id(id=1))

    # print(service.cria_anime(
    #    nome='Leviathan61',
    #    data_lancamento=date(day=10, month=7, year=2025),
    #    descricao="""É uma série steampunk adaptada do livro de Scott
    #    Westerfeld. A história se passa num universo alternativo para 1914,
    #    onde existem criaturas vivas (como navios dirigidos) e máquinas
    #    biológicas. Dois protagonistas — um príncipe (Aleksandar) e uma
    #    garota disfarçada de menino (Deryn)"""
    # )
    # )
    print(service.busca_anime_by_id(1))
    # service.deleta_anime(10)
    # print(service.atualiza_anime({'id': 1,
    #                               'nome': 'Fullmetal Alchemist',
    #                               'i': 39}))
    # print(myrepo.busca_all_animes())
