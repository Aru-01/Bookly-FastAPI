from pydantic import BaseModel, Field
import uuid
from datetime import datetime


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    password_hash: str = Field(exclude=True)
    first_name: str
    last_name: str
    is_verified: bool
    created_at: datetime
    update_at: datetime


class UserCreateModel(BaseModel):
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)
    first_name: str
    last_name: str
