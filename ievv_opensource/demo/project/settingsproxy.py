"""
A simple Django settings module proxy that lets us configure Django
using the DJANGOENV environment variable.

Example (running tests)::

    $ DJANGOENV=test python manage.py test

Defaults to the ``develop`` enviroment, so developers can use ``python
manage.py`` without anything extra during development.
"""
import os

DJANGOENV = os.environ.get('DJANGOENV', 'develop')

if DJANGOENV == 'develop':  # Used for local development
    from ievv_opensource.demo.project.develop.settings import *  # noqa
elif DJANGOENV == 'test':  # Used when running the Django tests
    from ievv_opensource.demo.project.test.settings import *  # noqa
else:
    raise ValueError('Invalid value for the DJANGOENV environment variable: {}'.format(DJANGOENV))
