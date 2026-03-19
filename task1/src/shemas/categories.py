from pydantic import BaseModel, Field

class Category(BaseModel):
    title: str = Field(max_length=256, min_length=3)
    description: str = Field(min_length=5)
    slug = Field(min_length=1)