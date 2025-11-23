from ..repository.anime_repository import RepositoryAnime


class ServiceAnime:
    def __init__(self, repository_anime: RepositoryAnime) -> None:
        self.repository_anime = repository_anime

    def busca_anime_by_id(self, id: int) -> list:
        return self.repository_anime.busca_anime_by_id(id=id)

    def busca_all_animes(self) -> list:
        return self.repository_anime.busca_all_animes()


    def deleta_anime(self, id: int) -> None:
        return self.repository_anime.deleta_anime(id=id)


if __name__ == "__main__":
    from db.database import ConexaoDB

    con_db = ConexaoDB().session()
    myrepo = RepositoryAnime(con_db)
    service = ServiceAnime(repository_anime=myrepo)

    print(myrepo.busca_anime_by_id(1))
    service.deleta_anime(13)
    # print(myrepo.busca_all_animes())
