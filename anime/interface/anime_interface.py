from abc import ABC, abstractmethod


class IanimeRepository(ABC):

    @abstractmethod
    def cria_anime(self):
        pass

    @abstractmethod
    def busca_anime_by_id(self):
        pass

    @abstractmethod
    def busca_all_animes(self):
        pass

    @abstractmethod
    def atualiza_anime(self):
        pass

    @abstractmethod
    def deleta_anime(self):
        pass
