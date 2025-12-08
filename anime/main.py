from fastapi import FastAPI
from anime.controller.v1 import anime_controller

app = FastAPI()

app.include_router(
    anime_controller.router
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
