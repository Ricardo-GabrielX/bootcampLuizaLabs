from fastapi import APIRouter, status
from sqlalchemy import values
from schemas.post import PostIn
from models.post import posts
from views.post import PostOut
from database import database

router = APIRouter(prefix="/posts")

@router.get("/", response_model=list[PostOut])
async def read_posts(published: bool, limit: int, skip: int = 0):
    query = posts.select()
    return await database.fetch_all(query)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    command = posts.insert().values(title=post.title, content=post.content, published=post.published, published_at=post.published_at)
    last_id = await database.execute(command)
    return {**post.model_dump(), "id" : last_id}





            
        
# Argumentos obrigátorios devem vir antes dos opcionais, caso contrário, o FastAPI não conseguirá identificar os parâmetros corretamente e retornará um erro.
# posts?published=on -> posts?published=true
# posts?published=off -> posts?published=false





