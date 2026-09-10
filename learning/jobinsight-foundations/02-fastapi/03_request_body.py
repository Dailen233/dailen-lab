from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="JobInsight Candidate API",
    description="Pydantic 请求体练习",
    version="0.3.0"
)

class CandidateCreate(BaseModel):
    name: str = Field(min_length=1, max_length=30)
    target_job: str = Field(min_length=1, max_length=50)
    skills: list[str] = Field(min_length=1)

candidates = [
    {
        "id": 1,
        "name": "小明",
        "target_job": "Python 后端开发",
        "skills": ["Python", "Git"]
    }
]

@app.get("/candidates")
def get_candidates():
    return {
        "total": len(candidates),
        "data": candidates
    }


@app.post("/candidates", status_code=201)
def create_candidate(candidate: CandidateCreate):
    new_candidate = {
        "id": len(candidates) + 1,
        **candidate.model_dump()
    }

    candidates.append(new_candidate)
    return new_candidate
