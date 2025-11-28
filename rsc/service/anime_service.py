from ..repository.anime_repository import RepositoryAnime
from ..model.anime_model import AnimeModel


class ServiceAnime:
    def __init__(self, repository_anime: RepositoryAnime) -> None:
        self.repository_anime = repository_anime

    def busca_anime_by_id(self, id: int) -> AnimeModel:
        if id is None:
            raise ValueError("ID do anime não pode ser None")

        if not isinstance(id, int):
            raise Exception('ID deve ser uma valor inteiro!!')

        return self.repository_anime.busca_anime_by_id(id=id)

    def busca_all_animes(self) -> AnimeModel:
        return self.repository_anime.busca_all_animes()

    def deleta_anime(self, id: int) -> None:
        vanime = self.busca_anime_by_id(id=id)
        if vanime is None:
            print('Anime não encontrato')
            raise Exception('Esse anime não existe!!')

        self.repository_anime.deleta_anime(id=id)

    def atualiza_anime(self,
                       dict_Anime_model: dict) -> None:
        vanime = self.busca_anime_by_id(id=dict_Anime_model.get('id', None))
        if vanime is None:
            print('Anime não encontrato')
            raise Exception('Esse anime não existe!!')

        dict_atualizar = {
            key: value for key, value in dict_Anime_model.items()
        }

        self.repository_anime.atualiza_anime(dict_Anime_model=dict_atualizar)

    def cria_anime(self):
        pass


if __name__ == "__main__":
    from db.database import ConexaoDB

    con_db = ConexaoDB().session()
    myrepo = RepositoryAnime(con_db)
    service = ServiceAnime(repository_anime=myrepo)

    print(myrepo.busca_anime_by_id(1))
    # print(myrepo.busca_all_animes())
    service.deleta_anime(10)
    service.atualiza_anime({'id': 1,
                            'nome': 'Fullmetal Alchemist'})
    # print(myrepo.busca_all_animes())
