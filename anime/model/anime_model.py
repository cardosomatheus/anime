from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer, Date
from datetime import date
from typing import Optional
from anime.model.base import Base


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

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__mapper__.columns}
