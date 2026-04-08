from datetime import datetime
from typing import Annotated

from fastapi import Response, Cookie, FastAPI, status, Header
from pydantic import BaseModel

app = FastAPI()

fake_db = [
    {"title": "Criando uma aplicação com Django", "date": datetime.now(), "published": True},
    {"title": "Intercionalizando uma app FastAPI", "date": datetime.now(), "published": True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(), "published": False},
    {"title": "Criando uma aplicação com Starlette", "date": datetime.now(), "published": True}
]

@app.get("/posts")
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
    return { "posts": [post for post in fake_db[skip: skip + limit] if post["published"] is published] 
            
        # posts = []

        # for post in fake_db:
        #     if len(posts) == limit:
        #         break
        #     if post["published"] is published:
        #         posts.append(post)
        
        # return posts
    }
# Argumentos obrigátorios devem vir antes dos opcionais, caso contrário, o FastAPI não conseguirá identificar os parâmetros corretamente e retornará um erro.
# posts?published=on -> posts?published=true
# posts?published=off -> posts?published=false


@app.get("/posts/{framework}")
def read_posts(framework: str):
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "date": datetime.now()},
            {"title": f"Intercionalizando uma app {framework}", "date": datetime.now()}
            ]
    }

class Post(BaseModel):
    title: str
    date: datetime = datetime.now()
    published: bool = False
    author: str

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post