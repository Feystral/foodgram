from django.core.management import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):
    help = 'Создаем тэги'

    def handle(self, *args, **kwargs):
        data = [
            {'name': 'Завтрак', 'slug': 'breakfast'},
            {'name': 'Обед', 'slug': 'lunch'},
            {'name': 'Ужин', 'slug': 'dinner'}]
        Tag.objects.bulk_create(Tag(**tag) for tag in data)
        self.stdout.write(self.style.SUCCESS('Все тэги загружены!'))
