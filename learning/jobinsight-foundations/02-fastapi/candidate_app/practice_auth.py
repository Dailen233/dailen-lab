from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Annotated

import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class PracticeSettings(BaseSettings):
    jwt_secret: SecretStr
    password_hash: str
    token_minutes: int = Field(default=30, ge=1)

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env.practice",
        env_file_encoding="utf-8",
        env_prefix="PRACTICE_",
    )


settings = PracticeSettings()
password_hasher = PasswordHash.recommended()
bearer = HTTPBearer(auto_error=False)

# 本节使用一个固定练习用户，暂不接用户数据库
DEMO_USER = {
    "id": 1,
    "username": "learner",
    "name": "练习用户",
    "role": "learner",
}


def auth_error(detail: str):
    return HTTPException(
        status_code=401,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )


def login_and_create_token(username: str, password: str):
    password_ok = password_hasher.verify(
        password,
        settings.password_hash,
    )

    if username != DEMO_USER["username"] or not password_ok:
        raise auth_error("用户名或密码错误")

    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=settings.token_minutes
    )

    payload = {
        "sub": str(DEMO_USER["id"]),
        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        settings.jwt_secret.get_secret_value(),
        algorithm="HS256",
    )


def get_practice_user(
    credentials: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(bearer),
    ],
):
    if credentials is None:
        raise auth_error("请提供 Bearer 令牌")

    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.jwt_secret.get_secret_value(),
            algorithms=["HS256"],
            options={"require": ["sub", "exp"]},
        )
    except InvalidTokenError:
        raise auth_error("令牌无效或已过期")

    if payload["sub"] != str(DEMO_USER["id"]):
        raise auth_error("用户不存在")

    return DEMO_USER.copy()


def require_practice_admin(
    user: dict = Depends(get_practice_user),
):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="需要管理员权限",
        )

    return user
