from pydantic import BaseModel, RootModel, ConfigDict
from typing import List


class CategoriaDtoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nome: str
    descricao: str


class ListCategoriaDtoOut(RootModel):
    root: List[CategoriaDtoOut]
