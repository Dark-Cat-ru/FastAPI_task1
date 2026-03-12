from pydantic import BaseModel, SecretStr, Field

class User(BaseModel):
    login: str = Field(max_length=12, min_length=5)
    password: SecretStr = Field(min_length=8)