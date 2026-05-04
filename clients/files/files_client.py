from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict


class CreateFileRequest(TypedDict):
    """
    Описаник структуры запроса на создание файла
    """
    filename: str
    directory: str
    file: str


class FilesClient(ApiClient):
    """
    Клиент для работы с файлами
    """
    def get_file_api(self) -> Response: # нужен access_token
        """
        Метод для получения файла
        :return: Ответ от сервера в виде httpx Response
        """
        return self.get(f"/api/v1/user/user-profile/avatar")

    def create_file_api(self, request: CreateFileRequest) -> Response:
        """
        Метод для создания файла
        :param request:
        :return: Ответ от сервера в виде httpx Response
        """
        return self.post(f"/api/v1/user/user-profile/avatar",
                         date=request,
                         files={"file": open(request["file"], "rb")}
                         )

    def delete_file_api(self) -> Response:
        """
        Метод для удаления файла
        :return: Ответ от сервера в виде httpx Response
        """
        return self.delete(f"/api/v1/user/user-profile/avatar")