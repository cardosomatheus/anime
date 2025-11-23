from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

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

    def session(self) -> Session:
        return self._session()
