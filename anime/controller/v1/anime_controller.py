from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus

from anime.controller.home import myservice, ServiceAnime
from anime.exception.anime_exception import AnimeException
from anime.schemas.anime_schema import (
    AnimeSchema,
    AnimeSchemaUpdate,
    ListAnimeSchema
)


router = APIRouter(prefix="/v1/animes", tags=["Animes"])


@router.get(
    path="/",
    response_model=ListAnimeSchema,
    status_code=HTTPStatus.OK
)
def lista_all_animes(
    service: ServiceAnime = Depends(myservice)
) -> ListAnimeSchema:
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
    response_model=AnimeSchema,
    status_code=HTTPStatus.OK
)
def listar_anime_by_id(
    id_anime: int,
    service: ServiceAnime = Depends(myservice)
) -> AnimeSchema:
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
    status_code=HTTPStatus.OK
)
def deleta_anime_by_id(id: int,
                       service: ServiceAnime = Depends(myservice)) -> dict:
    # Exclusão de anime pelo ID
    try:
        response = service.deleta_anime(id=id)
        return response

    except AnimeException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        print(str(error))


@router.put("/id={id}", status_code=HTTPStatus.OK)
def editar_anime_by_id(
    id: int,
    anime: AnimeSchemaUpdate,
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


if __name__ == '__main__':
    editar_anime_by_id(2, "{ 'nome': 'mpss', 'data_lancamento': '2025-12-26'}")
    # deleta_anime_by_id(9, myservice())
    # print(listar_anime_by_id(11, myservice()))
