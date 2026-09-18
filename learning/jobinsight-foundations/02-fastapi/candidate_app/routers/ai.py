import httpx
from fastapi import APIRouter, HTTPException

from candidate_app.llm_service import generate_study_advice
from candidate_app.schemas import StudyAdviceInput, StudyAdviceResponse


router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/study-advice", response_model=StudyAdviceResponse)
def create_study_advice(data: StudyAdviceInput):
    target_job = data.target_job.strip()

    if not target_job:
        raise HTTPException(
            status_code=422,
            detail="目标岗位不能只包含空格"
        )

    try:
        advice = generate_study_advice(target_job)

    except RuntimeError:
        raise HTTPException(
            status_code=503,
            detail="后端尚未配置模型 API Key"
        ) from None

    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="模型响应超时，请稍后重试"
        ) from None

    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=502,
            detail="模型服务返回错误，状态码："
            + str(error.response.status_code)
        ) from None

    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="无法连接模型服务"
        ) from None

    except (KeyError, IndexError, TypeError, ValueError):
        raise HTTPException(
            status_code=502,
            detail="模型响应格式异常，或回答为空"
        ) from None

    return {
        "target_job": target_job,
        "advice": advice
    }

