import datetime
import markdown

from django.db import models
from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern
from bs4 import BeautifulSoup


#: Pattern which recognise dates with the format: 25.01.89
DATE_RE = r'(^|(\d{2}\.\d{2}\.\d{2}))\n'

#: Pattern which recognise hours and minutes with the format: 16:45
TIME_RE = r'(^|(\d{2}\:\d{2}))\n'

#: Pattern which recognise the place of the events.
PLACE_RE = r'(\@)(.*?)(\n)'


class ExtendedExtension(Extension):
    """
    This class inherites Extension class from Markdown and extends its functionality.
    """

    def extendMarkdown(self, md, md_globals):
        """
        The function which adds new patterns to be recognized.
        """
        date_tag = SimpleTagPattern(DATE_RE, 'date')
        md.inlinePatterns.add('date', date_tag, '>not_strong')
        hour_tag = SimpleTagPattern(TIME_RE, 'hour')
        md.inlinePatterns.add('hour', hour_tag, '>not_strong')
        place_tag = SimpleTagPattern(PLACE_RE, 'place')
        md.inlinePatterns.add('place', place_tag, '>not_strong')


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
        parsed_text_area = markdown.markdown(text_area, entensions=[ExtendedExtension()])
        parsed_html = BeautifulSoup(parsed_text_area, "html.parser")
        ev = Event.create(parsed_html.find('h1').text,
                          parsed_html.find_all('p')[1].text,
                          parsed_html.find('date').text,
                          parsed_html.find('hour').text,
                          parsed_html.find('place').text,
                          parsed_html.find('a').text)
        return ev