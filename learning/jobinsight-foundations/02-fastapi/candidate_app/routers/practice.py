from typing import Annotated

from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, Query, HTTPException, UploadFile
from candidate_app.schemas import CandidateResponse
from candidate_app.practice_auth import (
    get_practice_user,
    login_and_create_token,
    require_practice_admin,
)

router = APIRouter(
    prefix="/practice",
    tags=["依赖注入练习"]
)


def get_pagination(
    limit: int = Query(default=10, ge=1, le=50),
    offset: int = Query(default=0, ge=0)
):
    print("① 正在执行分页依赖")

    return {
        "limit": limit,
        "offset": offset
    }


PaginationDep = Annotated[
    dict[str, int],
    Depends(get_pagination)
]


@router.get("/pagination")
def show_pagination(pagination: PaginationDep):
    print("② 正在执行接口函数")

    return pagination


@router.get("/pagination-summary")
def show_pagination_summary(pagination: PaginationDep):
    return {
        "message": (
            f"跳过 {pagination['offset']} 条，"
            f"最多获取 {pagination['limit']} 条"
        )
    }


def get_practice_resource():
    print("A：准备资源")

    resource = "练习资源"

    try:
        yield resource
    finally:
        print("C：清理资源")


ResourceDep = Annotated[
    str,
    Depends(get_practice_resource)
]


@router.get("/resource")
def use_resource(
    resource: ResourceDep,
    fail: bool = False
):
    print("B：接口正在使用资源")

    if fail:
        raise HTTPException(
            status_code=400,
            detail="模拟接口处理失败"
        )

    return {"resource": resource}


@router.get(
    "/response-model",
    response_model=CandidateResponse,
)
def practice_response_model(broken: bool = False):
    result = {
        "id": 1,
        "name": "小明",
        "target_job": "Python 后端开发",
        "internal_note": "这是一条内部练习备注",
    }

    if broken:
        result.pop("target_job")

    print("接口函数准备返回：", result)

    return result


@router.post("/upload-resume")
async def upload_resume(file: UploadFile):
    max_bytes = 1024 * 1024  # 本练习最多接受 1 MiB 内容

    try:
        content = await file.read(max_bytes + 1)

        if len(content) > max_bytes:
            raise HTTPException(
                status_code=413,
                detail="文件不能超过 1 MiB",
            )

        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            raise HTTPException(
                status_code=400,
                detail="本练习只接受 UTF-8 编码的文本文件",
            )

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="文件内容不能为空",
            )

        return {
            "filename": file.filename,
            "size_bytes": len(content),
            "character_count": len(text),
            "preview": text[:100],
        }
    finally:
        await file.close()


@router.get("/me")
def practice_me(user: dict = Depends(get_practice_user)):
    return {
        "message": "认证成功",
        "user": user,
    }


class PracticeLoginInput(BaseModel):
    username: str = Field(min_length=1, max_length=64)
    password: str = Field(min_length=1, max_length=256)


class PracticeTokenResponse(BaseModel):
    access_token: str
    token_type: str


@router.post("/login", response_model=PracticeTokenResponse)
def practice_login(data: PracticeLoginInput):
    token = login_and_create_token(
        data.username,
        data.password,
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@router.get("/admin-summary")
def practice_admin_summary(
    user: dict = Depends(require_practice_admin),
):
    return {
        "message": "管理员接口访问成功",
        "operator": user["username"],
    }
