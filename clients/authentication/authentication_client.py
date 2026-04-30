
from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса для логина
    """
    phoneNumberOrEmail: str
    password: str


class RefreshTokenRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена
    """
    refreshToken: str


class AuthenticationClient(ApiClient):
    """
    Класс клиента для работы с аутентификацией
    """
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод для логина
        :param request: словарь с данными для логина
        :return: ответ от сервера в виде httpx Response
        """
        return self.post("/api/auth/login", json=request)

    def refresh_token_api(self, request: RefreshTokenRequestDict) -> Response:
        """
        Метод для обновления токена
        :param request: словарь с данными для обновления токена
        :return: ответ от сервера в виде httpx Response
        """
        return self.post("/api/auth/refresh-token", json=request)

