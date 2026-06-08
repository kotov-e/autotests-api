import allure
from httpx import Request, Response
from tools.http.curl import make_curl_from_request
from tools.logger import get_logger

logger = get_logger("HTTP_LOGGER")


def curl_event_hook(request: Request):
    """
    Event hook, который вызывается при отправке запроса. Для автоматического прикрепления cURL команды к allure отчету.
    :param request: HTTP запрос, переданный в httpx клиенте
    """
    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)


def log_request_event_hook(request: Request):
    """
    Логирует информацию об отправленном HTTP запросе
    :param request: Объект запроса HTTPX
    """
    logger.info(
        f'Make {request.method} request to {request.url}'
    )


def log_response_event_hook(response: Response):
    """
    Логирует информацию об полученном HTTP запросе
    :param response: Объект ответа HTTPX
    """
    logger.info(
        f'Got response {response.status_code} {response.reason_phrase} from {response.url}'
    )
