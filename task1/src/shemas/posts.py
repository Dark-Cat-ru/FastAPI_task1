from pydantic import BaseModel, Field
from datetime import datetime
from shemas.users import User
from shemas.locations import Location
from shemas.categories import Category

class Post(BaseModel):
    title: str = Field(max_length=256, min_length=3)
    text: str = Field(min_length=5)
    pub_date: datetime
    author: User
    location: Location
    category: Category