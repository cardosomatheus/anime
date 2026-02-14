import jwt
from typing import Annotated
from pwdlib import PasswordHash
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from anime.dto.token_dto import TokenDtoOut
from anime.dto.usuario_dto import UsuarioValidaTokenDtoOut
from datetime import timedelta, datetime, timezone

from anime.db.database import ConexaoDB
from anime.repository.usuario_repository import UsuarioRepository
from anime.service.usuario_service import UsuarioService
from dotenv import load_dotenv
import os


# Carrega variaveis via .env
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def myservice():
    session = ConexaoDB().mysession()
    repo = UsuarioRepository(session=session)
    service = UsuarioService(repository=repo)
    return service


# Configura a rota e padrão hash da senha
ppassword_hash = PasswordHash.recommended()
router = APIRouter(prefix='/v1/token', tags=['token'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    # Faz a busca do usuario e valida seu token
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise credentials_exception

        return payload
    except Exception:
        raise credentials_exception


def create_access_token(username: str, expires_delta: timedelta | None = None):
    # Cria o token de acesso com o tempo de expiração informado.
    # Retorna um TokenDtoOut com o token gerado e seu type bearer
    if expires_delta is None:
        expires_delta = ACCESS_TOKEN_EXPIRE_MINUTES

    expire = datetime.now(timezone.utc) + expires_delta
    vaccess_token = jwt.encode(
        payload={"sub": username, "exp": expire},
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

    return TokenDtoOut(access_token=vaccess_token, token_type="bearer")


def autenticate_user(username: str, passoword: str):
    # Faz a autenticacao da senha e a senha hash salva no banco
    dto = UsuarioValidaTokenDtoOut(
        username=username,
        password_hash=None
    )
    service = myservice()
    dto = service._busca_usuario_by_nome(dto=dto)

    if not dto:
        return False

    if not ppassword_hash.verify(passoword, dto.password_hash):
        return False

    return True


@router.post("/")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> TokenDtoOut:
    credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario ou senha inconrreta",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not autenticate_user(form_data.username, form_data.password):
        raise credentials_exception

    return create_access_token(
        username=form_data.username,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )


if __name__ == '__main__':
    print(ppassword_hash.hash('minhasenha123'))