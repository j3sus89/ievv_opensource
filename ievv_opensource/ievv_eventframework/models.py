import datetime
import markdown

from django.db import models
from ievv_opensource.ievv_eventframework.myextension import MyExtension
from bs4 import BeautifulSoup


class Event(models.Model):
    """
    This class represents the events.
    """

    #: The title for the event.
    title = models.CharField(max_length=255, null=False)

    #: The description shows what the event is about.
    description = models.TextField(null=False, blank=True, default='')

    #: The date and hour for the event.
    start_datetime = models.DateTimeField(null=True, blank=True)

    #: The place where the event is taking place.
    location = models.CharField(max_length=255, null=False, blank=True)

    #: The event's website.
    website = models.CharField(max_length=255, null=False, blank=True)

    @classmethod
    def create(cls, title, description, date, time, location, website):
        event = cls(title=title,
                    description=description,
                    location=location,
                    website=website,
                    start_datetime=datetime.datetime.combine(datetime.date(int("20" + date.split(".")[2]),
                                                                           int(date.split(".")[1]),
                                                                           int(date.split(".")[0])),
                                                             datetime.time(int(time.split(":")[0]),
                                                                           int(time.split(":")[1]))))
        return event

    def __str__(self):
        """
        This is the string function for Event class.
        """
        print(
            self.title + ". " + self.description + ". " + self.location + ". " + self.website + ". " + self.start_datetime)

    def add_event(self, text_area):
        """
        This functions gets the data from the text string and makes an event.
        """
        parsed_text_area = markdown.markdown(text_area, entensions=[MyExtension()])
        print(parsed_text_area)
        parsed_html = BeautifulSoup(parsed_text_area, "html.parser")
        print("LO QUE DEVUELVE: "+str(parsed_html))
        ev = Event.create(parsed_html.find('h1').text,
                          parsed_html.find_all('p')[1].text,
                          parsed_html.find('date').text,
                          parsed_html.find('hour').text,
                          parsed_html.find('place').text,
                          parsed_html.find('a').text)
        return ev