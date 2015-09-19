from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tag(models.Model):
    """
    A single tag.

    A tag has a unique name, and data models is added to a tag via :class:`.TaggedItem`.
    """
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    #: The label for the tag.
    taglabel = models.CharField(
        verbose_name=_('Tag'),
        max_length=30,
        unique=True,
        help_text=_('Maximum 30 characters.')
    )

    #: The tagtype is a way for applications to group tags by type.
    #: No logic is assigned to this field by default, other than
    #: that is is ``db_indexed``.
    tagtype = models.CharField(
        max_length=255,
        db_index=True
    )


# class TaggedItem(models.Model):
#     tag = models.ForeignKey(Tag)
#     object_id = models.Posi
