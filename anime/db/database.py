from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from dotenv import load_dotenv
import os


class ConexaoDB:
    load_dotenv()

    def mysession(self) -> Session:
        engine = create_engine(
            URL.create(
                "postgresql+psycopg2",
                username=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host="localhost",
                port=5432,
                database=os.getenv("POSTGRES_DB"),
            ),
            future=True,
        )

        return Session(engine)
