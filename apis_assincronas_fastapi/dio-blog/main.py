from contextlib import asynccontextmanager

import databases
import sqlalchemy as sa
from fastapi import FastAPI
from controllers import post

DATABASE_URL = "sqlite:///./blog.sqlite"

database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()
engine = sa.create_engine(DATABASE_URL, connect_args= {"check_same_thread": False})



@asynccontextmanager
async def lifespan(app: FastAPI):
    from models import post
    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)




