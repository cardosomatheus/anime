from fastapi import FastAPI
from anime.controller.v1 import (
    anime_controller,
    token_controller,
    user_controller2
)

app = FastAPI()

app.include_router(anime_controller.router)
app.include_router(user_controller2.router)
app.include_router(token_controller.router)
