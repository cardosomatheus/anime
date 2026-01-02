from abc import ABC, abstractmethod


class IusuarioRepository(ABC):

    @abstractmethod
    def criar_usuario(self):
        pass
