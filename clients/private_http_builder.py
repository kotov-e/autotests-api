from httpx import Client
from pydantic import BaseModel, Field, ConfigDict
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from functools import lru_cache

class AuthenticationUsersSchema(BaseModel, frozen=True): # теперь это неизменяемый объект
    model_config = ConfigDict(populate_by_name=True)

    email: str = Field(alias="email")
    password: str = Field(alias="password")

@lru_cache(maxsize=None) # кеширует возвращаемое значение функции
def get_private_http_client(user: AuthenticationUsersSchema) -> Client:
    """
    Функция создает экземпляр httpx Client с аутентификацией пользователя
    :param user: Объект AuthenticationUsersSchema с phoneNumberOrEmail и password
    :return: Готовый к работе экземпляр httpx Client c у становленным заголовком Authorization
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
