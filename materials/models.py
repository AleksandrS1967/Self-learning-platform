from django.db import models
from config.settings import AUTH_USER_MODEL

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название",
        help_text="Введите название курса"
    )
    description = models.TextField(verbose_name="Описание",
                                   **NULLABLE)
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="владелец",
        help_text="Укажите владельца",
        **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Название",
        help_text="Введите название урока"
    )
    description = models.TextField(verbose_name="Описание",
                                   **NULLABLE)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Укажите курс",
        related_name="lesson",
    )
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
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Test(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Название",
        help_text="Введите название теста"
    )
    description = models.TextField(
        verbose_name="Описание вопроса",
        help_text="Укажите Описание вопроса",
    )
    correct_answer = models.TextField(
        verbose_name="Правильный ответ",
        help_text="Укажите Правильный ответ",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Укажите урок",
        related_name="test",
    )
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
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class AttemptAnswer(models.Model):
    answer = models.TextField(
        verbose_name="Попытка ответа",
        help_text="Укажите ваш ответ",
    )
    answer_bool = models.BooleanField(verbose_name="Правильно/Неправильно",
                                      **NULLABLE)
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name="Тест",
        help_text="Укажите тест",
        related_name="attempt_answer",
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="владелец",
        help_text="Укажите владельца",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.answer}"

    class Meta:
        verbose_name = "Попытка ответа"
        verbose_name_plural = "Попытки ответа"
