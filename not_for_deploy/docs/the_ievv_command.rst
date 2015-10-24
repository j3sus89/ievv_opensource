####################
The ``ievv`` command
####################

The ``ievv`` command does two things:

1. It avoids having to write ``python manange.py appressotaks_something`` and
   lets you write ``ievv something`` istead.
2. It provides commands that are not management commands, such as the commands
   for building docs and creating new projects.

When we add the command for initializing a new project, the ievv command will
typically be installed globally instead of as a requirement of each project.

You find the source code for the command in
``ievv_opensource/ievvtasks_common/cli.py``.


Some of the commands has required settings. See :doc:`settings`.
