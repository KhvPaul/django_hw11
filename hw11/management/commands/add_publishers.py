from django.core.management.base import BaseCommand

from faker import Faker

from hw11.models import Publisher


class Command(BaseCommand):
    help = 'Creates the specified number of new publishers. You must specify a number'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('add_publishers', nargs='?', type=int, choices=range(1, 100000), default=25,
                            help='You must specify a count of publishers [1; 100000] (default = 25)',
                            metavar='publishers_count')

    def handle(self, *args, **options):
        for j in range(options['add_publishers']):
            Publisher.objects.create(name=f'{Faker().name()} Publishing House')
            self.stdout.write(self.style.SUCCESS('Successfully added publisher "%s"' % Publisher.objects.last().name))
