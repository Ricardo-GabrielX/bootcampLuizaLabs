from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get("/posts/{framework}")
def read_posts(framework: str):
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "date": datetime.now()},
            {"title": f"Intercionalizando uma app {framework}", "date": datetime.now()}
            ]
    }