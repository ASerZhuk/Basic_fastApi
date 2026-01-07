from fastapi import APIRouter

from routes.health import router as health_router
from schemas.user import UserCreate, UserRead, UserUpdate
from services.auth import auth_backend, fastapi_users


router = APIRouter()

router.include_router(health_router)
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

