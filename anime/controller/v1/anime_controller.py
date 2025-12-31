from fastapi import APIRouter, Depends, HTTPException, status
from anime.controller.home import myservice, ServiceAnime
from anime.exception.anime_exception import AnimeException
from anime.dto.anime_dto import (
    AnimeDtoIn,
    AnimeDtoOut,
    ListAnimeDtoOut
)


router = APIRouter(prefix="/v1/animes", tags=["Animes"])


@router.get(
    path="/",
    response_model=ListAnimeDtoOut,
    status_code=status.HTTP_200_OK
)
def lista_all_animes(
    service: ServiceAnime = Depends(myservice)
) -> ListAnimeDtoOut:
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
    response_model=AnimeDtoOut,
    status_code=status.HTTP_200_OK
)
def lista_anime_by_id(
    id_anime: int,
    service: ServiceAnime = Depends(myservice),
) -> AnimeDtoOut:
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
    status_code=status.HTTP_200_OK
)
def deleta_anime_by_id(id: int,
                       service: ServiceAnime = Depends(myservice)) -> None:
    # Exclusão de anime pelo ID
    try:
        response = service.deleta_anime(id=id)
        return response
    except AnimeException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        print(str(error))


@router.put("/id={id}", status_code=status.HTTP_200_OK)
def atualiza_anime_by_id(
    id: int,
    anime: AnimeDtoIn,
    service: ServiceAnime = Depends(myservice)
) -> None:
    # Edição de anime.
    try:
        vdto = AnimeDtoOut(id=id, **anime.model_dump())
        response = service.atualiza_anime(dto=vdto)
        return response

    except AnimeException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        print(str(error))


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED
)
def cria_anime(
    anime: AnimeDtoIn,
    service: ServiceAnime = Depends(myservice)
) -> dict:
    # Criação de anime.
    try:
        response = service.cria_anime(dto=anime)
        return response
    except AnimeException as error:
        raise HTTPException(status_code=error.status_code, detail=str(error))

    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


if __name__ == "__main__":
    from datetime import date
    animes = AnimeDtoIn(
      nome="string",
      data_lancamento=date(year=2020, month=5, day=10),
      descricao='string'
    )

    cria_anime(anime=animes, service=myservice())
