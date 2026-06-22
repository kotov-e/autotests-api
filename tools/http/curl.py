from httpx import Request, RequestNotRead


def make_curl_from_request(request: Request) -> str:
    """
    Генерирует curl-запрос из httpx-запроса
    :param request: HTTP-запрос, из которого нужно сгенерировать curl каманду
    :return: Строка с командой curl, содержащая все необходимые параметры
    """
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    try:
        if body := request.content: # := моржовое присваивание, одновременно присвоить значение переменной и использовать его в выражении
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    return " \\\n  ".join(result)
