from fastapi import FastAPI
from source.controller.v1 import anime_controller

app = FastAPI()

app.include_router(
    anime_controller.router,
    prefix="/v1/animes", tags=["Animes"]
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger!"}
