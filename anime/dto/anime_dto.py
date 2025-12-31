from pydantic import BaseModel, RootModel, ConfigDict
from datetime import date
from typing import List


class AnimeDtoIn(BaseModel):
    nome: str = None
    data_lancamento: date | None = None
    descricao: str | None = None


class AnimeDtoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    data_lancamento: date | None
    descricao: str | None


class ListAnimeDtoOut(RootModel):
    root: List[AnimeDtoOut]
