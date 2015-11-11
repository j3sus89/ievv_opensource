from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern


#: Pattern which recognise dates with the format: 25.01.89
DATE_RE = r'(^|(\d{2}\.\d{2}\.\d{2}))(\n)'

#: Pattern which recognise hours and minutes with the format: 16:45
TIME_RE = r'(^|(\d{2}\:\d{2}))(\n)'

#: Pattern which recognise the place of the events.
PLACE_RE = r'(\@)(.*?)(\n)'


class MyExtension(Extension):
    """
    This class inherites Extension class from Markdown and extends its functionality.
    """
    def extendMarkdown(self, md, md_globals):
        date_tag = SimpleTagPattern(DATE_RE, 'date')
        md.inlinePatterns.add('date', date_tag, '>not_strong')
        hour_tag = SimpleTagPattern(TIME_RE, 'hour')
        md.inlinePatterns.add('hour', hour_tag, '>not_strong')
        place_tag = SimpleTagPattern(PLACE_RE, 'place')
        md.inlinePatterns.add('place', place_tag, '>not_strong')


def makeExtension(*args, **kwargs):
    return MyExtension(*args, **kwargs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()