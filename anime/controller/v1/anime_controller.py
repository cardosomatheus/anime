from fastapi import APIRouter, Depends, HTTPException, status

from anime.controller.home import myservice, ServiceAnime
from anime.exception.anime_exception import AnimeException
from anime.schemas.anime_schema import (
    AnimeSchemaIn,
    AnimeSchemaOut,
    ListAnimeSchemaOut
)


router = APIRouter(prefix="/v1/animes", tags=["Animes"])


@router.get(
    path="/",
    response_model=ListAnimeSchemaOut,
    status_code=status.HTTP_200_OK
)
def lista_all_animes(
    service: ServiceAnime = Depends(myservice)
) -> ListAnimeSchemaOut:
    # Todos os animes em formato de Json
    try:
        response = service.busca_all_animes()
        return response

    except AnimeException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        print(str(error))


@router.get(
    "/id={id_anime}",
    response_model=AnimeSchemaOut,
    status_code=status.HTTP_200_OK
)
def lista_anime_by_id(
    id_anime: int,
    service: ServiceAnime = Depends(myservice),
) -> AnimeSchemaOut:
    # Todos os animes em formato de Json
    try:
        response = service.busca_anime_by_id(id=id_anime)
        return response

    except AnimeException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        print(str(error))


@router.delete(
    path="/id={id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deleta_anime_by_id(id: int,
                       service: ServiceAnime = Depends(myservice)) -> None:
    # Exclusão de anime pelo ID
    try:
        service.deleta_anime(id=id)

    except AnimeException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        print(str(error))


@router.put("/id={id}", status_code=status.HTTP_200_OK)
def atualiza_anime_by_id(
    id: int,
    anime: AnimeSchemaIn,
    service: ServiceAnime = Depends(myservice)
) -> None:
    # Edião de anime.
    try:
        vbody = {'id': id, **anime.model_dump()}
        service.atualiza_anime(dict_anime=vbody)
        return {'message': 'Atualizado com sucesso'}

    except AnimeException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        print(str(error))


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED
)
def cria_anime(
    anime: AnimeSchemaIn,
    service: ServiceAnime = Depends(myservice)
):
    # Criação de anime.
    try:
        service.cria_anime(dto=anime)
    except AnimeException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        print(str(error))

