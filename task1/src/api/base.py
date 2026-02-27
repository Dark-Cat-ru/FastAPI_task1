from fastapi import APIRouter, status, HTTPException
from models.users import User
from models.cats import Cat

router = APIRouter()

user_repo = [
    {
        'id': 0,
        'login': 'cat', 
        'password': '666darkCat13!'
    },
    {
        'id': 1,
        'login': 'dog',
        'password': '13BadDog666!'
    },
]

@router.get("cats/", status_code=status.HTTP_200_OK)
async def get_cat_data(cat: Cat):
    response = {
        "name": cat.name,
        "color": cat.color,
        "birth_year": cat.birth_year,
        "owner": cat.owner.login
    }
    return response

@router.post("change_user/<user_id>/", status_code=status.HTTP_200_OK, response_model=User)
async def change_user_data(user: User, user_id: int):
    if len(user.login) < 3:
        raise HTTPException(
            detail="Длина логина должна быть не меньше 3 символов",
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        )
    for i in user_repo:
        if i['login'] == user.login:
            responce = {
                'id': user_id,
                "login": user.login,
                "password": user.password
            }
            return User.model_validate(obj=responce)
        raise HTTPException(
            detail="Не найден пользователь с таким id",
            status_code=status.HTTP_404_NOT_FOUND,
        )

@router.put("create_user/", status_code=status.HTTP_201_CREATED, response_model=User)
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
            'id': len(user_repo),
            'login': new_user.login,
            'password': new_user.password,
        }
        return User.model_validate(obj=responce)

@router.delete("delete_user/<user_id>/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id : int):
    if not any(user['login'] == user.login for user in user_repo):
        raise HTTPException(
            detail="Пользователя с таким логином нет",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        for u in user_repo:
            if u["id"] == user_id:
                user_repo = user_repo.pop(user_id)
                return user_repo
