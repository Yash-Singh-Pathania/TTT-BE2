# app/routes/user.py

from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserInDB

router = APIRouter()

@router.post("/users/", response_model=UserInDB)
async def create_user(user: UserCreate):
    user_obj = await User.create(**user.dict())
    return await UserInDB.from_tortoise_orm(user_obj)

@router.get("/users/{user_id}", response_model=UserInDB)
async def read_user(user_id: int):
    user_obj = await User.filter(id=user_id).first()
    if user_obj is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await UserInDB.from_tortoise_orm(user_obj)

@router.put("/users/{user_id}", response_model=UserInDB)
async def update_user(user_id: int, user: UserUpdate):
    user_obj = await User.filter(id=user_id).first()
    if user_obj is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_obj = await User.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await UserInDB.from_tortoise_orm(user_obj)

@router.delete("/users/{user_id}", response_model=UserInDB)
async def delete_user(user_id: int):
    user_obj = await User.filter(id=user_id).first()
    if user_obj is None:
        raise HTTPException(status_code=404, detail="User not found")
    await User.filter(id=user_id).delete()
    return await UserInDB.from_tortoise_orm(user_obj)
