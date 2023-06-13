from typing import List
from pydantic import BaseModel


class MealsParams(BaseModel):
    ingredients: List[str] = []
    allergies: List[str] = []
    is_halal: bool = True
    price_max: int = 999999999
    price_min: int = 0
