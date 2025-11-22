from abc import ABC, abstractmethod


class Ianime(ABC):

    @abstractmethod
    def busca_anime_by_id(self, id: int) -> list:
        pass

    @abstractmethod
    def busca_all_animes(self, id: int) -> list:
        pass
