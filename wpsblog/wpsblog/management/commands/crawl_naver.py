from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('query', type=str)

    def handle(self, *args, **options):
        query = options.get('query')

        self.stdout.write('Crawling {query} blog from Naver.'.format(
            query=query,
            ))
