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
async def root(service: ServiceAnime = Depends(myservice)) -> dict:
    # Todos os animes em formato de dicionario
    try:
        response = service.busca_all_animes()
        return response
    except Exception as error:
        print(error)


@router.get("/id={id_anime}")
async def litar_anime(id_anime: int,
                      service: ServiceAnime = Depends(myservice)) -> dict:
    # Anime em formato de dicionario
    try:
        response = service.busca_anime_by_id(id=id_anime)
        return response
    except Exception as error:
        print(error)


if __name__ == '__main__':
    conn = ConexaoDB().mysession()
    print(type(conn))
    repo = RepositoryAnime(conn)
    service = ServiceAnime(repository_anime=repo)

    print(service.busca_anime_by_id(1))
