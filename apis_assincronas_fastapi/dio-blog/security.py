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
    sub: int
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: srt

class JWTToken(BaseModel):
    access_token: AccessToken

def sign_jwt(user_id: int) -> JWTToken:
    now = time.time()
    payload = {
        "iss": "curso-fast.com.br",
        "sub": user_id,
        "aud": "curso-fastapi",
        "exp": now + (60 * 30),
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    return JWTToken(access_token=token)


async def decode_jwt(token: str) -> JWTToken | None:
    try:
        decoded_token = jwt.decode(token, SECRET, audience="curso-fastapi", algorithms=[ALGORITHM])
        _token =  JWTToken.model_validate({"access_token": decoded_token})
        return _token if _token.access_token.exp >= time.time() else None
    except Exception:
        return None






