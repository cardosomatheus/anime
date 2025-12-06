from fastapi import APIRouter, Depends
from source.service.anime_service import ServiceAnime
from source.repository.anime_repository import RepositoryAnime
from db.database import ConexaoDB


router = APIRouter(prefix="/v1/animes", tags=["Animes"])


def myservice() -> ServiceAnime:
    conn = ConexaoDB()
    repo = RepositoryAnime(conn)
    service = ServiceAnime(repository_anime=repo)
    return service


@router.get("/")
async def root() -> dict:
    return {"message": "Hello word2"}


@router.get("/id={id_anime}")
async def litar_anime(id_anime: int,
                      service: ServiceAnime = Depends(myservice)) -> dict:
    try:
        response = service.busca_anime_by_id(id=id_anime)
        print('response controller', response)
        return response
    except Exception as error:
        print(f'Error ao tenar buscar o anime pelo ID {id_anime}!!\n')
        print(error)


