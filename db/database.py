from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from contextlib import contextmanager
from dotenv import load_dotenv
import os


class ConexaoDB:

    def __init__(self):
        load_dotenv()
        self._engine = create_engine(
            URL.create(
                "postgresql+psycopg2",
                username=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host="localhost",
                port=5433,
                database=os.getenv("POSTGRES_DB"),
            ),
            future=True,
        )
        self._session = sessionmaker(
                                     bind=self._engine,
                                     autocommit=False,
                                     autoflush=True,
                                     future=True
                                    )

    @contextmanager
    def session(self) -> Session:
        """Context manager seguro para abrir e fechar sessão."""

        db: Session = self._session()
        try:
            yield db
        finally:
            db.close()
