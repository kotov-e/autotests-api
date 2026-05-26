
from httpx import Client, URL, QueryParams, Response
from typing import Any
from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client):
        """
        Базовый API клиент для выполнения запросов
        :param client: экземпляр httpx.Client для выполнения запросов
        """
        self.client = client

    def get(self,
            url: URL | str,
            params: QueryParams | None = None
            ) -> Response:
        """
        Выполняет GET запрос
        :param url: URL
        :param params: параметры запроса
        :return: объект Response с данными ответа
        """
        return self.client.get(url, params=params)

    def post(self,
             url: URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None
             ) -> Response:
        """
        Выполняет POST запрос
        :param url: URL
        :param json: json данные
        :param data: данные запроса
        :param files: файлы
        :return: объект Response с данными ответа
        """
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self,
              url: URL | str,
              json: Any | None = None
              ) -> Response:
        """
        Выполняет PATCH запрос
        :param url: URL
        :param json: json данные запроса
        :return: object Response с данными ответа
        """
        return self.client.patch(url, json=json)

    def delete(self,
               url: URL | str
               ) -> Response:
        """
        Выполняет DELETE запрос
        :param url: URL
        :return: object Response с данными ответа
        """
        return self.client.delete(url)