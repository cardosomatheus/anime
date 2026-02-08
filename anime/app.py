from fastapi import FastAPI, Depends
from anime.controller.v1.token_controller import get_current_user
from anime.controller.v1 import (
    anime_controller,
    token_controller,
    usuario_controller,
    categoria_anime_controller
)

app = FastAPI()

app.include_router(token_controller.router)

app.include_router(
    router=anime_controller.router,
    dependencies=[Depends(get_current_user)]
)

app.include_router(
    router=usuario_controller.router,
    dependencies=[Depends(get_current_user)]
)

app.include_router(
    router=categoria_anime_controller.router,
    dependencies=[Depends(get_current_user)]
)
