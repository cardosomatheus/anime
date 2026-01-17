from fastapi import APIRouter, status, Depends, HTTPException
from anime.controller.home import myservice_usuario, UsuarioService
from anime.dto.usuario_dto import UsuarioDtoOut, UsuarioDtoIn
from anime.dto.token_dto import TokenDtoOut
from anime.exception.usuario_exception import UsuarioException
from anime.controller.v1.token_controller import login_for_access_token


router = APIRouter(prefix='/v1/usuario', tags=['usuarios'])


@router.post(path='/',  status_code=status.HTTP_201_CREATED)
def cria_usuario(
    usuario: UsuarioDtoIn,
    service: UsuarioService = Depends(myservice_usuario),
    token: TokenDtoOut = Depends(login_for_access_token)
) -> dict:
    # Criação de usuario.
    try:
        response = service.criar_usuario(dto=usuario)
        return response
    except UsuarioException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get(path='/{id}',
            response_model=UsuarioDtoOut,
            status_code=status.HTTP_200_OK)
def lista_usuario_by_id(
    id: int,
    service: UsuarioService = Depends(myservice_usuario),
    token: TokenDtoOut = Depends(login_for_access_token)
) -> UsuarioDtoOut:
    # Busca Usuario pelo ID
    try:
        return service.busca_usuario_by_id(id=id)
    except UsuarioException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        print(str(error))
