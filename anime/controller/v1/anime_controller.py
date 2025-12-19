from fastapi import APIRouter, Depends
from anime.service.anime_service import ServiceAnime
from anime.repository.anime_repository import RepositoryAnime
from anime.db.database import ConexaoDB
from anime.schemas.anime_schema import AnimeSchema, ListAnimeSchema


router = APIRouter(prefix="/v1/animes", tags=["Animes"])


def myservice() -> ServiceAnime:
    session = ConexaoDB().mysession()
    repo = RepositoryAnime(session=session)
    service = ServiceAnime(repository_anime=repo)
    return service


@router.get("/", response_model=ListAnimeSchema)
async def lista_all_animes(service: ServiceAnime = Depends(myservice)) -> dict:
    # Todos os animes em formato de dicionario
    try:
        response = service.busca_all_animes()
        response.root
        return response
    except Exception as error:
        print(error)


@router.get("/id={id_anime}", response_model=AnimeSchema)
def listar_anime_by_id(
    id_anime: int,
    service: ServiceAnime = Depends(myservice)
) -> dict:
    try:
        response = service.busca_anime_by_id(id=id_anime)
        return response

    except Exception as error:
        print(error)


@router.put("/excluir={id_anime}")
async def excluir_anime_by_id(
    id_anime: int,
    service: ServiceAnime = Depends(myservice)
) -> dict:
    # Exclusão de anime pelo ID
    try:
        response = service.deleta_anime(id=id_anime)
        return response
    except Exception as error:
        print(error)


@router.post("/editar")     # Como receber o Body?
async def editar_anime_by_id(
    service: ServiceAnime = Depends(myservice)
) -> dict:
    # Edião de anime.
    try:
        response = service.atualiza_anime()
        return response
    except Exception as error:
        print(error)


if __name__ == '__main__':
    conn = ConexaoDB().mysession()
    print(type(conn))
    repo = RepositoryAnime(conn)
    service = ServiceAnime(repository_anime=repo)

    print(service.busca_anime_by_id(1))
