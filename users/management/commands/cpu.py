from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@rambler.ru",
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("1234")
        user.save()

        user = User.objects.create(
            email="alexandr@top.ru",
            is_active=True,
            is_staff=True,
            is_superuser=False,
        )

        user.set_password("1234")
        user.save()

        user = User.objects.create(
            email="sergo@top.ru",
            is_active=True,
            is_staff=True,
            is_superuser=False,
        )

        user.set_password("1234")
        user.save()

        user = User.objects.create(
            email="test@top.ru",
            is_active=True,
            is_staff=True,
            is_superuser=False,
        )

        user.set_password("1234")
        user.save()
