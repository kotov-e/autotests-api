from httpx import Client

from typing import TypedDict


class AuthenticationUsersDict(TypedDict):
        phoneNumberOrEmail: str
        password: str


HOST = "https://api.prod.booking.ktsf.ru"


def get_public_http_client() -> Client: # без заголовков
    return Client(
        timeout=100,
        base_url=f"{HOST}"
    )



