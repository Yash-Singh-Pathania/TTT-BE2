# app/core/__init__.py

# Import enums
from .enums import UserRole

# Import utility functions or classes
# from .utils import some_utility_function
# from .logger import configure_logging

# Example: Export items to be available at the package level
__all__ = [
    "UserRole",
    "settings",
    # "some_utility_function",
    # "configure_logging",
]
