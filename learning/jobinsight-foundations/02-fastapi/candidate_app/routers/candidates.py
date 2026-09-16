from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from candidate_app.database import SessionDep
from candidate_app.models import Candidate
from candidate_app.schemas import (
    CandidateResponse,
    CandidateInput,
    CandidateListResponse,
    CandidateDeleteResponse,
)


router = APIRouter(tags=["候选人"])

def candidate_to_dict(candidate: Candidate) -> dict:
    return {
        "id": candidate.id,
        "name": candidate.name,
        "target_job": candidate.target_job,
    }


@router.get("/candidates", response_model=CandidateListResponse)
def get_candidates(session: SessionDep):
    statement = select(Candidate).order_by(Candidate.id)
    candidates = session.scalars(statement).all()

    return {
        "total": len(candidates),
        "data": [
            candidate_to_dict(candidate)
            for candidate in candidates
        ]
    }


@router.get(
    "/candidates/{candidate_id}",
    response_model=CandidateResponse
)
def get_candidate(candidate_id: int, session: SessionDep):
    candidate = session.get(Candidate, candidate_id)

    if candidate is None:
        raise HTTPException(
            status_code=404,
            detail="候选人不存在"
        )

    return candidate_to_dict(candidate)


@router.post(
    "/candidates", 
    status_code=201,
    response_model=CandidateResponse,
)
def create_candidate(data: CandidateInput, session: SessionDep):
    candidate = Candidate(
        name=data.name,
        target_job=data.target_job
    )

    session.add(candidate)
    session.commit()
    session.refresh(candidate)

    return candidate_to_dict(candidate)


@router.put("/candidates/{candidate_id}", response_model=CandidateResponse)
def update_candidate(
    candidate_id: int, 
    data: CandidateInput,
    session: SessionDep
):
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


@router.delete("/candidates/{candidate_id}",response_model=CandidateDeleteResponse)
def delete_candidate(candidate_id: int, session: SessionDep):
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

