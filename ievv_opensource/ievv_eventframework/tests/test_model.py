import datetime

from django.test import TestCase
from model_mommy import mommy
from django.db import IntegrityError, OperationalError

from ievv_opensource.ievv_eventframework.models import Event


class TestEventModel(TestCase):

    def test_create_event_with_title_ok(self):
        event = mommy.make(Event, title='Event test')
        self.assertEqual('Event test', event.title)

    def test_create_event_without_title_fail(self):
        with self.assertRaises(IntegrityError):
            mommy.make(Event, title=None)

    def test_create_event_with_description_ok(self):
        event = mommy.make(Event, description='Description example')
        self.assertEqual('Description example', event.description)

    def test_create_event_without_description_fail(self):
        with self.assertRaises(IntegrityError):
            mommy.make(Event, description=None)

    def test_create_event_with_location_ok(self):
        event = mommy.make(Event, location='Location example')
        self.assertEqual('Location example', event.location)

    def test_create_event_without_location_fail(self):
        with self.assertRaises(IntegrityError):
            mommy.make(Event, location=None)

    def test_create_event_with_website_ok(self):
        event = mommy.make(Event, website='www.example.no')
        self.assertEqual('www.example.no', event.website)

    def test_create_event_without_website_fail(self):
        with self.assertRaises(IntegrityError):
            mommy.make(Event, website=None)

    def test_create_event_with_start_datetime_ok(self):
        event = mommy.make(Event, start_datetime=datetime.date.today())
        self.assertEqual(datetime.date.today(), event.start_datetime)

    def test_create_function_ok(self):
        event = mommy.make(Event).create("title", "description", "22.12.16", "15:32", "location", "website")
        self.assertEqual(event.title, "title")
        self.assertEqual(event.description, "description")
        self.assertEqual(event.location, "location")
        self.assertEqual(event.website, "website")
        self.assertEqual(event.start_datetime, datetime.datetime.combine(datetime.date(2016, 12, 22),
                                                                         datetime.time(15, 32)))

    ### What about the tests when the create function fails? Talk to Magne about this