from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from anime.schemas.user_schema import UserSchema, UserSchemaIn

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


router = APIRouter(prefix='/v1/user', tags=['User'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/user/token")


def fake_hash_password(password: str):
    print("fakehashed" + password)
    return "fakehashed" + password


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserSchemaIn(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    print('ETAPA 5')
    user = fake_decode_token(token)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[UserSchema, Depends(get_current_user)],
):
    print('ETAPA 6')
    if current_user.disabled:
        print('ETAPA 7')
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    print('ETAPA 1')
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )
    print('ETAPA 2')
    user = UserSchemaIn(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    print('ETAPA 3')
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400, 
            detail="Incorrect username or password"
        )

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("me")
async def read_users_me(
    current_user: Annotated[UserSchema, Depends(get_current_active_user)],
):
    print('ETAPA 4')
    return current_user

if __name__ == "__main__":
    read_users_me()