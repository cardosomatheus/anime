from fastapi import FastAPI
from anime.controller.v1 import (
    anime_controller,
    token_controller,
    usuario_controller
)

app = FastAPI()

app.include_router(anime_controller.router)
app.include_router(usuario_controller.router)
app.include_router(token_controller.router)
