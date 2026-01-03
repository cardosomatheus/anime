from pydantic import BaseModel, ConfigDict, RootModel
from datetime import datetime, timezone
from typing import List


class UsuarioDtoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    is_admin: bool | None = False
    criado_em: datetime | None = datetime.now(timezone.utc)


class UsuarioDtoIn(UsuarioDtoOut):
    password_hash: str


class ListUsuarioDtoOut(RootModel):
    root: List[UsuarioDtoOut]
