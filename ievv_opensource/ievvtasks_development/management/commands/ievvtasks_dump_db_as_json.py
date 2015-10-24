import os

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand


def get_dumpdata_filepath():
    return os.path.join(settings.IEVVTASKS_DUMPDATA_DIRECTORY,
                        'default.json')


class Command(BaseCommand):
    help = 'Dump the development database as json.'

    def handle(self, *args, **options):
        if hasattr(settings, 'IEVVTASKS_DUMPDATA_EXCLUDES'):
            dumpdata_excludes = settings.IEVVTASKS_DUMPDATA_EXCLUDES
        else:
            dumpdata_excludes = {
                'contenttypes',
                'auth.Permission',
                'sessions.Session',
            }
            if hasattr(settings, 'IEVVTASKS_DUMPDATA_ADD_EXCLUDES'):
                dumpdata_excludes.update(set(settings.IEVVTASKS_DUMPDATA_ADD_EXCLUDES))

            # We automatically exclude the sorl-thumbnail KVStore table if it is
            # in use.
            if 'sorl.thumbnail' in settings.INSTALLED_APPS \
                    and 'cached_db_kvstore' in getattr(settings, 'THUMBNAIL_KVSTORE', ''):
                dumpdata_excludes.add('thumbnail.KVStore')
        dumpdata_excludes = list(dumpdata_excludes)

        outfile = get_dumpdata_filepath()
        if not os.path.exists(settings.IEVVTASKS_DUMPDATA_DIRECTORY):
            os.makedirs(settings.IEVVTASKS_DUMPDATA_DIRECTORY)
        management.call_command('dumpdata',
                                indent=2,
                                exclude=dumpdata_excludes,
                                output=outfile)
        self.stdout.write('Dumped the database into {}, excluding {}'.format(
            outfile, dumpdata_excludes))
