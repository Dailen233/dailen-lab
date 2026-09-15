from pathlib import Path

from sqlalchemy import Text, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DB_PATH = Path(__file__).resolve().parent / "candidates_learning.db"


class Base(DeclarativeBase):
    pass


class Candidate(Base):
    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    target_job: Mapped[str] = mapped_column(Text, nullable=False)


def main():
    if not DB_PATH.is_file():
        raise FileNotFoundError(f"请先运行 07_sqlite_basics.py: {DB_PATH}")

    engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)

    with Session(engine) as session:
        statement = select(Candidate).order_by(Candidate.id)
        candidates = session.scalars(statement).all()

        print("\n候选人列表：")
        for candidate in candidates:
            print(candidate.id, candidate.name, candidate.target_job)

        print("\n按主键查询：")
        person = session.get(Candidate, 2)

        if person is not None:
            print("对象类型：", type(person).__name__)
            print("姓名：", person.name)
            print("目标岗位：", person.target_job)


        statement = select(Candidate).where(Candidate.name == "小红")
        candidates = session.scalars(statement).all()

        for candidate in candidates:
            print(candidate.id, candidate.name, candidate.target_job)

        print("\n更新候选人：")
        person = session.get(Candidate, 3)

        if person is not None:
            person.target_job = "AI 应用开发"
            session.commit()
            print("更新已提交")
        else:
            print("候选人不存在")

    with Session(engine) as session:
        person = session.get(Candidate, 3)

        if person is not None:
            print("新会话读取：", person.id, person.name, person.target_job)

    with Session(engine) as session:
        person = session.get(Candidate, 3)

        if person is not None:
            person.target_job = "临时岗位"

            session.flush()
            print("flush 后：", person.target_job)

            session.rollback()
            print("rollback 后：", person.target_job)

if __name__ == "__main__":
    main()


