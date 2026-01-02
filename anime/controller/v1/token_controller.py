import jwt
from typing import Annotated
from pwdlib import PasswordHash
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from anime.dto.login_dto import TokenDtoOut
from datetime import timedelta, datetime, timezone

SECRET_KEY = "1bacd7fea1893fd493fa7059e7c29a6182cfecf81ad9748e6a93aea6a96a8314"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
my_db_user = {
    "matheus": {
        "username": "matheus",
        "password": "$argon2id$v=19$m=65536,t=3,p=4$ukifqXDBk7RAEpIQk1TdUw$VCah/R55h0uQ8Wt5o3wGt7/XDzCZ/NVd5B5/VJ2p5JU"
    }
}

password_hash = PasswordHash.recommended()
router = APIRouter(prefix='/v1/token', tags=['token'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def create_access_token(
    username: str,
    expires_delta: timedelta | None = timedelta(minutes=15)
):
    """Criação do token de acesso"""
    expire = datetime.now(timezone.utc) + expires_delta
    vaccess_token = jwt.encode(
        payload={"sub": username, "exp": expire},
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

    return TokenDtoOut(access_token=vaccess_token, token_type="bearer")


def autenticate_user(username: str, hash_password: str):
    """ Autenticacao do usurio e senha"""
    pass_user = my_db_user.get(username)
    if not pass_user:
        return False

    if not password_hash.verify(hash_password, pass_user.get('password')):
        return False

    return True


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> TokenDtoOut:
    if not autenticate_user(form_data.username, form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return create_access_token(
        username=form_data.username,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )


if __name__ == '__main__': 
    print('etn')
    print(my_db_user.get('matheus').get('password'))
    print(password_hash.verify(
        'mcds123',
        my_db_user.get('matheus').get('password')
    ))