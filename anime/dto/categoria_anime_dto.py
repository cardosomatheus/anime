from pydantic import BaseModel


class CategoriaAnimeDtoIn(BaseModel):
    id_anime: int
    id_categoria: int
