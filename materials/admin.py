from django.contrib import admin

from materials.models import Course, Lesson, Test, AttemptAnswer


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(AttemptAnswer)
class AttemptAnswerAdmin(admin.ModelAdmin):
    list_display = ("pk", "answer", "answer_bool")
