from fastapi import APIRouter, status, HTTPException
from models.users import User
from models.cats import Cat

router = APIRouter()

user_repo = [
    {
        'login': 'cat', 
        'password': '666darkCat13!'
    },
    {
        'login': 'dog',
        'password': '13BadDog666!'
    },
]

@router.get("/cats", status_code=status.HTTP_200_OK)
async def get_cat_data(cat: Cat):
    response = {
        "name": cat.name,
        "color": cat.color,
        "birth_year": cat.birth_year,
        "owner": cat.owner.login
    }
    return response

@router.post("/create_user", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(new_user: User):
    if len(new_user.login) < 3:
        raise HTTPException(
            detail="Длина логина должна быть не меньше 3 символов",
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        )
    if any(user['login'] == new_user.login for user in user_repo):
        raise HTTPException(
            detail="Пользователь с таким логином уже есть",
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        )
    else:
        responce = {
            'login': new_user.login,
            'password': new_user.password,
        }
        return User.model_validate(obj=responce)

@router.put("/change_user/<user_login>", status_code=status.HTTP_200_OK, response_model=User)
async def change_user_data(user: User, user_login: str):
    if len(user.login) < 3:
        raise HTTPException(
            detail="Длина логина должна быть не меньше 3 символов",
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        )
    for i in user_repo:
        if i['login'] == user_login:
            responce = {
                "login": user.login,
                "password": user.password
            }
            return User.model_validate(obj=responce)
        raise HTTPException(
            detail="Не найден пользователь с таким login",
            status_code=status.HTTP_404_NOT_FOUND,
        )

@router.delete("/delete_user/<user_login>", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_login : int):
    if not any(user['login'] == user.login for user in user_repo):
        raise HTTPException(
            detail="Пользователя с таким id уже нет",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        for u in user_repo:
            if u["login"] == user_login:
                user_repo = user_repo.pop(user_login)
                return user_repo
