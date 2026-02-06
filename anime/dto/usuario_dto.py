from pydantic import BaseModel, ConfigDict, RootModel
from datetime import datetime, timezone
from typing import List


# DTO de saida de usuario
class UsuarioDtoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    is_admin: bool | None = False
    criado_em: datetime | None = datetime.now(timezone.utc)


# DTO de saida de usuario em formato de listagem 
class ListUsuarioDtoOut(RootModel):
    root: List[UsuarioDtoOut]


# DTO de entrada de usuario
class UsuarioDtoIn(UsuarioDtoOut):
    password_hash: str


# DTO de que valida o token de saida.
class UsuarioValidaTokenDtoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    password_hash: str | None = None
