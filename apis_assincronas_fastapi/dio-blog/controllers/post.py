from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Cookie, Header, FastAPI, Response, status
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")

fake_db = [
    {"title": "Criando uma aplicação com Django", "date": datetime.now(), "published": True},
    {"title": "Intercionalizando uma app FastAPI", "date": datetime.now(), "published": True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(), "published": False},
    {"title": "Criando uma aplicação com Starlette", "date": datetime.now(), "published": True}
]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post

@router.get("/", response_model=list[PostOut])
def read_posts(
    response: Response,
    published: bool, 
    limit: int, 
    skip: int = 0, 
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None
):

    response.set_cookie(key="user", value="gabrieeltech@gmail.com")
    print(f"Cookie: {ads_id}")
    print(f"User-Agent: {user_agent}")
    tail = skip + limit
    return [post for post in fake_db[skip: tail] if post["published"] is published]
            
        # posts = []

        # for post in fake_db:
        #     if len(posts) == limit:
        #         break
        #     if post["published"] is published:
        #         posts.append(post)
        
        # return posts
# Argumentos obrigátorios devem vir antes dos opcionais, caso contrário, o FastAPI não conseguirá identificar os parâmetros corretamente e retornará um erro.
# posts?published=on -> posts?published=true
# posts?published=off -> posts?published=false


@router.get("/{framework}", response_model=PostOut)
def read_posts(framework: str):
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "date": datetime.now()},
            {"title": f"Intercionalizando uma app {framework}", "date": datetime.now()}
            ]
    }


