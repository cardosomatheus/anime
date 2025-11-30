from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String, Integer, Date
from datetime import date

from typing import Optional
from source.model.base_model import Base


class AnimeModel(Base):
    __tablename__ = "tb_anime"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    data_lancamento: Mapped[date] = mapped_column(Date)
    descricao: Mapped[Optional[str]]

    def __repr__(self):
        return (
            f"TB_ANIME(id={self.id}, "
            f"nome={self.nome} "
            f"data_lancamento={self.data_lancamento} "
            f"descricao={self.descricao})"
        )

    def to_dict(self) -> dict:
        return {
          "id": self.id,
          "nome": self.nome,
          "data_lancamento": self.data_lancamento,
          "descricao": self.descricao
        }
