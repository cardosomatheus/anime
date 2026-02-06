from builtins import Exception


# Exeptions criados para usuarios
class UsuarioException(Exception):
    status = 400

    def __init__(self, mensagem):
        super().__init__(mensagem)


class UsuarioRepositoryUnique(UsuarioException):
    status_code = 409
