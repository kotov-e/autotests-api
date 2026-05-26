from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from tools.fakers import fake


class ExerciseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex")
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class CreateExerciseResponseSchema(BaseModel):
    exercises: ExerciseSchema


class GetExerciseResponseSchema(BaseModel):
    exercises: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    pass
