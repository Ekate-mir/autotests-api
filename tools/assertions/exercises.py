from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseSchema, \
    CreateExerciseResponseSchema, GetExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(request: CreateExerciseRequestSchema,
                                    response: ExerciseSchema):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.title, "title")
    assert_equal(request.course_id, response.course_id, "course_id")
    assert_equal(request.max_score, response.max_score, "max_score")
    assert_equal(request.min_score, response.min_score, "min_score")
    assert_equal(request.order_index, response.order_index, "order_index")
    assert_equal(request.description, response.description, "description")
    assert_equal(request.estimated_time, response.estimated_time, "estimated_time")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет корректность данных задания.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(get_exercise_response: GetExerciseResponseSchema,
                                 create_exercise_response: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ API при запросе пользователя соответствует ответу API при создании задания.

    :param get_exercise_response: Ответ API при запросе задания.
    :param create_exercise_response: Ответ API при создании задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)
