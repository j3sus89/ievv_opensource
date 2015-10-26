import argparse
import logging
import os
import sys

import shutil
import textwrap
import sh
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

    sphinx_build_html = sh.Command('sphinx-build')
    output = sphinx_build_html(documentation_directory, documentation_build_directory,
                               b='html')
    print(output)
    logger.info('Built docs. Open %s in your browser to view them.',
                documentation_indexhtml)

    if args.opendocs:
        _opendocs([])


def _find_management_commands():
    commands = []
    try:
        pythoncommand = sh.Command('python')
    except sh.CommandNotFound:
        pass
    else:
        output = pythoncommand('manage.py', '--help')
        for line in output.split():
            line = line.strip()
            if line.startswith('ievvtasks_'):
                commands.append(line[len('ievvtasks_'):])
    return commands


def _make_cli_epilog(commands):
    cli_help = """
    Available commands:
      {}
    """.format('\n      '.join(commands))
    return cli_help


def cli():
    commands = _find_management_commands()
    commands.extend([
        'docs',
        'opendocs',
        'cleandocs',
    ])
    commands = list(set(commands))
    commands.sort()

    args = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description='IEVV command line interface.',
        epilog=textwrap.dedent(_make_cli_epilog(commands)),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # Do not include help unless we just run ``ievv --help`` or ``ievv``.
        # If we do not use this, we can not add help for the sub commands.
        add_help=len(args) <= 1)

    parser.add_argument('command', type=str,
                        metavar='command',
                        help='The command to run. Use ``ievv <command> --help`` for '
                             'help with a specific command. The available commands '
                             'is listed in the "Available commands" section below.',
                        choices=commands)
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
