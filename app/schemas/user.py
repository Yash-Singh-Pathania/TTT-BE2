from pydantic import BaseModel, EmailStr, root_validator, ValidationError , Field
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
    password: str = Field(..., max_length=255)
    role: UserRole
    organization: Optional[int] = None
    organization_name: Optional[str] = None 
    organization_id: Optional[int] = None

    @root_validator(pre=True)
    def check_organization(cls, values):
        organization_id = values.get('organization_id')
        organization_name = values.get('organization_name')

        if not organization_id and not organization_name:
            raise ValueError('Either organization_id or organization_name must be provided.')

        return values

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
