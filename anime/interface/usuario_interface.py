from abc import ABC, abstractmethod


class IusuarioRepository(ABC):

    @abstractmethod
    def criar_usuario(self):
        pass

    @abstractmethod
    def busca_usuario_by_id(self):
        pass

    @abstractmethod
    def busca_all_usuarios(self):
        pass

    @abstractmethod
    def _busca_usuario_by_nome_e_senha(self):
        pass
