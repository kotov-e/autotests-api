"""
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
"""


from pydantic import BaseModel, Field, ConfigDict
from typing import Any

class ValidationErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ошибки валидации API
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx") # context читабельность - что такое ctx, мы указали alias
    message: str = Field(alias="msg")
    location:  list[str]= Field(alias="loc")

class ValidationErrorResponseSchema(BaseModel):
    """
    Модель, описывающая структуру ошибки API c ошибкой валидации
    """
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorSchema] = Field(alias="detail")


class InternalErrorResponseSchema(BaseModel):
    """
    Модель, описывающая структуру внутренней ошибки API
    """
    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias="detail")