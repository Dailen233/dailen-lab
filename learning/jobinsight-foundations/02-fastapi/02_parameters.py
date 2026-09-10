from fastapi import FastAPI, HTTPException, Query


app = FastAPI(
    title="JobInsight Candidate API",
    description="路径参数和查询参数练习",
    version="0.2.0"
)


candidates = [
    {
        "id": 1,
        "name": "小明",
        "target_job": "Python 后端开发",
        "skills": ["Python", "git"]
    },
    {
        "id": 2,
        "name": "小红",
        "target_job": "前端开发",
        "skills": ["HTML", "CSS", "JavaScript"]
    },
    {
        "id": 3,
        "name": "小刚",
        "target_job": "FastAPI 后端开发",
        "skills": ["Python", "FastAPI", "MySQL"]
    }
]


@app.get("/candidates")
def search_candidates(
    skill: str | None = None,
    target_job: str | None = None,
    limit: int = Query(default=10, ge=1, le=20)
):
    result = candidates

    if skill is not None:
        result = [
            candidate
            for candidate in candidates
            if skill in candidate["skills"]
        ]

    if target_job is not None:
        result = [
            candidate
            for candidate in result
            if target_job in candidate["target_job"]
        ]

    return {
        "total": len(result),
        "data": result[:limit]
    }



@app.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: int):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate

    raise HTTPException(
        status_code=404,
        detail="候选人不存在"
    )

