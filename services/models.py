from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.conf import settings


###################

# BLOG POSTS

class Service(Page):
    
    body = models.TextField()
    
    lead = models.CharField(max_length=255)
    intro = models.CharField(max_length=255)
    
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
        return self.thumbnail_image.get_rendition('original').url

    @property
    def banner_url(self):
        return self.banner_image.get_rendition('original').url


    content_panels = Page.content_panels + [
        FieldPanel('lead', classname="full"),
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full"),
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
        'body',
        'slug',
        'lead',
        'intro',
        'seo_title',
        'is_featured'
    )