from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUsersSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, GetExerciseQuerySchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetCourseQuerySchema


class ExercisesClient(APIClient):
    """
    Клиент для работы с занятиями
    """

    def get_exercise_api(self, query: GetCourseQuerySchema) -> Response:
        """
        Метод получения занятия по id
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))


    def get_exercise_id_api(self, exercise_id: str) -> Response:
        """
        Метод получения занятия по id
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")


    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания занятия
        :param request: схема создания занятия
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))


    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создания занятия
        :param request: схема создания занятия
        :return: Ответ от сервера в виде объекта CreateExerciseResponseSchema
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)


    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления занятия
        :param exercise_id: id занятия
        :param request: схема обновления занятия
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))


    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления занятия
        :param exercise_id:
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUsersSchema) -> ExercisesClient:
    """
    Функция создает экземпляр CoursesClient с уже настроенным http клиентом
    :return: Готовый к работе экземпляр CoursesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
