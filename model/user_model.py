from typing import List
from pydantic import BaseModel


class UserAuth(BaseModel):
    email: str
    password: str


class UserPreferences(BaseModel):
    eat_halal: bool = True
    allergies: List[str] = []
    ingredients: List[str] = []
    price_max: int = 999999999
    price_min: int = 0
