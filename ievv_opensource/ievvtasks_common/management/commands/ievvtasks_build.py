from collections import OrderedDict
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand
import time
import logging
from os.path import dirname, abspath, join, isdir
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from fnmatch import fnmatch
import subprocess


# log = logging.getLogger('buildless')
# this_dir = abspath(dirname(__file__))
# lessc_path = [join(this_dir, 'bootstrap', 'less')]
#
#
# #: The map of *.less to *.css files.
# FILES = (
#         ('less/cultiva.less', 'css/cultiva.css'),
#         ('less/cultiva_tinymce.less', 'css/cultiva_tinymce.css'),
#         ('less/cultiva_ckeditor.less', 'css/cultiva_ckeditor.css'),
#         ('less/cultiva_adminextras.less', 'css/cultiva_adminextras.css'),
#         ('bootstrap/less/responsive.less', 'css/bootstrap_responsive.css')
#         )
#
#
# def lessc(folder, infile, outfile):
#     cmd = ['lessc', '--include-path={0}'.format(':'.join(lessc_path)), infile, outfile]
#     try:
#         subprocess.check_call(cmd, cwd=folder)
#     except subprocess.CalledProcessError as e:
#         log.exception('%s failed', ' '.join(cmd))
#     else:
#         log.info('Built %s successfully', outfile)
#
#
# def buildall(folder):
#     for infile, outfile in FILES:
#         lessc(folder, infile, outfile)
#
#
# class FSEvents(FileSystemEventHandler):
#     def __init__(self, folder):
#         self.folder = folder
#         super(FSEvents, self).__init__()
#
#     def on_any_event(self, event):
#         #diff = datetime.now() - self.last_event_time
#         #diff_sec = diff.total_seconds()
#         path = event.src_path
#         is_lessdirchange = isdir(path) and path.endswith('less') # NOTE: For PyCharm file change detection
#         if not is_lessdirchange and not fnmatch(path, '*.less'):
#             log.debug('Ignored %s because it is not a *.less file', path)
#             return
#         log.warn('Change detected in: %s', path)
#         buildall(self.folder)
#
#
# def watch(folder):
#     event_handler = FSEvents(folder)
#     observer = Observer()
#     log.info('Watching for changes to *.less files in %s', folder)
#     observer.schedule(event_handler, folder, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(0.3)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
#
#
# if __name__ == '__main__':
#     import sys
#
#     logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
#     folder = this_dir
#     log.info('Using %s as CWD for ``lessc``.', folder)
#     buildall(folder)
#
#     if len(sys.argv) == 2:
#         if sys.argv[1] == 'watch':
#             watch(folder)
#         else:
#             raise SystemExit('usage: {} [watch]'.format(sys.argv[0]))


class Command(BaseCommand):
    help = 'A build system (for less, coffeescript, ...).'

    def handle(self, *args, **options):
        settings.IEVVTASKS_BUILD_APPS.configure_logging()
        settings.IEVVTASKS_BUILD_APPS.install()
        settings.IEVVTASKS_BUILD_APPS.run()
