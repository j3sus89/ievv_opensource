from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


# def get_tagtype_choices():
#     return settings.IEVV_TAGFRAMEWORK_TAGTYPE_CHOICES


class Tag(models.Model):
    """
    A single tag.

    A tag has a unique name, and data models is added to a tag via :class:`.TaggedObject`.
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
    #: that is is ``db_indexed``. The valid choices for the field
    #: is configured via the
    #: :obj:`~ievv_opensource.project.default.projectspecific_settings.IEVV_TAGFRAMEWORK_TAGTYPE_CHOICES`
    #: setting.
    tagtype = models.CharField(
        max_length=255,
        db_index=True,
        # choices=get_tagtype_choices
    )


class TaggedObject(models.Model):
    """
    Represents a many-to-many relationship between any data model object and
    a :class:`.Tag`.
    """
    class Meta:
        verbose_name = _('Tagged object')
        verbose_name_plural = _('Tagged objects')

    #: The :class:`.Tag`.
    tag = models.ForeignKey(Tag)

    #: The ContentType of the tagged object.
    content_type = models.ForeignKey(ContentType)

    #: The ID of the tagged object.
    object_id = models.PositiveIntegerField()

    #: The GenericForeignKey using :obj:`~TaggedObject.content_type` and
    #: :obj:`~TaggedObject.object_id` to create a generic foreign key
    #: to the tagged object.
    content_object = GenericForeignKey('content_type', 'object_id')
