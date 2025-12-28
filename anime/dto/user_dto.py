from pydantic import BaseModel


class UserDto(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    disabled: bool | None = None


class UserDtoIn(UserDto):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
