"""dddppp models for slides."""

from dddp.models import AleaIdMixin, meteor_random_id
from django.conf import settings
from django.db import models
from django.utils import timezone, module_loading
from django.utils.encoding import python_2_unicode_compatible
from mptt.models import MPTTModel
from orderable.models import Orderable


@python_2_unicode_compatible
class Presentation(AleaIdMixin, models.Model):

    """Presentation database model."""

    class PublicationState(object):

        """Publication state enumeration."""

        DRAFT = 'draft'
        PUBLIC = 'public'
        PRIVATE = 'private'

    PUBLICATION_STATE_CHOICES = [
        (PublicationState.DRAFT, 'Draft'),
        (PublicationState.PUBLIC, 'Public'),
        (PublicationState.PRIVATE, 'Private'),
    ]

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    publication_state = models.CharField(
        max_length=10, choices=PUBLICATION_STATE_CHOICES,
        default=PublicationState.DRAFT,
    )
    authors = models.ManyToManyField('auth.User', related_name='presentations')
    invited = models.ManyToManyField('auth.User', blank=True, related_name='+')

    def __str__(self):
        return self.title


class Slide(AleaIdMixin, Orderable):

    """Presentation Slide database model."""

    CONTENT_TYPE_CHOICES = [
        (content_type.mimetype, content_type.name)
        for content_type in (
            module_loading.import_string(name)
            for name in sorted(settings.DDDPPP_CONTENT_TYPES)
        )
    ]

    publication = models.ForeignKey('Presentation')
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES)
    notes = models.TextField(blank=True)
    notes_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES)


class PresentationRole(AleaIdMixin, models.Model):

    """Presentation role database model."""

    presentation = models.ForeignKey('Presentation')
    user = models.ForeignKey('auth.User')

    can_present = models.BooleanField(default=False)
    can_modify = models.BooleanField(default=False)
    can_review = models.BooleanField(default=False)
    can_moderate = models.BooleanField(default=False)
    can_mix = models.BooleanField(default=False)


class Session(AleaIdMixin, models.Model):

    """Presentation session database model."""

    class ViewState(object):

        """Session view state enumeration."""

        PENDING = 'pending'
        LIVE = 'live'
        PAUSED = 'paused'
        PROBLEM = 'problem'
        BREAK = 'break'
        FORUM = 'forum'
        CLOSED = 'closed'

    VIEW_STATE_CHOICES = [
        (ViewState.PENDING, 'Pending'),
        (ViewState.LIVE, 'Live'),
        (ViewState.PAUSED, 'Paused'),
        (ViewState.PROBLEM, 'Problem'),
        (ViewState.BREAK, 'Break'),
        (ViewState.FORUM, 'Forum'),
        (ViewState.CLOSED, 'Closed'),
    ]

    presentation = models.ForeignKey('Presentation')
    view_state = models.CharField(
        max_length=10, default=ViewState.PENDING,
    )
    current_slide = models.ForeignKey('Slide', blank=True, null=True)
    present = models.ManyToManyField('auth.User', blank=True)
