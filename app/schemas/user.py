from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.core.enums import UserRole

class UserBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=30, example="User")
    last_name: str = Field(..., min_length=2, max_length=30, example="Userson")
    username: str = Field(..., min_length=2, max_length=20, regex=r"^[a-z0-9]+$", example="userson")
    email: EmailStr = Field(..., example="user.userson@example.com")
    role: UserRole
    organization_id: int

class UserCreate(UserBase):
    hashed_password: str = Field(..., example="hashedpassword123")

class UserRead(UserBase):
    id: int
    profile_image_url: str = Field(default="https://www.profileimageurl.com")
    is_superuser: bool = False
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    is_deleted: bool

class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=2, max_length=30, example="User")
    last_name: Optional[str] = Field(None, min_length=2, max_length=30, example="Userberg")
    username: Optional[str] = Field(None, min_length=2, max_length=20, regex=r"^[a-z0-9]+$", example="userberg")
    email: Optional[EmailStr] = Field(None, example="user.userberg@example.com")
    profile_image_url: Optional[str] = Field(None, regex=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", example="https://www.profileimageurl.com")
    hashed_password: Optional[str] = None
    is_superuser: Optional[bool] = None
    deleted_at: Optional[datetime] = None
    is_deleted: Optional[bool] = None

class UserDelete(BaseModel):
    is_deleted: bool
    deleted_at: datetime

class UserRestoreDeleted(BaseModel):
    is_deleted: bool
