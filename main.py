from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from service import auth, db
from model.user_model import UserAuth

app = FastAPI()
security = HTTPBearer()


@app.get("/kostkater/")
def index():
    return {"greetings": "Hi! Welcome to KostKater Back-End App"}


@app.post("/kostkater/login")
async def login(userAuth: UserAuth):
    try:
        user = auth.sign_in_with_email_and_password(
            userAuth.email, userAuth.password)
        return {"message": "Login successful",
                "userInfo": {
                    "email": user["email"],
                    "token": user["idToken"]
                }}
    except:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@app.post("/kostkater/register")
async def register(userAuth: UserAuth):
    try:
        user = auth.create_user_with_email_and_password(
            userAuth.email, userAuth.password)
        return {"message": "Registration successful",
                "userInfo": {
                    "email": user["email"],
                    "token": user["idToken"]
                }}
    except:
        raise HTTPException(status_code=400, detail="Registration failed")


@app.get("/kostkater/user/profile")
async def get_user_email(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        user = auth.get_account_info(token)
        email = user["users"][0]["email"]
        return {"email": email}
    except:
        raise HTTPException(
            status_code=401, detail="Invalid or missing authentication token")
