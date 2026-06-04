from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
import allure


@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.
    :param actual: Фактическая ошибка валидации
    :param expected: Ожидаемая ошибка валидации
    :return: AssertionError если ошибки не совпадают
    """
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")


@allure.step("Check validation error response")
def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema
):
    """
    Проверяет, что объект ответа API с ошибками валидации соответствует ожидаемому значению.
    :param actual: Фактический ответ API
    :param expected: Ожидаемый ответ API
    :return: AssertionError если ответы не совпадают
    """
    assert_length(actual.details, expected.details, "details")

    # assert_equal(actual.details, expected.details, "details") если ошибка, то в логах будет очень много информации

    for index, detail in enumerate(expected.details):  # enumerate - возвращает индекс и значение
        assert_validation_error(actual.details[index], detail)


@allure.step("Check internal error response")
def assert_internal_error_response(
        actual: InternalErrorResponseSchema,
        expected: InternalErrorResponseSchema
):
    """
    Функция для проверки внутренней ошибки API, например: 404
    :param actual: фактический ответ API
    :param expected: ожидаемый ответ API
    :return: AssertionError если ответы не совпадают
    """
    assert_equal(actual.details, expected.details, "details")
