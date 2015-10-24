from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run makemessages for the languages specified in the ' \
           'IEVVTASKS_MAKEMESSAGES_LANGUAGE_CODES setting.'

    def handle(self, *args, **options):
        ignore = getattr(settings, 'IEVVTASKS_MAKEMESSAGES_IGNORE', [
            'static/*'
        ])
        management.call_command('makemessages',
                                locale=settings.IEVVTASKS_MAKEMESSAGES_LANGUAGE_CODES,
                                ignore=ignore)
