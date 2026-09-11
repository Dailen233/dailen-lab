def select_candidates(
    candidates: list[dict[str, str]],
    target_job: str | None = None
) -> list[str]:
    target_candidates = []
    if target_job is not None:
        target_candidates = [
            candidate["name"]
            for candidate in candidates
            if target_job in candidate["target_job"]
        ]
    else:
        target_candidates = [
            candidate["name"]
            for candidate in candidates
        ]

    return target_candidates

def find_candidate_index(
    candidates: list[dict[str, str]],
    name: str
) -> int | None:
    for index, candidate in enumerate(candidates):
        if candidate["name"] == name:
            return index

    return None

candidates = [
    {"name": "小明", "target_job": "Python 后端开发"},
    {"name": "小红", "target_job": "前端开发"},
    {"name": "小刚", "target_job": "FastAPI 后端开发"}
]

print(select_candidates(candidates))
print(select_candidates(candidates, "后端"))
print(select_candidates(candidates, "测试"))


print(find_candidate_index(candidates, "小明"))  # 0
print(find_candidate_index(candidates, "小刚"))  # 2
print(find_candidate_index(candidates, "小李"))  # None