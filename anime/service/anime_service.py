from anime.interface.anime_interface import IanimeRepository
from anime.model.anime_model import AnimeModel
from anime.exception.anime_exception import AnimeIdNuloError
from anime.exception.anime_exception import AnimeIdInvalidoError
from anime.exception.anime_exception import AnimeNaoEncontrado
from datetime import date


class ServiceAnime:
    def __init__(self, repository_anime: IanimeRepository) -> None:
        self.repository_anime = repository_anime

    def __valida_anime_encontrado(self,
                                  anime: dict,
                                  ind_multiplo: int = 0) -> None:

        if anime is None and ind_multiplo == 0:
            raise AnimeNaoEncontrado("Anime não Encontrado pelo ID")

        elif anime is None and ind_multiplo == 1:
            raise AnimeNaoEncontrado("Animes Não encontrados")

    def __valida_id_nulo_inteiro(self, id: int) -> None:
        """ Valida se o ID é nulo ou não é inteiro."""
        if id is None:
            raise AnimeIdNuloError("O ID Está nulo.")

        if not isinstance(id, int):
            raise AnimeIdInvalidoError('ID precisa ser um Inteiro')

    def __identifica_campos_anime(self, dict_columns: dict) -> dict:
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
        """ Retorna a consulta do repository"""
        self.__valida_id_nulo_inteiro(id=id)
        byanime = self.repository_anime.busca_anime_by_id(id=id)
        self.__valida_anime_encontrado(anime=byanime)
        return byanime

    def busca_all_animes(self) -> dict:
        """ Retorna a consulta do repository"""
        all_anime_model = self.repository_anime.busca_all_animes()
        self.__valida_anime_encontrado(all_anime_model[0], ind_multiplo=1)
        return all_anime_model

    def deleta_anime(self, id: int) -> dict:
        """
        Deleta anime pelo repository
        obs: As validações são feitas na self.busca_anime_by_id
        """
        self.busca_anime_by_id(id=id)
        self.repository_anime.deleta_anime(id=id)
        return {"sucess": True, "info": "anime deletado."}

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
