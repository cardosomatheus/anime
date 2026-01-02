from fastapi import APIRouter, status
# Depends,  HTTPException
from anime.dto.usuario_dto import UsuarioDtoOut, UsuarioDtoIn

router = APIRouter(prefix='/v1/usuario', tags=['usuarios'])


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED
)
def cria_usuario(usuario: UsuarioDtoIn) -> UsuarioDtoOut:
    print(usuario)
    return usuario
