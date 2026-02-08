from anime.interface.categoria_anime_interface import IcategoriaAnimeRepository
from anime.model.catergoria_anime_model import CategoriaAnimeModel
from anime.dto.categoria_dto import ListCategoriaDtoOut
from anime.dto.categoria_anime_dto import CategoriaAnimeDtoIn


class CategoriaAnimeService:

    def __init__(self, repository: IcategoriaAnimeRepository):
        self.repository = repository

    def busca_all_categoria(self):
        # Busca as categorias retornadas.
        all_categorias = self.repository.busca_all_categorias()
        return ListCategoriaDtoOut.model_validate(all_categorias)

    def adiciona_vinculo(self, dto: CategoriaAnimeDtoIn):
        try:
            model = CategoriaAnimeModel(
                id_anime=dto.id_anime,
                id_categoria=dto.id_categoria
            )

            self.repository.vincula_categoria_anime(model)

            return {'result': True, 'message': 'Anime categorizado.'}
        except Exception as error:
            message = {
                'result': False,
                'message': 'Falha em categorizar o anime.',
                'error': error.args[0]
            }
            raise Exception(message)

    def remove_vinculo(self, dto: CategoriaAnimeDtoIn):
        try:
            model = CategoriaAnimeModel(
                id_anime=dto.id_anime,
                id_categoria=dto.id_categoria
            )

            self.repository.remove_categoria_anime(model)

            return {'result': True, 'message': 'Categoria removida'}
        except Exception as error:
            message = {
                'result': False,
                'message': 'Falha na remoção da categoria',
                'error': error.args[0]
            }
            raise Exception(message)
