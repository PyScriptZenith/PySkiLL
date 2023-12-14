from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создания суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@mail.ru",
            first_name="Petr",
            last_name="Ivanov",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password("admin")
        user.save()
