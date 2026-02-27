from pydantic import BaseModel, Field

from models.users import User

CHOICES = (
    ('Gray', 'Серый'),
    ('Black', 'Чёрный'),
    ('White', 'Белый'),
    ('Ginger', 'Рыжий'),
    ('Mixed', 'Смешанный'),
)

class Achievement(BaseModel):
    name: str = Field(max_length=64)

class Cat(BaseModel):
    name: str = Field(max_length=16)
    color: str = Field(max_length=16, choices=CHOICES)
    birth_year: int = Field()
    owner: User
    achievements: Achievement = Field(through='AchievementCat')

class AchievementCat(BaseModel):
    achivement: Achievement
    cat: Cat