from typing import List
from pydantic import BaseModel


class UserAuth(BaseModel):
    email: str
    password: str


class UserPreferences(BaseModel):
    eat_halal: bool = True
    allergies: List[str] = []
