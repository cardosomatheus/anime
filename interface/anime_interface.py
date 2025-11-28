from abc import ABC, abstractmethod


class IanimeRepository(ABC):

    @abstractmethod
    def cria_anime(self, id: int) -> list:
        pass

    @abstractmethod
    def busca_anime_by_id(self, id: int) -> list:
        pass

    @abstractmethod
    def busca_all_animes(self, id: int) -> list:
        pass

    @abstractmethod
    def atualiza_anime(self, id: int) -> list:
        pass

    @abstractmethod
    def deleta_anime(self, id: int) -> list:
        pass
