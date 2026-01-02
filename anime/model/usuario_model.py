from anime.model.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean, Text, DATETIME
from datetime import datetime


class UsuarioModel(Base):
    __tablename__ = "tb_usuario"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(Text)
    criado: Mapped[datetime] = mapped_column(DATETIME)
    ind_admin: Mapped[bool] = mapped_column(Boolean)

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__mapper__.columns}
