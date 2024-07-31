from tortoise.models import Model
from tortoise import fields
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    SUPER_ADMIN = "super_admin"
    ORG_HEAD = "org_head"
    PLAYER = "player"

class User(Model):
    id = fields.IntField(pk=True, unique=True)
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=30)
    email = fields.CharField(max_length=50, unique=True, index=True)
    username = fields.CharField(max_length=20, unique=True, index=True)
    hashed_password = fields.CharField(max_length=255)  # You can adjust the length based on the hash length
    role = fields.CharEnumField(UserRole)
    organization_id = fields.IntField(index=True)

    created_at = fields.DatetimeField(auto_now_add=True, null=False)
    updated_at = fields.DatetimeField(auto_now=True, null=True)
    deleted_at = fields.DatetimeField(null=True)
    is_deleted = fields.BooleanField(default=False, index=True)

    class Meta:
        table = "users"

    def __repr__(self):
        return (f"<User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, "
                f"email={self.email}, username={self.username}, role={self.role}, "
                f"organization_id={self.organization_id})>")
