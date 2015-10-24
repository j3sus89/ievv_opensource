import json
import os
import tempfile
from django.conf import settings
from django.core import management
import shutil
from django.test import TestCase
from model_mommy import mommy


class TestDumpDbAsJson(TestCase):
    def __remove_dumpdata_directory(self):
        if os.path.exists(self.dumpdata_directory):
            shutil.rmtree(self.dumpdata_directory)

    def setUp(self):
        self.dumpdata_directory = tempfile.mkdtemp()
        self.dumpdata_file = os.path.join(self.dumpdata_directory, 'default.json')
        self.__remove_dumpdata_directory()

    def tearDown(self):
        self.__remove_dumpdata_directory()

    def test_dumpfile_created(self):
        self.assertFalse(os.path.exists(self.dumpdata_file))
        with self.settings(IEVVTASKS_DUMPDATA_DIRECTORY=self.dumpdata_directory):
            management.call_command('ievvtasks_dump_db_as_json')
        self.assertTrue(os.path.exists(self.dumpdata_file))
        dumped_data_list = json.load(open(self.dumpdata_file))
        self.assertEqual([], dumped_data_list)

    def test_dumpfile_includes_correct_data(self):
        mommy.make(settings.AUTH_USER_MODEL)
        with self.settings(IEVVTASKS_DUMPDATA_DIRECTORY=self.dumpdata_directory):
            management.call_command('ievvtasks_dump_db_as_json')
        dumped_data_list = json.load(open(self.dumpdata_file))
        self.assertEqual(1, len(dumped_data_list))

    def test_add_excludes(self):
        mommy.make(settings.AUTH_USER_MODEL)
        with self.settings(IEVVTASKS_DUMPDATA_DIRECTORY=self.dumpdata_directory,
                           IEVVTASKS_DUMPDATA_ADD_EXCLUDES=['auth.User']):
            management.call_command('ievvtasks_dump_db_as_json')
        dumped_data_list = json.load(open(self.dumpdata_file))
        self.assertEqual(0, len(dumped_data_list))

    def test_excludes(self):
        mommy.make(settings.AUTH_USER_MODEL)
        with self.settings(IEVVTASKS_DUMPDATA_DIRECTORY=self.dumpdata_directory,
                           IEVVTASKS_DUMPDATA_EXCLUDES=[
                               'contenttypes',
                               'auth.Permission',
                               'sessions.Session',
                               'auth.User',
                           ]):
            management.call_command('ievvtasks_dump_db_as_json')
        dumped_data_list = json.load(open(self.dumpdata_file))
        self.assertEqual(0, len(dumped_data_list))
