from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from model.user_model import UserAuth, UserPreferences
from model.meal_model import MealsParams
from model.ml.ml_model import recommend_meal_plan
from service.config import auth
from service.database_manager import *
from typing import List
from os import environ as env
import re

app = FastAPI()
security = HTTPBearer()


def is_email_valid(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if (re.fullmatch(email_regex, email)):
        return True
    return False


@app.get("/")
def index():
    return {"greetings": "Hi! Welcome to KostKater Back-End App"}


@app.get("/check")
async def check_environment():
    try:
        user_list = read_users_collection()
        return {"env": f"This is in {env['ENV']} environment", "userList": user_list}
    except Exception as error:
        return {
            "error": True,
            "message": ("An error occurred:", str(error))
        }


@app.post("/login")
async def login(userAuth: UserAuth):
    try:
        if not is_email_valid(userAuth.email):
            return {
                "error": True,
                "message": "Format email tidak valid"
            }
        user = auth.sign_in_with_email_and_password(
            userAuth.email, userAuth.password)
        return {"error": False,
                "message": "Login berhasil!",
                "userInfo": {
                    "email": user["email"],
                    "token": user["idToken"]
                }}
    except:
        return {
            "error": True,
            "message": "Email atau password tidak sesuai"
        }


@app.post("/register")
async def register(userAuth: UserAuth):
    try:
        if not is_email_valid(userAuth.email):
            return {
                "error": True,
                "message": "Format email tidak valid"
            }
        user = auth.create_user_with_email_and_password(
            userAuth.email, userAuth.password)
        add_user_doc(userAuth.email)
        return {"message": "Registrasi berhasil!",
                "userInfo": {
                    "email": user["email"],
                    "token": user["idToken"]
                }}
    except:
        return {
            "error": True,
            "message": "Proses registrasi gagal, email sudah digunakan"
        }


@app.get("/user/data")
async def get_user_data(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        user = auth.get_account_info(token)
        email = user["users"][0]["email"]
        user_data = read_user_doc(email)
        return {"data": user_data}
    except Exception as error:
        return {
            "error": True,
            "message": ("An error occurred:", str(error))
        }


@app.post("/user/data")
async def update_user_data(userPreferences: UserPreferences, credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        user = auth.get_account_info(token)
        email = user["users"][0]["email"]
        update_user_doc(email, userPreferences.eat_halal,
                        userPreferences.allergies)
        user_data = read_user_doc(email)
        return {"data": user_data}
    except Exception as error:
        return {
            "error": True,
            "message": ("An error occurred:", str(error))
        }


@app.get("/meals/recommend")
async def get_meals_recommend(
        ingredients: List[str] = Query(
        default=[], description="List of ingredients"),
        allergies: List[str] = Query(
        default=[], description="List of allergies"),
        is_halal: bool = Query(
        default=True, description="Is halal"),
        price_min: int = Query(
        default=0, description="Minimum price"),
        price_max: int = Query(default=999999999, description="Maximum price"),
        credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        if is_halal:
            is_halal = '1'
        else:
            is_halal = '0'
        allergies = ",".join(allergies)

        meals_data = recommend_meal_plan(
            ingredients, allergies, is_halal, price_min, price_max, ingredients)

        return {"data": meals_data}
    except Exception as error:
        return {
            "error": True,
            "message": ("An error occurred:", str(error))
        }
