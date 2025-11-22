from rsc.repository.anime_repository import RepositoryAnime
from db.database import ConexaoDB

myrepo = RepositoryAnime()
con_db = ConexaoDB()
print(myrepo.busca_anime_by_id(1, con_db))