from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailapi.utils import get_base_url
from modelcluster.fields import ParentalKey
import os

from django.conf import settings


###################

# LANDING_PAGE

class LandingPage(Page):

    lead = models.CharField(max_length=255)
    body = models.TextField()

    thumbnail_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def thumbnail_url(self):
        return os.path.join(get_base_url(), self.thumbnail_image.get_rendition('original').url.strip("/"))

    @property
    def banner_url(self):
        return os.path.join(get_base_url(), self.banner_image.get_rendition('original').url.strip("/"))

    content_panels = Page.content_panels + [
        FieldPanel('lead', classname="full"),
        FieldPanel('body', classname="full"),
    ]

    promote_panels = [
        FieldPanel('slug'),
        FieldPanel('search_description'),
        ImageChooserPanel('thumbnail_image'),
        ImageChooserPanel('banner_image'),
    ]

    api_fields = (
        'thumbnail_url',
        'banner_url',
        'search_description',
        'slug',
        'body',
        'lead'
    )
