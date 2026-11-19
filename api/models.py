from django.db import models
from django.contrib.auth.models import AbstractUser

from pgvector.django import VectorField

class Teacher(AbstractUser):
    teacher_name = models.CharField(max_length=100, verbose_name="Подпись в уроке")

class Lesson(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Учитель",
    )
    date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата урока",
    )
    level = models.CharField(
        max_length=50,
        verbose_name="Уровень",
    )
    topic = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Тема",
    )
    lesson_type = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Тип урока",
    )
    duration_minutes = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Длительность (мин)",
    )
    aim = models.TextField(verbose_name="Цель урока")
    sub_aim = models.CharField(
        max_length=400,
        blank=True,
        verbose_name="Подцель урока",
    )
    homework_summary = models.CharField(
        max_length=400,
        blank=True,
        verbose_name="Краткое ДЗ",
    )

    plan_json = models.JSONField(verbose_name="План урока (JSON)")
    embedding = VectorField(
        dimensions=384,
        verbose_name="Эмбеддинг",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создан",
    )
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"