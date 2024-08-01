# app/routes/user.py

from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserInDB, UserUpdate
from app.schemas.base import ResponseData
from app.services.user.creator.user_creator import UserCreator

router = APIRouter()

@router.post("/signup/", response_model=UserResponse)
async def create_user(user: UserCreate):
    await UserCreator.create_user(user)
    return UserResponse(
        data=ResponseData(
            message=["User Created Successfully"],
            error_message=[]
        ),
        status_code=200
    )

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
    
    # Update fields
    await User.filter(id=user_id).update(**user.dict(exclude_unset=True))
    
    # Re-fetch updated user
    updated_user_obj = await User.filter(id=user_id).first()
    return await UserInDB.from_tortoise_orm(updated_user_obj)

@router.delete("/users/{user_id}", response_model=UserInDB)
async def delete_user(user_id: int):
    user_obj = await User.filter(id=user_id).first()
    if user_obj is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete user
    await User.filter(id=user_id).delete()
    
    # Return the deleted user object
    return await UserInDB.from_tortoise_orm(user_obj)
