import os

from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float = 5 # .env имеет приоритет

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", # .env.dev .enev.stable .env.prod ...
        env_file_encoding="utf-8",
        env_nested_delimiter="." # разделитель вложенные модели HTTP_CLIENT.URL HTTP_CLIENT.TIMEOUT TEST_DATA.IMAGE_PNG_FILE
                            #"__" HTTP_CLIENT__URL HTTP_CLIENT__TIMEOUT
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig

#os.environ.setdefault("HTTP_CLIENT.TIMEOUT", "200") # наибольший приоритет

settings = Settings() # глобальная переменная, не через фикстуру


