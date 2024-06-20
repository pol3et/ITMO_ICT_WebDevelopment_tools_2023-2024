from sqlmodel import SQLModel, Field, Session, create_engine
import os
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DB_URL"), echo=True)


class Article(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    url: str
    text: str


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


init_db()