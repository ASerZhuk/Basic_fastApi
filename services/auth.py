from collections.abc import AsyncGenerator
from typing import Annotated
from uuid import UUID

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)

from bd.user_db import get_user_db
from models.user import User
from services.settings import get_settings


class UserManager(BaseUserManager[User, UUID]):
    reset_password_token_secret = get_settings().secret
    verification_token_secret = get_settings().secret

    async def on_after_register(self, user: User, request: Request | None = None) -> None:
        return


async def get_user_manager(
    user_db=Depends(get_user_db),
) -> AsyncGenerator[UserManager, None]:
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    settings = get_settings()
    return JWTStrategy(secret=settings.secret, lifetime_seconds=settings.access_token_lifetime_seconds)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


fastapi_users = FastAPIUsers[User, UUID](
    get_user_manager,
    [auth_backend],
)


current_active_user = fastapi_users.current_user(active=True)

