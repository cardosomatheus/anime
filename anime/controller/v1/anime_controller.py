from anime.db.database import ConexaoDB
from anime.repository.anime_repository import RepositoryAnime
from anime.service.anime_service import ServiceAnime
from anime.service.anime_service import AnimeIdInvalidoError
from anime.service.anime_service import AnimeIdNuloError
from anime.service.anime_service import AnimeNaoEncontrado
from anime.schemas.anime_schema import AnimeSchema, ListAnimeSchema
from anime.schemas.anime_schema import AnimeSchemaUpdate
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from http import HTTPStatus

router = APIRouter(prefix="/v1/animes", tags=["Animes"])


def myservice() -> ServiceAnime:
    session = ConexaoDB().mysession()
    repo = RepositoryAnime(session=session)
    service = ServiceAnime(repository_anime=repo)
    return service


@router.get(
    path="/",
    response_model=ListAnimeSchema,
    status_code=HTTPStatus.OK
)
def lista_all_animes(service: ServiceAnime = Depends(myservice)) -> dict:
    # Todos os animes em formato de Json
    try:
        response = service.busca_all_animes()
        return response
    except AnimeNaoEncontrado as error:
        raise HTTPException(status_code=404, detail=str(error))

    except AnimeIdInvalidoError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except AnimeIdNuloError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except Exception as error:
        print(str(error))


@router.get(
    "/id={id_anime}",
    response_model=AnimeSchema,
    status_code=HTTPStatus.OK
)
def listar_anime_by_id(id_anime: int,
                       service: ServiceAnime = Depends(myservice)) -> dict:
    # Todos os animes em formato de Json
    try:
        response = service.busca_anime_by_id(id=id_anime)
        return response

    except AnimeNaoEncontrado as error:
        raise HTTPException(status_code=404, detail=str(error))

    except AnimeIdInvalidoError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except AnimeIdNuloError as error:
        raise HTTPException(status_code=400, detail=str(error))

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
    except AnimeNaoEncontrado as error:
        raise HTTPException(status_code=404, detail=str(error))

    except AnimeIdInvalidoError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except AnimeIdNuloError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except Exception as error:
        print(str(error))


@router.put(
    "/id={id}",
    status_code=HTTPStatus.OK
)
def editar_anime_by_id(
    id: int,
    anime: AnimeSchemaUpdate,
    service: ServiceAnime = Depends(myservice)
) -> None:
    # Edião de anime.
    try:
        service.atualiza_anime(dict_anime=jsonable_encoder(anime))
    except AnimeNaoEncontrado as error:
        raise HTTPException(status_code=404, detail=str(error))

    except AnimeIdInvalidoError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except AnimeIdNuloError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except Exception as error:
        print(str(error))


if __name__ == '__main__':
    deleta_anime_by_id(9, myservice())
    # print(listar_anime_by_id(11, myservice()))
