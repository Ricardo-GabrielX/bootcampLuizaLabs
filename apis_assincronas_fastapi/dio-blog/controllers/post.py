from fastapi import APIRouter, status
from schemas.post import PostIn, PostUpdateIn
from views.post import PostOut
from services.post import PostService

router = APIRouter(prefix="/posts")
service = PostService()


# LISTAR TODOS 
@router.get("/", response_model=list[PostOut])
async def read_posts(published: bool = True, limit: int = 10, skip: int = 0):
    return await service.read_all(published, limit, skip)


# CRIAR POST
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    last_id = await service.create(post)
    return {**post.model_dump(), "id": last_id}


# LER POST POR ID
@router.get("/{id}", response_model=PostOut)
async def read_post(id: int):
    return await service.read(id)


# ATUALIZAR POST
@router.put("/{id}", response_model=PostOut)
async def update_post(id: int, post: PostUpdateIn):
    return await service.update(id, post)


# DELETAR POST  
@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_post(id: int):
    await service.delete(id)
    return {"mensagem": f"Post de id {id} deletado com sucesso!"}