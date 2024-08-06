from django.db import models
from config.settings import AUTH_USER_MODEL

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название", help_text="Введите название курса"
    )
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="владелец",
        help_text="Укажите владельца",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
