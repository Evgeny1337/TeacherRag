from datetime import date as Date
from idlelib.history import History

from ninja import Schema, ModelSchema
from pydantic import Field, PositiveInt

from api.models import Lesson


class LessonRequestSchema(Schema):
    date: Date | None = Field(default=None, description="Дата урока")
    level: str = Field(description="Уровень")
    topic: str = Field(default="", description="Тема урока")
    lesson_type: str = Field(default="", description="Тип урока")
    duration_minutes: PositiveInt | None = Field(
        default=None, description="Длительность урока в минутах"
    )
    aim: str = Field(description="Цель урока")
    sub_aim: str = Field(default="", description="Подцель урока")
    homework_summary: str = Field(default="", description="Краткое ДЗ")
    plan_json: dict = Field(description="План урока в JSON-формате")
    embed_text: str = Field(description="Текст для эмбеддинга")


class SimilarRequestSchema(Schema):
    embed_text: str = Field(description="Текст запроса для поиска похожих уроков")
    level: str | None = Field(default=None, description="Опциональный фильтр по уровню")
    lesson_type: str | None = Field(
        default=None, description="Опциональный фильтр по типу урока"
    )
    limit: PositiveInt = Field(default=3, description="Сколько уроков вернуть")


class PlansResponseSchema(Schema):
    plans: list[dict] = Field(description="Список планов уроков")
    plans_count: int = Field(description="Количество планов уроков")


class MessageResponseSchema(Schema):
    message: str = Field(description="Сообщение о результате операции")


class HistoryResponseSchema(ModelSchema):
    class Meta:
        model = Lesson
        fields = ('id', 'created_at', 'aim', 'topic',)

