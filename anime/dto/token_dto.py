from pydantic import BaseModel


class TokenDtoOut(BaseModel):
    access_token: str
    token_type: str
