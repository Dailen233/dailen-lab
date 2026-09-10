from fastapi import FastAPI


app = FastAPI(
    title="JobInsight Learning API",
    description="JobInsight 项目的 FastAPI 基础练习",
    version="0.1.0"
)


@app.get("/")
def read_root():
    return {
        "message": "欢迎使用 JobInsight API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


