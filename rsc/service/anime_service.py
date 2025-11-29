from ..repository.anime_repository import RepositoryAnime
from datetime import date

class ServiceAnime:
    def __init__(self, repository_anime: RepositoryAnime) -> None:
        self.repository_anime = repository_anime

    def __valida_existencia_anime(self, id: int) -> None:
        if self.repository_anime.busca_anime_by_id(id=id) is None:
            raise Exception('Anime não encontrado.')

    def __valida_id_nulo_inteiro(self, id: int) -> None:
        if id is None:
            raise ValueError("ID não informado.")

        if not isinstance(id, int):
            raise Exception('ID Precisa ser um numero inteiro!!')

    def __identifica_campos_anime(self, dict_columns: dict) -> dict:
        return {
            key: value for key, value in dict_columns.items()
        }

    def __valida_criacao_anime(self, dict_anime: dict):
        pass

    def busca_anime_by_id(self, id: int) -> dict:
        try:
            self.__valida_id_nulo_inteiro(id=id)
            self.__valida_existencia_anime(id=id)
            anime_model = self.repository_anime.busca_anime_by_id(id=id)
            return {"sucess": True, "type": "Anime", "Info": anime_model}

        except Exception as error:
            return {"sucess": False, "message": str(error)}

    def busca_all_animes(self) -> dict:
        try:
            all_anime_model = self.repository_anime.busca_all_animes()
            return {"sucess": True, "type": "Anime", "Info": all_anime_model}
        except Exception as error:
            return {"sucess": False, "message": str(error)}

    def deleta_anime(self, id: int) -> dict:
        try:
            self.__valida_id_nulo_inteiro(id=id)
            self.__valida_existencia_anime(id=id)
            self.repository_anime.deleta_anime(id=id)
            return {"sucess": True, "type": "Anime", "Info": "anime deletado."}
        except Exception as error:
            return {"sucess": False, "message": str(error)}

    def atualiza_anime(self,
                       dict_Anime_model: dict) -> dict:
        try:
            dict_Anime_model = self.__identifica_campos_anime(
                dict_columns=dict_Anime_model
            )
            self.__valida_id_nulo_inteiro(id=dict_Anime_model.get('id'))
            self.__valida_existencia_anime(id=dict_Anime_model.get('id'))

            self.repository_anime.atualiza_anime(
                dict_Anime_model=dict_Anime_model
            )

            return {"sucess": True, "type": "Anime", "Info": "Anime editado"}
        except Exception as error:
            return {"sucess": False, "message": str(error)}

    def cria_anime(self,
                   nome: str,
                   data_lancamento: date,
                   descricao: str,
                   ) -> dict:
        pass

if __name__ == "__main__":
    from db.database import ConexaoDB

    con_db = ConexaoDB().session()
    myrepo = RepositoryAnime(con_db)
    service = ServiceAnime(repository_anime=myrepo)

    print(service.busca_anime_by_id(id=1))
    # print(myrepo.busca_all_animes())
    # service.deleta_anime(10)
    # service.atualiza_anime({'id': 1, 'nome': 'Fullmetal Alchemist'})
    # print(myrepo.busca_all_animes())
