from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUsersSchema
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema, CreateExerciseResponseSchema,
                                                GetExerciseQuerySchema, UpdateExerciseRequestSchema)
import allure
from tools.routes import APIRoutes
from clients.api_coverage import tracker

class ExercisesClient(APIClient):
    """
    Клиент для работы с занятиями
    """

    @allure.step("Get exercises")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}")
    def get_exercise_api(self, query: GetExerciseQuerySchema) -> Response:
        """
        Метод получения занятия по id
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.get(f"{APIRoutes.EXERCISES}", params=query.model_dump(by_alias=True))

    @allure.step("Get exercises by id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def get_exercise_id_api(self, exercise_id: str) -> Response:
        """
        Метод получения занятия по id
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create exercise")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания занятия
        :param request: схема создания занятия
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.post(f"{APIRoutes.EXERCISES}", json=request.model_dump(by_alias=True))

    @allure.step("Create exercise")
    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создания занятия
        :param request: схема создания занятия
        :return: Ответ от сервера в виде объекта CreateExerciseResponseSchema
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Update exercise by id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления занятия
        :param exercise_id: id занятия
        :param request: схема обновления занятия
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления занятия
        :param exercise_id:
        :return: Ответ от сервера в виде объекта httpx Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")


def get_exercises_client(user: AuthenticationUsersSchema) -> ExercisesClient:
    """
    Функция создает экземпляр CoursesClient с уже настроенным http клиентом
    :return: Готовый к работе экземпляр CoursesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
