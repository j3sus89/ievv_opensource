from django.core import management
from django.core.management.base import BaseCommand

from ievv_opensource.ievvtasks_development.management.commands.ievvtasks_dump_db_as_json import \
    get_dumpdata_filepath


class Command(BaseCommand):
    help = 'Recreate the database using django_dbdev migrate the database ' \
           'and load the json data dump created with ' \
           'ievvtasks_dump_devdb_as_json.'

    def handle(self, *args, **options):
        management.call_command('ievvtasks_remove_sorl_cache_media')
        management.call_command('dbdev_reinit')
        management.call_command('migrate')
        dumpdatafile = get_dumpdata_filepath()
        self.stdout.write('Loading data from {}.'.format(dumpdatafile))
        management.call_command('loaddata', dumpdatafile)
