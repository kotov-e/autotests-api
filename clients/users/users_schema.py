from pydantic import BaseModel, Field, ConfigDict, EmailStr
from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Описание структуры модели пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr = Field(default_factory=fake.email)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры модели запроса для создания пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    first_name: str = Field(alias="firstName",
                            default_factory=fake.first_name)
    last_name: str = Field(alias="lastName",
                           default_factory=fake.last_name)
    middle_name: str = Field(alias="middleName",
                             default_factory=fake.middle_name)
    password: str = Field(default_factory=fake.password)
    email: EmailStr = Field(alias="email",
                            default_factory=fake.email)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры модели ответа для создания пользователя
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления пользователя.
    """
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры запроса получения пользователя.
    """
    user: UserSchema
