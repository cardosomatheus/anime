from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    disable: bool | None = None


class UserSchemaIn(UserSchema):
    hashed_password: str
