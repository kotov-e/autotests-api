import pytest
from httpx import Response
from pydantic import BaseModel, EmailStr, ConfigDict
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema
from clients.private_http_builder import AuthenticationUsersSchema


class UserFixture(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUsersSchema:
        return AuthenticationUsersSchema(email=self.email, password=self.password)


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    """
    Фикстура для работы с публичным API
    :return: PublicUsersClient
    """
    return get_public_users_client()


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    """
    Фикстура для работы с приватным API
    :return: PrivateUsersClient
    """
    return get_private_users_client(user=function_user.authentication_user)


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Фикстура для создания пользователя
    :param public_users_client: PublicUsersClient
    :return: UserFixture возвращает и request и response
    """
    create_user_request = CreateUserRequestSchema()
    response = public_users_client.create_user(create_user_request)
    return UserFixture(request=create_user_request, response=response)
