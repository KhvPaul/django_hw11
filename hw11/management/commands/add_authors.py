import random

from django.core.management.base import BaseCommand

from faker import Faker

from hw11.models import Author


class Command(BaseCommand):
    help = 'Creates the specified number of new authors. You must specify a number'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('add_authors', type=int, choices=range(1, 100000), help='The passed value of the created '
                                                                                    'authors')

    def handle(self, *args, **options):
        for j in range(options['add_authors']):
            Author.objects.create(name=Faker().name(), age=random.randint(15, 98))
            self.stdout.write(self.style.SUCCESS('Successfully added author "%s, %s"' % (Author.objects.last().name,
                                                                                         Author.objects.last().age)))
