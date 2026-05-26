
from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверрка json объект (instance) на соответствие json схеме (schema)

    :param instance: JSON объект
    :param schema: JSON схема
    :raise: jsonschema.exceptions.ValidationError: если instance объект не соответствует schema схеме
    """
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )