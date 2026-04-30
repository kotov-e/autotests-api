
from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

class UpdateUserProfileRequest(TypedDict):
    firstName: str | None
    lastName: str | None

class UsersClient(ApiClient):
    """
    Класс для работы с API пользователей
    """
    def user_profile_api(self) -> Response:
        """
        Метод для получения профиля пользователя
        :return: ответ от сервера httpx Response
        """
        return self.get('/api/v1/user/user-profile')

    def user_profile_id_api(self,
                            user_id: str
                            ) -> Response:
        """
        Метод для получения профиля пользователя по id
        :param user_id: id пользователя
        :return: ответ от сервера httpx Response
        """
        return self.get(f'/api/v1/user/{user_id}')

    def update_user_api(self,
                        request: UpdateUserProfileRequest
                        ) -> Response:
        """
        Метод для обновления профиля пользователя
        :param request: данные для обновления, поля не обязательные
        :return: ответ от сервера httpx Response
        """
        return self.patch('/api/v1/user/user-profile/update', json=request)

    def delete_user_api(self) -> Response:
        """
        Метод для удаления профиля пользователя
        :return: ответ от сервера httpx Response
        """
        return self.delete('/api/v1/user/user-profile/delete')