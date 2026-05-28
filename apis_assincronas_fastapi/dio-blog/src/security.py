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
    


# Corrigir classe;
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> JWTToken | None:
        authorization = request.headers.get("Authorization", "")
        scheme, _, credentials = authorization.partition(" ")
        
        if credentials:
            if not scheme == "Bearer":
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication scheme.")
            payload = await decode_jwt(credentials)
            if not payload:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or expired token.")
            return payload
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authorization code.")
    
    def get_current_user(self, token: Annotated[JWTToken, Depends(JWTBearer())]) -> dict[str, int]:
        print(token)
        return {"user_id": token.access_token.sub}
    
    def login_required(self, token: Annotated[dict[str, int], Depends(get_current_user)]):
        if not current_user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acess denied.")
        return current_user


