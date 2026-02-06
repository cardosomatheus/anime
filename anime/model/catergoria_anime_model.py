from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer
from anime.model.base import Base


class AnimeModel(Base):
    __tablename__ = "tb_categoria_anime"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_anime: Mapped[int] = mapped_column(Integer)
    id_categoria: Mapped[int] = mapped_column(Integer)
