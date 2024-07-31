# app/schemas/user.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    SUPER_ADMIN = "super_admin"
    ORG_HEAD = "org_head"
    PLAYER = "player"

class UserBase(BaseModel):
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    email: EmailStr
    username: str = Field(..., max_length=20)
    hashed_password: str = Field(..., max_length=255)
    role: UserRole
    organization_id: int

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    deleted_at: Optional[datetime] = None
    is_deleted: Optional[bool] = False

class UserInDB(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    is_deleted: bool

    class Config:
        orm_mode = True

class UserOut(UserInDB):
    pass
