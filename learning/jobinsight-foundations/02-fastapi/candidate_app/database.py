from pathlib import Path
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session


DB_PATH = (
    Path(__file__).resolve().parent.parent
    / "candidates_learning.db"
)

if not DB_PATH.is_file():
    raise FileNotFoundError("请先运行 07_sqlite_basics.py 创建练习数据库")

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)


class Base(DeclarativeBase):
    pass


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
