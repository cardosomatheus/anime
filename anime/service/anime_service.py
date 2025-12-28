from anime.schemas.anime_schema import AnimeSchemaIn
from anime.interface.anime_interface import IanimeRepository
from anime.model.anime_model import AnimeModel
from anime.exception.anime_exception import (
    AnimeIdNuloError,
    AnimeIdInvalidoError,
    AnimeNaoEncontrado)


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
            key: value
            for key, value in dict_columns.items()
            if key in AnimeModel.__table__.columns.keys() and value is not None
        }

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
                       dict_anime: dict) -> None:
        """ Atualiza anime pelo repository
        obs: As validações são feitas na self.busca_anime_by_id
        """
        dict_anime = self.__identifica_campos_anime(dict_columns=dict_anime)
        self.busca_anime_by_id(id=dict_anime.get('id'))
        self.repository_anime.atualiza_anime(dict_anime=dict_anime)

    def cria_anime(self,
                   dto: AnimeSchemaIn) -> dict:
        """Cria novo anime pelo repository"""
        try:
            anime_model = AnimeModel(
                nome=dto.nome,
                data_lancamento=dto.data_lancamento,
                descricao=dto.descricao
            )

            self.repository_anime.cria_anime(anime=anime_model)
            return {
                    "sucess": True,
                    "type": "Anime",
                    "Info": f"Anime {dto.nome} cadastrado com sucesso."
                    }
        except Exception as error:
            return {"sucess": False, "message": str(error)}
