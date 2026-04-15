from fastapi import APIRouter, FastAPI, Response, status
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")




@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    # fake_db.append(post.model_dump())
    return post

@router.get("/", response_model=list[PostOut])
def read_posts(
    response: Response,
    published: bool, 
    limit: int, 
    skip: int = 0
):
    return []
            
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





