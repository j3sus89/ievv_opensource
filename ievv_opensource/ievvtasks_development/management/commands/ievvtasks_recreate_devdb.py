import os
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

from ievv_opensource.ievvtasks_development.management.commands.ievvtasks_dump_db_as_sql import \
    get_dumpdata_filepath


class Command(BaseCommand):
    help = 'Recreate the database using django_dbdev migrate the database ' \
           'and load the json data dump created with ' \
           'ievvtasks_dump_devdb_as_sql.'

    def handle(self, *args, **options):
        management.call_command('ievvtasks_remove_sorl_cache_media')
        management.call_command('dbdev_reinit')
        dumpdatafile = get_dumpdata_filepath()
        if os.path.exists(dumpdatafile):
            self.stdout.write('Loading data from {}.'.format(dumpdatafile))
            management.call_command('dbdev_loaddump', dumpdatafile)
        self.stdout.write('Running management command: migrate.')
        management.call_command('migrate')
        post_management_commands = getattr(settings, 'IEVVTASKS_RECREATE_DEVDB_POST_MANAGEMENT_COMMANDS', [])
        for management_command in post_management_commands:
            if isinstance(management_command, dict):
                args = management_command.get('args', [])
                options = management_command.get('options', {})
                management_command = management_command['name']
            else:
                args = []
                options = {}
            self.stdout.write(
                'Running management command: {} with '
                'args={!r} and options={!r}.'.format(
                    management_command, args, options))
            management.call_command(management_command, *args, **options)
