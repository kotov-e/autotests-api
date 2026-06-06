import httpx
import allure

from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
from config import settings


@allure.step("Check create file response")
def assert_create_file_response(response: CreateFileResponseSchema, request: CreateFileRequestSchema):
    """
    Проверяет структуру ответа на запрос создания файла
    :param request: запрос на создание файла
    :param response: ответ с данными файла
    :return: AssertionError, если хотя бы одно поле не совпадает
    """
    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"
    assert_equal(str(response.file.url), expected_url, name="url")
    assert_equal(response.file.filename, request.filename, name="filename")
    assert_equal(response.file.directory, request.directory, name="directory")
    assert_file_is_accessible(str(response.file.url))


@allure.step("Check file is accessible")
def assert_file_is_accessible(url: str, ):
    """
    Проверяет доступность файла по ссылке
    :param url: ссылка на файл
    :return: AssertionError, если файл недоступен
    """
    response = httpx.get(url)
    assert response.status_code == 200, f"Файл по ссылке {url} недоступен"


@allure.step("Check file")
def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет структуру ожидаемого и фактического файла
    :param actual: фактические данные файл
    :param expected: ожидаемые данные файл
    :return: AssertionError, если хотя бы одно поле не совпадает
    """
    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.filename, expected.filename, name="filename")
    assert_equal(actual.directory, expected.directory, name="directory")
    assert_equal(actual.url, expected.url, name="id")


@allure.step("Check get file response")
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    Проверяет структуру ответа на запрос получения файла и структуру созданного файла
    :param get_file_response: ответ на запрос получения файла
    :param create_file_response: ответ на запрос создания файла
    :return: AssertionError, если ответы не совпадает
    """
    assert_file(get_file_response.file, create_file_response.file)


@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем содержит ожидаемую ошибку
    :param actual: ответ от API с ошибкой валидации, которую необходимо проверить
    :return: AssertionError, если фактический ответ не совпадает с ожидаемым
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"]
            )
        ]
    )

    assert_validation_error_response(actual, expected)


@allure.step("Check create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустой директорией содержит ожидаемую ошибку
    :param actual: ответ от API с ошибкой валидации, которую необходимо проверить
    :return: AssertionError, если фактический ответ не совпадает с ожидаемым
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"]
            )
        ]
    )

    assert_validation_error_response(actual, expected)


@allure.step("Check file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере
    :param actual: фактический ответ API
    :return: AssertionError если фактический ответ не совпадает ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)


@allure.step("Check get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """

    :param actual:
    :return:
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=["path", "file_id"],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-file-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                }
            )
        ]
    )

    assert_validation_error_response(actual, expected)
