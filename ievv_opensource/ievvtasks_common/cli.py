import argparse
import logging
import os
import sys

from sh import Command
import shutil
from ievv_opensource.ievvtasks_common.open_file import open_file_with_default_os_opener


documentation_directory = os.path.join('not_for_deploy', 'docs')
documentation_build_directory = os.path.join(documentation_directory, '_build')
documentation_indexhtml = os.path.join(documentation_build_directory, 'index.html')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] %(message)s')


def _opendocs(unknown_args):
    parser = argparse.ArgumentParser(
        description='Open docs')
    parser.parse_args(unknown_args)
    logging.info('Opening %s in your browser.', documentation_indexhtml)
    open_file_with_default_os_opener(documentation_indexhtml)


def _cleandocs(unknown_args):
    parser = argparse.ArgumentParser(
        description='Remove the build directory for docs.')
    parser.parse_args(unknown_args)
    if os.path.exists(documentation_build_directory):
        logging.info('Removing %s', documentation_build_directory)
        shutil.rmtree(documentation_build_directory)
    else:
        logging.info('Not removing %s - it does not exist.',
                     documentation_build_directory)


def _build_docs(unknown_args):
    parser = argparse.ArgumentParser(
        description='Build docs')
    parser.add_argument('-c', '--clean', dest='cleandocs',
                        required=False, action='store_true',
                        help='Remove any existing built docs before building the docs.')
    parser.add_argument('-o', '--open', dest='opendocs',
                        required=False, action='store_true',
                        help='Open the docs after building them.')
    args = parser.parse_args(unknown_args)

    if args.cleandocs:
        _cleandocs([])

    sphinx_build_html = Command('sphinx-build')
    sphinx_build_html(documentation_directory, documentation_build_directory,
                      b='html')
    logger.info('Built docs. Open %s in your browser to view them.',
                documentation_indexhtml)

    if args.opendocs:
        _opendocs([])


def cli():
    args = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description='IEVV command line interface.',
        # Do not include help unless we just run ``ievv --help`` or ``ievv``.
        # If we do not use this, we can not add help for the sub commands.
        add_help=len(args) <= 1)

    parser.add_argument('command', type=str,
                        help='The command to run. Use ``ievv <command> --help`` for '
                             'help with a specific command.',
                        choices=[
                            # 'createproject',
                            'docs',
                            'opendocs',
                            'cleandocs',
                            'recreate_devdb',
                            'remove_sorl_cache',
                            'dump_db_as_json',
                            'makemessages',
                            'compilemessages',
                        ])
    args, unknown_args = parser.parse_known_args()

    if args.command == 'docs':
        _build_docs(unknown_args)
    elif args.command == 'opendocs':
        _opendocs(unknown_args)
    elif args.command == 'cleandocs':
        _cleandocs(unknown_args)
    # elif args.command == 'createproject':
    #     # parser = argparse.ArgumentParser(
    #     #     description='Initialize a new project')
    #     # parser.add_argument('command', type=str)
    #     # args = parser.parse_args(unknown_args)
    #     raise SystemExit('Not implemented yet.')
    else:
        os.system('python manage.py ievvtasks_{} {}'.format(
            args.command, ' '.join(unknown_args)))
