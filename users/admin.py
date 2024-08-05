from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Вывод пользователя в админку."""
    list_display = ("pk", "email")

