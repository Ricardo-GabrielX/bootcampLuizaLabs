import pytest_asyncio
from fastapi import status
from httpx import AsyncClient

@pytest_asyncio.fixture(autouse=True)
async def populate_post(db):
    from src.schemas.post import PostIn
    from src.services.post import PostService

    service = PostService()
    await service.create(PostIn(title="Post 1", content="Content 1", published=True))
    await service.create(PostIn(title="Post 2", content="Content 2", published=True))
    await service.create(PostIn(title="Post 3", content="Content 3", published=False))

async def test_read_post_success(client: AsyncClient, access_token: str):
    # Given
    post_id = 1
    headers = {"Authorization": f"Bearer {access_token}"}

    # When
    response = await client.get(f"/posts/{post_id}", headers=headers)

    # Then
    content = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert content["id"] == post_id

async def test_read_post_not_found_fail(client: AsyncClient, access_token: str):
    # Given
    post_id = 999
    headers = {"Authorization": f"Bearer {access_token}"}

    # When
    response = await client.get(f"/posts/{post_id}", headers=headers)

    # Then
    assert response.status_code == status.HTTP_404_NOT_FOUND