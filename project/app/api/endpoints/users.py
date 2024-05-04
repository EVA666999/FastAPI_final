from fastapi import APIRouter, HTTPException
from app.api.models.user import User
from urllib.parse import unquote
from app.core.security import *
users_app = APIRouter()

users_db = []

@users_app.post('/auth/register/')
async def register_user(user: User):
    users_db.append(user.model_dump())
    return user


@auth_app.post('/auth/login/')
async def login(login_user: User):
    for db_user in users_db:
        user_dict = db_user
        if user_dict["username"] == login_user.username and user_dict["password"] == login_user.password:
            return {"access_token": create_jwt_token({"sub": login_user.username}), "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

def get_user(username: str):
    for user_data in users_db:
        if user_data["username"] == username:
            print("Found user:", user_data)  # Отладочное сообщение
            return User(**user_data)
    print("User not found for username:", username)  # Отладочное сообщение
    return None

@auth_app.get("/users/{username}", response_model=User)
async def get_item(username: str, current_user: str = Depends(get_user_from_token)):
    user_data = get_user(current_user)
    if username == user_data.username:
        return user_data
    raise HTTPException(status_code=404, detail="User not found")
