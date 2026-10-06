from time import perf_counter
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from candidate_app.routers import ai, practice
from candidate_app.routers.candidates import router as candidates_router


app = FastAPI(title="JobInsight 候选人管理 Demo")


@app.get("/health", tags=["运行检查"])
def health_check():
    return {
        "status": "ok",
        "service": "jobinsight-learning",
    }


@app.middleware("http")
async def record_request_time(request: Request, call_next):
    start_time = perf_counter()

    print(f"【中间件】收到请求：{request.method} {request.url.path}")

    response = await call_next(request)

    elapsed_ms = (perf_counter() - start_time) * 1000

    response.headers["X-Process-Time-Ms"] = f"{elapsed_ms:.2f}"

    print(
        f"【中间件】准备返回："
        f"状态码={response.status_code}，"
        f"耗时={elapsed_ms:.2f} ms"
    )

    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=[
        "Content-Type",
        "X-Learning-Demo",
        "Authorization",
    ],
    expose_headers=["X-Process-Time-Ms"],
)

app.include_router(candidates_router)
app.include_router(ai.router)
app.include_router(practice.router)
