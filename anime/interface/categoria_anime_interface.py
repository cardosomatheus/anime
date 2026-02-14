from abc import ABC, abstractmethod


# Interface de Categoria
class IcategoriaAnimeRepository(ABC):

    @abstractmethod
    def vincula_categoria_anime(self):
        pass

    @abstractmethod
    def remove_categoria_anime(self):
        pass

    @abstractmethod
    def busca_all_categorias(self):
        pass
