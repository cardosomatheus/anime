from pydantic import BaseModel
from datetime import datetime, timezone


class UsuarioDtoOut(BaseModel):
    username: str
    is_admin: bool | None = False
    criado_em: datetime | None = datetime.now(timezone.utc)


class UsuarioDtoIn(UsuarioDtoOut):
    password_hash: str
