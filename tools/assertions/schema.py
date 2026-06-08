import allure
from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
from tools.logger import get_logger

logger = get_logger("SCHEMA_ASSERTIONS")

@allure.step("Validation JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверрка json объект (instance) на соответствие json схеме (schema)

    :param instance: JSON объект
    :param schema: JSON схема
    :raise: jsonschema.exceptions.ValidationError: если instance объект не соответствует schema схеме
    """
    logger.info("Validation JSON schema")

    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )