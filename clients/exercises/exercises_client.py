from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUsersSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema


class ExercisesClient(APIClient):
    """
    Клиент для работы с занятиями
    """

    def get_exercise_api(self) -> Response:
        """
        Метод получения списка занятий по курсу
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.get("/api/v1/exercises")


    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания занятия
        :param request: схема создания занятия
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUsersSchema) -> ExercisesClient:
    """
    Функция создает экземпляр CoursesClient с уже настроенным http клиентом
    :return: Готовый к работе экземпляр CoursesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
