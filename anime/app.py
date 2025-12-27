from fastapi import FastAPI
from anime.controller.v1 import anime_controller
from anime.controller.v1 import user_controller

app = FastAPI()

app.include_router(anime_controller.router)
app.include_router(user_controller.router)