from fastapi import FastAPI
from fastapi.testclient import TestClient

from candidate_app.routers import practice


# 创建测试应用，挂载已有的练习路由
app = FastAPI()
app.include_router(practice.router)

client = TestClient(app)


def login_headers():
    response = client.post(
        "/practice/login",
        json={
            "username": "learner",
            "password": "Learn-JobInsight-2026",
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert data["token_type"] == "bearer"

    return {
        "Authorization": f"Bearer {data['access_token']}",
    }


def test_me_without_token():
    response = client.get("/practice/me")

    assert response.status_code == 401
    assert response.json()["detail"] == "请提供 Bearer 令牌"


def test_login_with_wrong_password():
    response = client.post(
        "/practice/login",
        json={
            "username": "learner",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "用户名或密码错误"


def test_me_with_invalid_token():
    response = client.get(
        "/practice/me",
        headers={"Authorization": "Bearer wrong-token"},
    )

    assert response.status_code == 401


def test_login_then_get_me():
    response = client.get(
        "/practice/me",
        headers=login_headers(),
    )

    assert response.status_code == 200

    user = response.json()["user"]
    assert user["username"] == "learner"
    assert user["role"] == "learner"


def test_learner_cannot_access_admin():
    response = client.get(
        "/practice/admin-summary",
        headers=login_headers(),
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "需要管理员权限"