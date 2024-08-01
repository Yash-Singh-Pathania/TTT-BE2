from app.models.user import User
from app.models.organizations import Organization
from app.schemas.user import UserCreate
from app.services.user.validations import UserValidations
from passlib.context import CryptContext

# Initialize the password context for hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreator:
    @staticmethod
    async def create_user(user_create: UserCreate):
        # Validate uniqueness of email and username
        await UserValidations.validate_create(user_create.email, user_create.username)

        # Pre-process user data
        hashed_password = pwd_context.hash(user_create.password)

        # Handle organization creation
        organization_id = user_create.organization_id
        if not organization_id:
            if user_create.organization_name:
                organization = await Organization.filter(name=user_create.organization_name).first()
                if not organization:
                    organization = await Organization.create(name=user_create.organization_name)
                organization_id = organization.id
            else:
                raise ValueError("Organization ID or Organization Name must be provided")

        # Create a user in the database
        user_obj = await User.create(
            first_name=user_create.first_name,
            last_name=user_create.last_name,
            email=user_create.email,
            username=user_create.username,
            hashed_password=hashed_password,
            role=user_create.role,
            organization_id=organization_id
        )
        return user_obj
