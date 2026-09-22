from typing import Annotated

from fastapi import APIRouter, Depends, Query, HTTPException


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

