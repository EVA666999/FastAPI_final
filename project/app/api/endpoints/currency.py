
from fastapi import APIRouter, HTTPException
from app.api.endpoints.users import get_user_from_token
from app.api.models.user import User
from ..models.currency import Curency1, Curency2, Curency
from app.core.security import *
from app.api.models.user import User

import requests

curency_app = APIRouter()


@curency_app.post("/currency/exchange")
def get_currency_data(curency: Curency, user: User = Depends(get_user_from_token)):
    keys = get_keys()
    if user is None:
        raise HTTPException(status_code=401, detail="Требуется аутентификация")
    elif curency.source not in keys or curency.currency not in keys:
        print(curency.source, curency.currency)
        raise HTTPException(status_code=402, detail="Вы предоставили один или несколько недействительных кодов валюты.")
    else:
        url = f"https://api.apilayer.com/currency_data/live?source={curency.source}&currencies={curency.currency}"
        headers = {
            "apikey": "hEERwmcHb9fG5JuTbQY6bANWKrhRP4WB"
        }
        response = requests.get(url, headers=headers)
        return response.json()
    
@curency_app.get('/curency/keys')
def get_keys():
    url = "https://api.apilayer.com/currency_data/list"
    headers = { 
        "apikey": "hEERwmcHb9fG5JuTbQY6bANWKrhRP4WB"
    }
    response = requests.get(url, headers=headers)
    currency_data = response.json()
    keys = list(currency_data["currencies"].keys())
    return keys

@curency_app.get('/currency/list/')
def get_list():
    url = "https://api.apilayer.com/currency_data/list"
    headers = {
        "apikey": "hEERwmcHb9fG5JuTbQY6bANWKrhRP4WB"
    }
    response = requests.get(url, headers=headers)
    return response.json()

