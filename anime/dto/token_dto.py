from pydantic import BaseModel


# DTO de saida do TOKEN
class TokenDtoOut(BaseModel):
    access_token: str
    token_type: str
