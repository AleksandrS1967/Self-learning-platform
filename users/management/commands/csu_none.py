from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Удаление суперпользователя."""

    def handle(self, *args, **options):
        user = User.objects.get(
            email="admin@rambler.ru",
        ).delete()
