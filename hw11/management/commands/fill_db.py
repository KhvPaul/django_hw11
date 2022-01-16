import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fills the database with pseudo-conscious values.' \
           ' You must specify a count of values \'authors_count publishers_count books_count stores_count\'' \
           ' \n 0 to fill db with default values 150 25 500 40 '  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('fill_db', nargs='+', type=int, choices=range(0, 100000),
                            help='You must specify a count of values \'authors_count publishers_count books_count '
                                 'stores_count\' \n 0 to fill db with default values 150 25 500 40')

        # parser.add_argument('fill_db', required=False)

    def handle(self, *args, **options):
        options['fill_db'] += [0, 0, 0]

        os.system(f"python manage.py add_authors {options['fill_db'][0] if options['fill_db'][0] else 150}")
        os.system(f"python manage.py add_publishers {options['fill_db'][1] if options['fill_db'][1] else 25}")
        os.system(f"python manage.py add_books {options['fill_db'][2] if options['fill_db'][2] else 500}")
        os.system(f"python manage.py add_stores {options['fill_db'][3] if options['fill_db'][3] else 40}")

        self.stdout.write(self.style.SUCCESS('Successfully filled the database with pseudo-conscious objects'))
