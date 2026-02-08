from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from anime.model.base import Base
from typing import Optional


class Categoria_model(Base):
    __tablename__ = "tb_categoria"
    id:        Mapped[int] = mapped_column(primary_key=True)
    nome:      Mapped[str] = mapped_column(String(50))
    descricao: Mapped[Optional[str]]
