from django.contrib import admin

from materials.models import Course


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
