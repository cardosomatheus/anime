from pydantic import BaseModel, RootModel
from datetime import date
from typing import List


class AnimeSchema(BaseModel):
    id: int
    nome: str
    data_lancamento: date | None
    descricao: str | None


class ListAnimeSchema(RootModel):
    root: List[AnimeSchema]


class AnimeSchemaUpdate(BaseModel):
    id: int | None = None
    nome: str = None
    data_lancamento: date | None = None
    descricao: str | None = None
