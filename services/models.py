from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailapi.utils import get_base_url
from modelcluster.fields import ParentalKey
import os

from django.conf import settings


###################

# SERVICE SECTION

class ServiceSection(Orderable, models.Model):
    page = ParentalKey('services.Service', related_name='content_sections')
    body = models.TextField()
    label = models.CharField(max_length=100, help_text="What's displayed in the nav? i.e. \"Benefits\"")
    slug = models.SlugField(max_length=100)

    panels = [
        FieldPanel('label'),
        FieldPanel('slug'),
        FieldPanel('body'),
    ]




###################

# SERVICES

class Service(Page):

    lead = models.CharField(max_length=255)
    intro = RichTextField()

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

    is_featured = models.BooleanField(default=False)

    @property
    def thumbnail_url(self):
        return os.path.join(get_base_url(), self.thumbnail_image.get_rendition('original').url.strip(":/"))

    @property
    def banner_url(self):
        return os.path.join(get_base_url(), self.banner_image.get_rendition('original').url.strip(":/"))

    content_panels = Page.content_panels + [
        FieldPanel('lead', classname="full"),
        FieldPanel('intro', classname="full"),
        InlinePanel('content_sections', label="Content Sections"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        FieldPanel('is_featured'),
        ImageChooserPanel('thumbnail_image'),
        ImageChooserPanel('banner_image'),
    ]

    api_fields = (
        'thumbnail_url',
        'banner_url',
        'content_sections',
        'search_description',
        'slug',
        'label',
        'body',
        'lead',
        'intro',
        'seo_title',
        'is_featured'
    )
