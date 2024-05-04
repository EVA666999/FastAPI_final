from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

auth_app = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

@auth_app.get("/protected_resource")
def get_user_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        return user_id
    except jwt.ExpiredSignatureError:
        return {'message': 'токен истёк'}
    except jwt.InvalidTokenError:
        return {'message': 'неправильный токен'}