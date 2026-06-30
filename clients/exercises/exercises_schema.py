from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка заданий.
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения задания.
    """
    exercise: ExerciseSchema


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления данных задания.
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    course_id: str


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(default_factory=fake.uuid4)     # Генерация только для негативных тестов
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    order_index: int = Field(default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление данных задания.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    order_index: int | None = Field(default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)
