from pathlib import Path

from fastapi import FastAPI, HTTPException
from sqlalchemy import Text, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from pydantic import BaseModel, Field

DB_PATH = Path(__file__).resolve().parent / "candidates_learning.db"

if not DB_PATH.is_file():
    raise FileNotFoundError("请先运行 07_sqlite_basics.py 创建练习数据库")

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)

app = FastAPI(title="JobInsight 数据库接口 Demo")


class Base(DeclarativeBase):
    pass


class Candidate(Base):
    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    target_job: Mapped[str] = mapped_column(Text, nullable=False)


class CandidateInput(BaseModel):
    name: str = Field(min_length=1, max_length=30)
    target_job: str = Field(min_length=1, max_length=50)


class CandidateResponse(BaseModel):
    id: int
    name: str
    target_job: str


class CandidateListResponse(BaseModel):
    total: int
    data: list[CandidateResponse]


class CandidateDeleteResponse(BaseModel):
    message: str
    data: CandidateResponse


def candidate_to_dict(candidate: Candidate) -> dict:
    return {
        "id": candidate.id,
        "name": candidate.name,
        "target_job": candidate.target_job,
    }


@app.get("/candidates", response_model=CandidateListResponse)
def get_candidates():
    with Session(engine) as session:
        statement = select(Candidate).order_by(Candidate.id)
        candidates = session.scalars(statement).all()

        return {
            "total": len(candidates),
            "data": [
                candidate_to_dict(candidate)
                for candidate in candidates
            ]
        }


@app.get("/candidates/{candidate_id}", response_model=CandidateResponse)
def get_candidate(candidate_id: int):
    with Session(engine) as session:
        candidate = session.get(Candidate, candidate_id)

        if candidate is None:
            raise HTTPException(
                status_code=404,
                detail="候选人不存在"
            )

        return candidate_to_dict(candidate)


@app.post(
    "/candidates", 
    status_code=201,
    response_model=CandidateResponse,
)
def create_candidate(data: CandidateInput):
    with Session(engine) as session:
        candidate = Candidate(
            name=data.name,
            target_job=data.target_job
        )

        session.add(candidate)
        session.commit()
        session.refresh(candidate)

        return candidate_to_dict(candidate)


@app.put("/candidates/{candidate_id}", response_model=CandidateResponse)
def update_candidate(candidate_id: int, data: CandidateInput):
    with Session(engine) as session:
        candidate = session.get(Candidate, candidate_id)

        if candidate is None:
            raise HTTPException(
                status_code=404,
                detail="候选人不存在"
            )

        candidate.name = data.name
        candidate.target_job = data.target_job

        session.commit()
        session.refresh(candidate)

        return candidate_to_dict(candidate)


@app.delete("/candidates/{candidate_id}",response_model=CandidateDeleteResponse)
def delete_candidate(candidate_id: int):
    with Session(engine) as session:
        candidate = session.get(Candidate, candidate_id)

        if candidate is None:
            raise HTTPException(
                status_code=404,
                detail="候选人不存在"
            )

        deleted_data = candidate_to_dict(candidate)

        session.delete(candidate)
        session.commit()

        return {
            "message": "候选人删除成功",
            "data": deleted_data
        }

