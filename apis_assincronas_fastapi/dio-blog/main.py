from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {"title": "Criando uma aplicação com Django", "date": datetime.now(), "published": True},
    {"title": "Intercionalizando uma app FastAPI", "date": datetime.now(), "published": True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(), "published": False},
    {"title": "Criando uma aplicação com Starlette", "date": datetime.now(), "published": True}
]

@app.get("/posts")
def read_posts(published: bool, skip: int = 0, limit: int = len(fake_db)):
    return { "posts": [post for post in fake_db[skip: skip + limit] if post["published"] is published] }
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