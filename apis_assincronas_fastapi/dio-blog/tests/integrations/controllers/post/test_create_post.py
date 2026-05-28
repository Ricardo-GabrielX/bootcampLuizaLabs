from fastapi import status
from httpx import AsyncClient


async def test_create_post_success(client: AsyncClient, access_token: str):
    #Todos seguind a estrutura Given, When, Then para facilitar a leitura e entendimento do teste

    # Given
    data = {
        "title": "My first post",
        "content": "This is the content of my first post",
        "published_at": "2024-06-01T00:00:00Z",
        "published": True
    }
    headers = {"Authorization": f"Bearer {access_token}"}

    # When
    response = await client.post("/posts/", json=data, headers=headers)

    # Then
    content = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert content["id"] is not None

async def test_create_post_invalid_payload_fail(client: AsyncClient, access_token: str):
    # Given
    data = {
        "title": "My first post",
        "content": "This is the content of my first post",
        "published_at": "2024-06-01T00:00:00Z",
        "published": True
    }
    headers = {"Authorization": f"Bearer {access_token}"}

    # When
    response = await client.post("/posts/", json=data, headers=headers)

    # Then
    content = response.json()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert content["detail"][0]["loc"] == ["body", "title"]

async def test_create_post_unauthorized_fail(client: AsyncClient):
    # Given
    data = {
        "title": "My first post",
        "content": "This is the content of my first post",
        "published_at": "2024-06-01T00:00:00Z",
        "published": True
    }

    # When
    response = await client.post("/posts/", json=data, headers={})

    # Then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED