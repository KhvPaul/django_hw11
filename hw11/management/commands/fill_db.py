from django.core.management import call_command

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fills the database with pseudo-conscious values. \n' \
           ' You must specify a count of values [authors_count, publishers_count, books_count, stores_count]' \
           ' \n empty field to fill db with default values [150 25 500 40] '  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('authors', nargs='?', type=int, choices=range(1, 100000), default=150,
                            help='You must specify a count of authors [1; 100000] (default = 150)',
                            metavar='authors_count')
        parser.add_argument('publishers', nargs='?', type=int, choices=range(1, 100000), default=25,
                            help='You must specify a count of publishers [1; 100000] (default 25)',
                            metavar='publishers_count')
        parser.add_argument('books', nargs='?', type=int, choices=range(1, 100000), default=500,
                            help='You must specify a count of books [1; 100000] (default 500)',
                            metavar='books_count')
        parser.add_argument('stores', nargs='?', type=int, choices=range(1, 100000), default=40,
                            help='You must specify a count of stores [1; 100000] (default 40)',
                            metavar='stores_count')

    def handle(self, *args, **options):
        call_command("add_authors", options['authors'])
        call_command("add_publishers", options['publishers'])
        call_command("add_books", options['books'])
        call_command("add_stores", options['stores'])

        self.stdout.write(self.style.SUCCESS('Successfully filled the database with pseudo-conscious objects'))
