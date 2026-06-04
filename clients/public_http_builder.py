from httpx import Client

from clients.event_hooks import curl_event_hook


def get_public_http_client() -> Client: # без заголовков
    """
    Функция создает экземпляр httpx.Client с базовами настройками
    :return: Готовый клиент
    """
    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        event_hooks={"request": [curl_event_hook]}
    )