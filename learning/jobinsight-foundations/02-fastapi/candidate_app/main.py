from fastapi import FastAPI

from candidate_app.routers.candidates import router as candidates_router


app = FastAPI(title="JobInsight 候选人管理 Demo")

app.include_router(candidates_router)

