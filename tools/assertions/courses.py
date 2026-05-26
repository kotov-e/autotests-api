from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.assertions.base import assert_equal


def assert_updated_courses_response(response: UpdateCourseResponseSchema, request: UpdateCourseRequestSchema):
    assert_equal(actual=response.course.title, expected=request.title, name="title")
    assert_equal(actual=response.course.max_score, expected=request.max_score, name="max_score")
    assert_equal(actual=response.course.min_score, expected=request.min_score, name="min_score")
    assert_equal(actual=response.course.description, expected=request.description, name="description")
    assert_equal(actual=response.course.estimated_time, expected=request.estimated_time, name="estimated_time")
