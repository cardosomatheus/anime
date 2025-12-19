from pydantic import BaseModel
from datetime import date


class AnimeSchema(BaseModel):
    id: int
    nome: str
    data_lancamento: date
    descricao: str


class ListAnimeSchema(AnimeSchema):
    list(AnimeSchema)