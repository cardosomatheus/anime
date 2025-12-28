from pydantic import BaseModel, RootModel
from datetime import date
from typing import List


class AnimeSchemaIn(BaseModel):
    nome: str = None
    data_lancamento: date | None = None
    descricao: str | None = None


class AnimeSchemaOut(BaseModel):
    id: int
    nome: str
    data_lancamento: date | None
    descricao: str | None


class ListAnimeSchemaOut(RootModel):
    root: List[AnimeSchemaOut]
