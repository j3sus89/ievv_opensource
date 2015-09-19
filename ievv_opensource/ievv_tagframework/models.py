from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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


class TaggedItem(models.Model):
    """
    Represents a many-to-many relationship between any data model object and
    a :class:`.Tag`.
    """
    #: The :class:`.Tag`.
    tag = models.ForeignKey(Tag)

    #: The ContentType of the tagged object.
    content_type = models.ForeignKey(ContentType)

    #: The ID of the tagged object.
    object_id = models.PositiveIntegerField()

    #: The GenericForeignKey using :obj:`~TaggedItem.content_type` and
    #: :obj:`~TaggedItem.object_id` to create a generic foreign key
    #: to the tagged object.
    content_object = GenericForeignKey('content_type', 'object_id')
