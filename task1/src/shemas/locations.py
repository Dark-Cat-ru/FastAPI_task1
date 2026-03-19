from pydantic import BaseModel, Field

class Location(BaseModel):
    name: str = Field(max_length=256, min_length=3)