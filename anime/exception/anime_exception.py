from builtins import Exception


class AnimeException(Exception):
    status_code = 400

    def __init__(self, menssagem: str):
        super().__init__(menssagem)


class AnimeIdInvalidoError(AnimeException):
    status_code = 400


class AnimeIdNuloError(AnimeException):
    status_code = 404


class AnimeNaoEncontrado(AnimeException):
    status_code = 404
