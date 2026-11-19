from http import HTTPStatus

from ninja import Router, Status
from pgvector.django import CosineDistance

from api.embeddings import embed_text
from api.models import Lesson
from api.schemas import (
    LessonRequestSchema,
    MessageResponseSchema,
    PlansResponseSchema,
    SimilarRequestSchema,
)

teacher_router = Router(tags=["lessons"])


@teacher_router.post(
    "/",
    response={HTTPStatus.CREATED: MessageResponseSchema},
    url_name="lesson_save",
)
def save_plan(request, plan: LessonRequestSchema):
    data = plan.model_dump(exclude={"embed_text"})
    data["embedding"] = embed_text(plan.embed_text)
    Lesson.objects.create(**data)
    return Status(HTTPStatus.CREATED, MessageResponseSchema(message="ok"))


@teacher_router.post(
    "/similar",
    response={HTTPStatus.OK: PlansResponseSchema},
    url_name="lesson_similar",
)
def similar_plans(request, payload: SimilarRequestSchema):
    query = embed_text(payload.embed_text)
    qs = Lesson.objects.all()
    if payload.level:
        qs = qs.filter(level=payload.level)
    if payload.lesson_type:
        qs = qs.filter(lesson_type=payload.lesson_type)
    lessons = qs.annotate(
        distance=CosineDistance("embedding", query)
    ).order_by("distance")[: payload.limit]
    plans = [lesson.plan_json for lesson in lessons]
    return Status(
        HTTPStatus.OK,
        PlansResponseSchema(plans=plans, plans_count=len(plans)),
    )
