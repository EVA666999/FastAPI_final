from datetime import datetime, date
from typing import List, Optional, Union
from pydantic import EmailStr
from pydantic import Field

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Authorizate(BaseModel):
    username: str
    password: str
    session_token: str = None