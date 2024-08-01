from fastapi import APIRouter, HTTPException
from typing import List
from app.models.organizations import Organization
from app.schemas.organization import OrganizationInDB

router = APIRouter()

@router.get("/{name_like}", response_model=List[OrganizationInDB])
async def read_organization(name_like: str):
    organization_objs = await Organization.filter(name__icontains=name_like).all()
    if not organization_objs:
        return {}
    return [OrganizationInDB.from_orm(org) for org in organization_objs]
