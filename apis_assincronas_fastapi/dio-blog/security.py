import time
from typing import Annotated
from uuid import uuid4

import jwt
from fastapi import HTTPException, Depends, Request, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel

SECRET = "my_secret"
ALGORITHM = "HS256"


class access_token(BaseModel):
    iss: str
    sub: str
    aud: str
    exp: int




