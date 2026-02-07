from anime.interface.categoria_anime_interface import IcategoriaAnimeRepository
from anime.model.catergoria_anime_model import CategoriaAnimeModel
from anime.dto.categoria_anime_dto import CategoriaAnimeDtoIn


class CategoriaAnimeService:

    def __init__(self, repositoty: IcategoriaAnimeRepository):
        self.repository = repositoty

    def adiciona_vinculo(self, dto: CategoriaAnimeDtoIn):
        try:
            model = CategoriaAnimeModel(
                id_anime=dto.id_anime,
                id_categoria=dto.id_categoria
            )

            self.repository.vincula_categoria_anime(model)

            return {'result': True, 'message': 'Anime categorizado.'}
        except Exception as error:
            return {
                'result': False,
                'message': 'Falha em categorizar o anime.',
                'error': error
            }

    def remove_vinculo(self, dto: CategoriaAnimeDtoIn):
        try:
            model = CategoriaAnimeModel(
                id_anime=dto.id_anime,
                id_categoria=dto.id_categoria
            )

            self.repository.remove_categoria_anime(model)

            return {'result': True, 'message': 'Categoria removida'}
        except Exception as error:
            return {
                'result': False,
                'message': 'Falha na remoção da categoria',
                'error': error
            }
