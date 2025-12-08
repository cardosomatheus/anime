from fastapi import APIRouter, Depends
from anime.service.anime_service import ServiceAnime
from anime.repository.anime_repository import RepositoryAnime
from anime.db.database import ConexaoDB


router = APIRouter(prefix="/v1/animes", tags=["Animes"])


def myservice() -> ServiceAnime:
    session = ConexaoDB().mysession()
    repo = RepositoryAnime(session=session)
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

if __name__ == '__main__':
    conn = ConexaoDB().mysession()
    print(type(conn))
    repo = RepositoryAnime(conn)
    service = ServiceAnime(repository_anime=repo)

    print(service.busca_anime_by_id(1))
