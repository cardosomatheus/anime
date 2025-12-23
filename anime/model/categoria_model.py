from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from typing import Optional


class Categoria(DeclarativeBase):
    __tablename__ = "tb_categoria"
    id:        Mapped[int] = mapped_column(primary_key=True)
    nome:      Mapped[str] = mapped_column(String(50))
    descricao: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return (
                f"TB_CATEGORIA(id={self.id!r}, "
                f"nome={self.nome!r}, "
                f"descricao={self.descricao!r})"
            )
