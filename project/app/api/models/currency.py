from datetime import datetime, date
from typing import List, Optional, Union
from pydantic import EmailStr
from pydantic import Field

from pydantic import BaseModel

class Curency1(BaseModel):
    source: str
    count: int | None = 1

class Curency2(BaseModel):
    source: str
    count: int | None = 1

class Curency(BaseModel):
    source: str
    currency: str