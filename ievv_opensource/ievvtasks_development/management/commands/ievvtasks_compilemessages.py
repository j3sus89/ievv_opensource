from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Compile translations.'

    def handle(self, *args, **options):
        management.call_command('compilemessages')
