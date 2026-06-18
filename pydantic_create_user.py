from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """
    Описывает структуру данных пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    Описывает запрос на создание пользователя
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserResponseSchema(BaseModel):
    """
    Описывает ответ с данными созданного пользователя
    """
    user: UserSchema
