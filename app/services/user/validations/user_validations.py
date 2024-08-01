from app.models.user import User
from fastapi import HTTPException

class UserValidations:
    @staticmethod
    async def validate_create(email: str, username: str):
        # Check for existing user with the same email
        if await User.filter(email=email).exists():
            raise HTTPException(status_code=400, detail="Email already registered")
        
        if await User.filter(username=username).exists():
            raise HTTPException(status_code=400, detail="Username already taken")
