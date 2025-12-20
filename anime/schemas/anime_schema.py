from pydantic import BaseModel, RootModel
from datetime import date
from typing import List


class AnimeSchema(BaseModel):
    id: int
    nome: str
    data_lancamento: date
    descricao: str


class ListAnimeSchema(RootModel):
    root: List[AnimeSchema]


class AnimeSchemaDelete(BaseModel):
    sucess: bool
    info: str
