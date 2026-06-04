from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, \
    ExerciseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema, GetExerciseResponseSchema, \
    GetExerciseIdResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response
import allure


@allure.step("Check exercise")
def assert_exercise(response: ExerciseSchema, request: ExerciseSchema):
    """
    Проверяет, что ответ на создание задания соответствует ожидаемому
    :param response: ответ на создание задания
    :param request: запрос на создание задания
    :return: AssertionError если хотя бы одно поле не совпадает
    """
    assert_equal(actual=response.title, expected=request.title, name="title")
    assert_equal(actual=response.course_id, expected=request.course_id, name="course_id")
    assert_equal(actual=response.max_score, expected=request.max_score, name="max_score")
    assert_equal(actual=response.min_score, expected=request.min_score, name="min_score")
    assert_equal(actual=response.order_index, expected=request.order_index, name="order_index")
    assert_equal(actual=response.description, expected=request.description, name="description")
    assert_equal(actual=response.estimated_time, expected=request.estimated_time, name="estimated_time")


@allure.step("Check create exercise response")
def assert_create_exercise_response(response: CreateExerciseResponseSchema, request: CreateExerciseRequestSchema):
    """
    Проверяет, что ответ на создание задания соответствует ожидаемому
    :param response: ответ на создание задания
    :param request: запрос на создание задания
    :return: AssertionError если хотя бы одно поле не совпадает
    """
    assert_equal(actual=response.exercise.title, expected=request.title, name="title")
    assert_equal(actual=response.exercise.course_id, expected=request.course_id, name="course_id")
    assert_equal(actual=response.exercise.max_score, expected=request.max_score, name="max_score")
    assert_equal(actual=response.exercise.min_score, expected=request.min_score, name="min_score")
    assert_equal(actual=response.exercise.order_index, expected=request.order_index, name="order_index")
    assert_equal(actual=response.exercise.description, expected=request.description, name="description")
    assert_equal(actual=response.exercise.estimated_time, expected=request.estimated_time, name="estimated_time")


@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExerciseResponseSchema,
        create_exercises_responses: list[CreateExerciseResponseSchema]
):
    """
    Функция проверки ответа на получение заданий
    :param get_exercises_response: данные ответа
    :param create_exercises_responses: данные запроса
    :return: AssertionError, если хотя бы один курс не совпадает
    """
    assert_length(get_exercises_response.exercises, create_exercises_responses, "exercises")

    for index, create_exercises_responses in enumerate(create_exercises_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercises_responses.exercise)


@allure.step("Check get exercise id response")
def assert_get_exercise_id_response(response: GetExerciseIdResponseSchema, request: CreateExerciseRequestSchema,
                                    exercise_id: str):
    """
    Проверяет, что ответ на получение задания соответствует ожидаемому
    :param response: ответ на получение задания
    :param request: запрос на получение задания
    :param exercise_id: id задания
    :return: AssertionError если хотя бы одно поле не совпадает
    """
    assert_equal(actual=response.exercise.title, expected=request.title, name="title")
    assert_equal(actual=response.exercise.course_id, expected=request.course_id, name="course_id")
    assert_equal(actual=response.exercise.max_score, expected=request.max_score, name="max_score")
    assert_equal(actual=response.exercise.min_score, expected=request.min_score, name="min_score")
    assert_equal(actual=response.exercise.order_index, expected=request.order_index, name="order_index")
    assert_equal(actual=response.exercise.description, expected=request.description, name="description")
    assert_equal(actual=response.exercise.estimated_time, expected=request.estimated_time, name="estimated_time")
    assert_equal(response.exercise.id, exercise_id, "id")


@allure.step("Check update exercise response")
def assert_update_exercise_response(response: UpdateExerciseResponseSchema, request: UpdateExerciseRequestSchema):
    """
    Проверяет, что ответ на обновление задания соответствует ожидаемому
    :param response: ответ на обновление задания
    :param request: запрос на обновление задания
    :return: AssertionError если хотя бы одно поле не совпадает
    """
    assert_equal(actual=response.exercise.title, expected=request.title, name="title")
    assert_equal(actual=response.exercise.max_score, expected=request.max_score, name="max_score")
    assert_equal(actual=response.exercise.min_score, expected=request.min_score, name="min_score")
    assert_equal(actual=response.exercise.order_index, expected=request.order_index, name="order_index")
    assert_equal(actual=response.exercise.description, expected=request.description, name="description")
    assert_equal(actual=response.exercise.estimated_time, expected=request.estimated_time, name="estimated_time")


@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание не найдено
    :param actual: фактический ответ API
    :return: AssertionError если фактический ответ не совпадает ошибке "Exercise not found"
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)
