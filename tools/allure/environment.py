import platform
import sys
from config import settings


def create_allure_environment_file():
    """
    Функция создания списка с элементами key=value из модели settings и
    запись в файл environment.properties в директории allure_results_dir
    """
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    items.append(f'system_platform={platform.platform()}')
    items.append(f'system_machine={platform.machine()}')
    items.append(f'python version={sys.version}') # {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}
    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)


