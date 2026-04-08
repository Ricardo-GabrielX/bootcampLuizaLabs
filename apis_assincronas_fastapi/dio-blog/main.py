
from fastapi import FastAPI

from controllers import post

app = FastAPI()
app.include_router(post.router)


# class Foo(BaseModel):
#     bar: str
#     message: str


# @app.get("/foobar", response_model=Foo)
# def read_foobar():
#     return {"bar": "foo", "message" : "Hello, World!"}

