from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from dotenv import load_dotenv
import os


class ConexaoDB:
    load_dotenv()

    # Gera uma sessão do banco sempre que for chamada.
    def mysession(self) -> Session:
        engine = create_engine(
            URL.create(
                "postgresql+psycopg2",
                username=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host="localhost",
                port=os.getenv("DB_PORTA"),
                database=os.getenv("POSTGRES_DB"),
            ),
            future=True,
        )

        return Session(engine)
