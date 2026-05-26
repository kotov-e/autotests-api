import pytest

from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient


@pytest.fixture  # по умолчанию [FUNCTION]
def authentication_client() -> AuthenticationClient:
    """
    Фикстура для работы с аутентификационным API
    :return: AuthenticationClient
    """
    return get_authentication_client()
