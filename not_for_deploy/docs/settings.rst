########
Settings
########


*************************
ievvtasks_dump_db_as_json
*************************

.. setting:: IEVVTASKS_DUMPDATA_DIRECTORY

IEVVTASKS_DUMPDATA_DIRECTORY
================================
The directory where we put dumps created by the ``ievvtasks_dump_db_as_json``
management command. Typically, you put something like this in your develop settings::

    THIS_DIR = os.path.dirname(__file__)

    IEVVTASKS_DUMPDATA_DIRECTORY = os.path.join(THIS_DIR, 'dumps')


.. setting:: IEVVTASKS_DUMPDATA_ADD_EXCLUDES

IEVVTASKS_DUMPDATA_ADD_EXCLUDES
===================================
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
===============================
If you do not want to get the default excludes, you can use this instead of
:setting:`IEVVTASKS_DUMPDATA_ADD_EXCLUDES` to specify exactly what to
exclude.


**********************
ievvtasks_makemessages
**********************


.. setting:: IEVVTASKS_MAKEMESSAGES_LANGUAGE_CODES

IEVVTASKS_MAKEMESSAGES_LANGUAGE_CODES
=========================================
The languages to build translations for. Example::

    IEVVTASKS_MAKEMESSAGES_LANGUAGE_CODES = ['en', 'nb']


.. setting:: IEVVTASKS_MAKEMESSAGES_IGNORE

IEVVTASKS_MAKEMESSAGES_IGNORE
=================================
The patterns to ignore when making translations. Defaults to::

    IEVVTASKS_MAKEMESSAGES_IGNORE = [
        'static/*'
    ]



*****************
ievv_tagframework
*****************


.. setting:: IEVV_TAGFRAMEWORK_TAGTYPE_CHOICES

IEVV_TAGFRAMEWORK_TAGTYPE_CHOICES
=================================
The legal values for :obj:`ievv_opensource.ievv_tagframework.models.Tag.tagtype`.
