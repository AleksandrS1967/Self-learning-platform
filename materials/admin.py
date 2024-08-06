from django.contrib import admin

from materials.models import Course, Lesson, Test, AttemptAnswer


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(Test)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(AttemptAnswer)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk",)
