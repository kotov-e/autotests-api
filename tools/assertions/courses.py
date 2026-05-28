from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


def assert_updated_courses_response(response: UpdateCourseResponseSchema, request: UpdateCourseRequestSchema):
    """
    Функция проверки ответа на обновление курса
    :param response: данные ответа
    :param request: данные запроса
    :return: AssertionError, если хотя бы одно из полей ответа не совпадают
    """
    assert_equal(actual=response.course.title, expected=request.title, name="title")
    assert_equal(actual=response.course.max_score, expected=request.max_score, name="max_score")
    assert_equal(actual=response.course.min_score, expected=request.min_score, name="min_score")
    assert_equal(actual=response.course.description, expected=request.description, name="description")
    assert_equal(actual=response.course.estimated_time, expected=request.estimated_time, name="estimated_time")


def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Функция проверки полей курса
    :param actual: данные курса
    :param expected: ожидаемые данные курса
    :return: AssertionError, если хотя бы одно из полей не совпадают
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
):
    """
    Функция проверки ответа на получение курсов
    :param get_courses_response: данные ответа
    :param create_course_responses: данные запроса
    :return: AssertionError, если хотя бы один курс не совпадает
    """
    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_responses in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_responses.course)

