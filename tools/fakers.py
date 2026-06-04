
from faker import Faker


class FakeClass:
    """
    Класс для генерации случайных данных с помощью библиотеки faker
    """
    def __init__(self, faker: Faker):
        """
        Инициализация класса
        :param faker: экземпляр класса Faker, который будет использоваться для генерации данных
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст
        :return: строка с случайным текстом
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует случайный uuid4
        :return: строка со случайным uuid4
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email адрес
        :return: строка с случайным email адресом
        """
        return self.faker.email(domain=domain)

    def phone_number(self) -> str:
        """
        Генерирует случайный номер телефона
        :return: строка со случайным номером телефона
        """
        operator = self.faker.random_int(900, 999)
        number = self.faker.random_int(1, 999_99_99)
        return f"+7{operator}{number:07d}"

    def sentence(self) -> str:
        """
        Генерирует случайное предложение
        :return: строка со случайным предложением
        """
        return self.faker.sentence()

    def word(self):
        """
        Генерирует случайное слово
        :return: строка со случайным словом
        """
        return self.faker.word()

    def password(self) -> str:
        """
        Генерирует случайный пароль
        :return: строка с случайным паролем
        """
        return self.faker.password()

    def first_name(self) -> str:
        """
        Генерирует случайное имя
        :return: строка со случайным именем
        """
        return self.faker.first_name()

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию
        :return: строка со случайной фамилией
        """
        return self.faker.last_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество
        :return: строка со случайным отчеством
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Генерирует случайное целое число
        :return: строка со случайным числом недель
        """
        return f"{self.integer(1,10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне
        :param start: начало диапазона
        :param end: конец диапазона
        :return: целое число в заданном диапазоне
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Генерирует случайное целое число
        :return: целое число от 50 до 100
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Генерирует случайное целое число
        :return: целое число от 1 до 30
        """
        return self.integer(1, 30)


fake = FakeClass(faker=Faker()) # ru_RU
en_faker = FakeClass(faker=Faker(locale="en_US"))
arabic_faker = FakeClass(faker=Faker(locale="ar_AA"))

#print(fake.phone_number())