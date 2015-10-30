########
Settings
########


*************************
ievvtasks_dump_db_as_json
*************************

.. setting:: IEVVTASKS_DUMPDATA_DIRECTORY

IEVVTASKS_DUMPDATA_DIRECTORY
============================
The directory where we put dumps created by the ``ievvtasks_dump_db_as_json``
management command. Typically, you put something like this in your develop settings::

    THIS_DIR = os.path.dirname(__file__)

    IEVVTASKS_DUMPDATA_DIRECTORY = os.path.join(THIS_DIR, 'dumps')


.. setting:: IEVVTASKS_DUMPDATA_ADD_EXCLUDES

IEVVTASKS_DUMPDATA_ADD_EXCLUDES
===============================
Use this setting to add models and apps to exclude from the dumped json. We exclude:

- contenttypes
- auth.Permission
- sessions.Session

By default, and we exclude ``thumbnail.KVStore`` by default if ``sorl.thumbnail`` is
in installed apps, and the ``THUMBNAIL_KVSTORE`` setting is configured to use the
database (``sorl.thumbnail.kvstores.cached_db_kvstore.KVStore``).

Example::

    IEVVTASKS_DUMPDATA_ADD_EXCLUDES = [
        'auth.Group',
        'myapp.MyModel',
    ]



.. setting:: IEVVTASKS_DUMPDATA_EXCLUDES

IEVVTASKS_DUMPDATA_EXCLUDES
===========================
If you do not want to get the default excludes, you can use this instead of
:setting:`IEVVTASKS_DUMPDATA_ADD_EXCLUDES` to specify exactly what to
exclude.


**********************
ievvtasks_makemessages
**********************


.. setting:: IEVVTASKS_MAKEMESSAGES_LANGUAGE_CODES

IEVVTASKS_MAKEMESSAGES_LANGUAGE_CODES
=====================================
The languages to build translations for. Example::

    IEVVTASKS_MAKEMESSAGES_LANGUAGE_CODES = ['en', 'nb']


.. setting:: IEVVTASKS_MAKEMESSAGES_IGNORE

IEVVTASKS_MAKEMESSAGES_IGNORE
=============================
The patterns to ignore when making translations. Defaults to::

    IEVVTASKS_MAKEMESSAGES_IGNORE = [
        'static/*'
    ]



**************
ievvtasks_docs
**************


.. setting:: IEVVTASKS_DOCS_DIRECTORY

IEVVTASKS_DOCS_DIRECTORY
========================
The directory where your sphinx docs resides (the directory where you have your sphinx ``conf.py``).
Defaults to ``not_for_deploy/docs/``.

.. setting:: IEVVTASKS_DOCS_BUILD_DIRECTORY

IEVVTASKS_DOCS_BUILD_DIRECTORY
==============================
The directory where your sphinx docs should be built.
Defaults to ``not_for_deploy/docs/_build``.



************************
ievvtasks_recreate_devdb
************************

.. setting:: IEVVTASKS_RECREATE_DEVDB_POST_MANAGEMENT_COMMANDS

IEVVTASKS_RECREATE_DEVDB_POST_MANAGEMENT_COMMANDS
=================================================
Iterable of managemement commands to after creating/restoring and migrating the
database in ``ievv recreate_devdb``. Example::

    IEVVTASKS_RECREATE_DEVDB_POST_MANAGEMENT_COMMANDS = [
        {
            'name': 'createsuperuser',
            'args': ['test@example.com'],
            'options': {'verbosity': 3}
        },
        'ievvtasks_set_all_passwords_to_test',
    ]

The items in the iterable can be one of:

- A string with the name of a management command (for commands without any
  arguments or options).
- A dict with ``name``, ``args``, and ``options`` keys. The
  ``name`` key is required, but ``args`` and ``options`` are
  optional. ``args`` and ``options`` is just forwarded to
  ``django.core.management.call_command``.


*****************
ievv_tagframework
*****************


.. setting:: IEVV_TAGFRAMEWORK_TAGTYPE_CHOICES

IEVV_TAGFRAMEWORK_TAGTYPE_CHOICES
=================================
The legal values for :obj:`ievv_opensource.ievv_tagframework.models.Tag.tagtype`.
