# app/models/organization.py

from tortoise import fields
from tortoise.models import Model

class Organization(Model):
    id = fields.IntField(pk=True, unique=True)
    name = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "organizations"

    def __repr__(self):
        return f"<Organization(id={self.id}, name={self.name})>"
