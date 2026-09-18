from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from candidate_app.routers.candidates import router as candidates_router


app = FastAPI(title="JobInsight 候选人管理 Demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type"],
)

app.include_router(candidates_router)

