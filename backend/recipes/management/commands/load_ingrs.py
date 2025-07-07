import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка ингредиентов из data/ingredients.csv'

    def handle(self, *args, **kwargs):
        file_path = Path(settings.BASE_DIR) / 'data' / 'ingredients.csv'

        with file_path.open('r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            created_count = 0
            for row in reader:
                obj, created = Ingredient.objects.get_or_create(
                    name=row['name'],
                    measurement_unit=row['measurement_unit']
                )
                if created:
                    created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Загрузка завершена.'
            f'Добавлено {created_count} новых ингредиентов.'
        ))
