# app/core/enums.py

from enum import Enum

class UserRole(str, Enum):
    SUPER_ADMIN = "super_admin"
    ORG_HEAD = "org_head"
    PLAYER = "player"
