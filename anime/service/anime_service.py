from anime.interface.anime_interface import IanimeRepository
from anime.model.anime_model import AnimeModel
from anime.dto.anime_dto import (
    AnimeDtoIn,
    AnimeDtoOut,
    ListAnimeDtoOut
)
from anime.exception.anime_exception import (
    AnimeIdNuloError,
    AnimeIdInvalidoError,
    AnimeNaoEncontrado)


class ServiceAnime:
    def __init__(self, repository_anime: IanimeRepository) -> None:
        self.repository_anime = repository_anime

    def cria_anime(self, dto: AnimeDtoIn) -> dict:
        """Cria novo anime pelo repository"""
        anime_model = AnimeModel(
            nome=dto.nome,
            data_lancamento=dto.data_lancamento,
            descricao=dto.descricao
        )

        self.repository_anime.cria_anime(anime=anime_model)
        return {"message": f"Anime {dto.nome} Criado com sucesso."}

    def atualiza_anime(self, dto: AnimeDtoOut) -> dict:
        """ Atualiza anime pelo repository"""
        self.busca_anime_by_id(id=dto.id)
        anime_model = AnimeModel(
            id=dto.id,
            nome=dto.nome,
            data_lancamento=dto.data_lancamento,
            descricao=dto.descricao
        )
        self.repository_anime.atualiza_anime(anime=anime_model)
        return {'message': f'{dto.nome} Atualizado com sucesso'}

    def deleta_anime(self, id: int) -> dict:
        """ Deleta anime pelo repository """
        
        self.busca_anime_by_id(id=id)
        print('aqui')
        self.repository_anime.deleta_anime(id=id)
        return {"message": "anime deletado."}

    def busca_anime_by_id(self, id: int) -> AnimeDtoOut:
        """ Retorna a consulta do repository"""
        self.__valida_id_nulo_inteiro(id=id)
        dto_anime = self.repository_anime.busca_anime_by_id(id=id)
        print(dto_anime)
        self.__valida_anime_encontrado(anime=dto_anime)
        return AnimeDtoOut.model_validate(dto_anime)

    def busca_all_animes(self) -> ListAnimeDtoOut:
        """ Retorna a consulta do repository"""
        dto_all_anime = self.repository_anime.busca_all_animes()
        self.__valida_anime_encontrado(dto_all_anime[0], ind_multiplo=1)
        return ListAnimeDtoOut.model_validate(dto_all_anime)

    def __valida_id_nulo_inteiro(self, id: int) -> None:
        """ Valida se o ID é nulo ou não é inteiro."""
        if id is None:
            raise AnimeIdNuloError("O ID Está nulo.")

        if not isinstance(id, int):
            raise AnimeIdInvalidoError('ID precisa ser um Inteiro')

    def __valida_anime_encontrado(self,
                                  anime: AnimeModel,
                                  ind_multiplo: int = 0) -> None:
        if anime is None and ind_multiplo == 0:
            raise AnimeNaoEncontrado("Anime não Encontrado pelo ID")

        elif anime is None and ind_multiplo == 1:
            raise AnimeNaoEncontrado("Animes Não encontrados")
