import pytest

from fixtures.users import UserFixture
from clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus

from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_user, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
class TestUsers:
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(
            email=fake.email(domain=email)
        )
        response = public_users_client.create_user_api(request)  # возвращает ответ от сервера
        response_data = CreateUserResponseSchema.model_validate_json(
            response.text)  # если response.text не json, то будет ошибка, model_validate_json преобразует json в объект модели

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        # HTTPSStatus.OK = 200, HTTPStatus.BAD_REQUEST = 400, HTTPStatus.NOT_FOUND = 404, HTTPStatus.CREATED = 201, HTTPStatus.ACCEPTED = 202
        # HTTPStatus.is_success = 200, 201, 202, 203, 204, 205, 206, 207, 208, 226
        # HTTPStatus.is_success(response.status_code)

        assert_create_user_response(request, response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_get_user_me(self, function_user: UserFixture, private_users_client: PrivateUsersClient):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_user_response(create_user_response=function_user.response, get_user_me_response=response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
