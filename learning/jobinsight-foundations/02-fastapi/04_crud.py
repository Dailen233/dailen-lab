from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="JobInsight Candidate CRUD API",
    description="候选人增删改查练习",
    version="0.4.0"
)

class CandidateInput(BaseModel):
    name: str = Field(min_length=1, max_length=30)
    target_job: str = Field(min_length=1, max_length=50)
    skills: list[str] = Field(min_length=1)


candidates = [
    {
        "id": 1,
        "name": "小明",
        "target_job": "Python 后端开发",
        "skills": ["Python", "Git"]
    },
    {
        "id": 2,
        "name": "小红",
        "target_job": "前端开发",
        "skills": ["HTML", "CSS", "JavaScript"]
    }
]


def find_candidate_index(candidate_id: int):
    for index, candidate in enumerate(candidates):
        if candidate["id"] == candidate_id:
            return index

    raise HTTPException(
        status_code=404,
        detail="候选人不存在"
    )


@app.get("/candidates")
def get_candidates():
    return {
        "total": len(candidates),
        "data": candidates
    }


@app.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: int):
    index = find_candidate_index(candidate_id)
    return candidates[index]


@app.post("/candidates", status_code=201)
def create_candidate(candidate: CandidateInput):
    new_id = max(
        (item["id"] for item in candidates),
        default=0
    ) + 1

    new_candidate = {
        "id": new_id,
        **candidate.model_dump()
    }

    candidates.append(new_candidate)
    return new_candidate


@app.put("/candidates/{candidate_id}")
def update_candidate(
    candidate_id: int,
    candidate: CandidateInput
):
    index = find_candidate_index(candidate_id)

    updated_candidate = {
        "id": candidate_id,
        **candidate.model_dump()
    }

    candidates[index] = updated_candidate
    return updated_candidate


@app.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int):
    index = find_candidate_index(candidate_id)
    deleted_candidate = candidates.pop(index)

    return {
        "message": "候选人删除成功",
        "data": deleted_candidate
    }
