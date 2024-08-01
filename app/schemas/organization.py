from pydantic import BaseModel
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models.organizations import Organization

class OrganizationCreate(BaseModel):
    name: str

class OrganizationInDB(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

OrganizationInDB = pydantic_model_creator(Organization, name="OrganizationInDB", include=("id", "name", "created_at", "updated_at"))
