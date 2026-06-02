from typing import Any, Sized # Sized - те типы данных, которые поддерживают метод __len__ (у которых есть длина)

def assert_status_code(actual: int, expected: int) -> None:
    """
    Проверка факртического и ожидаемого статус кода
    :param actual: фактический статус код
    :param expected: ожидаемый статус код
    :raise AssertionError: Если статус коды не совпадают
    """
    assert actual == expected, (
        f"\n"
        "Incorrect response status code \n"
        f"Expected status code: {expected} \n"
        f"Actual status code: {actual}"
    )


def assert_equal(actual: Any, expected: Any, name: str) -> None:
    """
    Проверка фактического и ожидаемого значения
    :param actual: фактическое значение
    :param expected: ожидаемое значение
    :param name: назнание поля
    :raise AssertionError: Если значения не совпадают
    """
    assert actual == expected, (
        f"\n"
        f"Incorrect value on field: {name} \n"
        f"Expected value: {expected} \n"
        f"Actual value: {actual}"
    )

def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: {name}'
        f'Expected true alue but got {actual}'
    )


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет длины двух объектов совпадают
    :param actual: фактическое значение длины
    :param expected: ожидаемое значение длины
    :param name: название поля
    :return: AssertionError если длины не совпадают
    """

    assert len(actual) == len(expected), (
        f"Incorrect object length: '{name}' \n"
        f"Expected length: {len(expected)} \n"
        f"Actual length: {len(actual)}"
    )