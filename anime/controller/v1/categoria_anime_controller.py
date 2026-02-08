from anime.dto.categoria_anime_dto import CategoriaAnimeDtoIn
from fastapi import APIRouter, Depends, HTTPException, status
from anime.db.database import ConexaoDB
from anime.repository.categoria_anime_repository import (
    CatergoriaAnimeRepository
)
from anime.service.catergoriaanime_service import CategoriaAnimeService


router = APIRouter(prefix='/v1/categoria', tags=['Categorias'])


def myservice() -> CategoriaAnimeService:
    session = ConexaoDB().mysession()
    repo = CatergoriaAnimeRepository(session=session)
    service = CategoriaAnimeService(repository=repo)
    return service


@router.get('/categorias', status_code=status.HTTP_200_OK)
def listar_categorias(service: CategoriaAnimeService = Depends(myservice)):
    try:
        return service.busca_all_categoria()

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@router.post(path='/categorizar_anime')
def adiciona_vinculo(
    body: CategoriaAnimeDtoIn,
    service: CategoriaAnimeService = Depends(myservice)
):
    try:
        return service.adiciona_vinculo(body)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error.args[0]
        )


@router.post(path='/descategorizar_anime')
def remove_vinculo(
    body: CategoriaAnimeDtoIn,
    service: CategoriaAnimeService = Depends(myservice)
):
    try:
        return service.remove_vinculo(body)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error.args[0]
        )
