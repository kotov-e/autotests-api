import allure
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal
from tools.logger import get_logger

logger = get_logger("USER_ASSERTIONS")

@allure.step("Check create user response")
def assert_create_user_response(response: CreateUserResponseSchema, request: CreateUserRequestSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу
    :param request: Исходный запрос
    :param response: Ответ на запрос с данными пользователя
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    logger.info("Check create user response")

    assert_equal(actual=response.user.email, expected=request.email, name="email")
    assert_equal(actual=response.user.first_name, expected=request.first_name, name="first_name")
    assert_equal(actual=response.user.last_name, expected=request.last_name, name="last_name")
    assert_equal(actual=response.user.middle_name, expected=request.middle_name, name="middle_name")


@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет, что пользователь совпадает с ожидаемым
    :param actual: фактический пользователь
    :param expected: ожидаемый пользователь
    :return: AssertionError, если хотя бы одно поле не совпадает
    """
    logger.info("Check user")

    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.email, expected=expected.email, name="email")
    assert_equal(actual=actual.last_name, expected=expected.last_name, name="last_name")
    assert_equal(actual=actual.first_name, expected=expected.first_name, name="first_name")
    assert_equal(actual=actual.middle_name, expected=expected.middle_name, name="middle_name")


@allure.step("Check get user response")
def assert_get_user_response(get_user_me_response: GetUserResponseSchema,
                             create_user_response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на получение пользователя совпадает с ответом на создание пользователя
    :param get_user_me_response: ответ на получение пользователя
    :param create_user_response: ответ на создание пользов
    :return: AssertionError, если ответы не совпадают
    """
    logger.info("Check get user response")

    assert_user(get_user_me_response.user, create_user_response.user)
