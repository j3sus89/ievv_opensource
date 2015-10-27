import argparse
import logging
import os
import sys
import textwrap

import sh

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] %(message)s')
logging.getLogger('sh.command').setLevel(logging.WARNING)


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
    # commands.extend([
    # ])
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
    if len(args) == 0:
        parser.print_help()
    else:
        args, unknown_args = parser.parse_known_args()

        # if args.command == 'createproject':
        #     # parser = argparse.ArgumentParser(
        #     #     description='Initialize a new project')
        #     # parser.add_argument('command', type=str)
        #     # args = parser.parse_args(unknown_args)
        # else:
        os.system('python manage.py ievvtasks_{} {}'.format(
            args.command, ' '.join(unknown_args)))
