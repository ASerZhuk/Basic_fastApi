from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from routes.api import router as api_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    load_dotenv()
    yield


app = FastAPI(title="SleepCalculate API", lifespan=lifespan)
app.include_router(api_router)

