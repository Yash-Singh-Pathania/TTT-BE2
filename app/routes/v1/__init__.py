from fastapi import APIRouter
from .user import router as users_router
from .organizations import router as organizations_router

router = APIRouter(prefix="/v1")

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(organizations_router, prefix="/organizations", tags=["organizations"])
