from pydantic import BaseModel
from typing import List, Any

class ResponseData(BaseModel):
    message: List[Any] = []
    error_message: List[str] = []

class ResponseBase(BaseModel):
    data: ResponseData
    status_code: int