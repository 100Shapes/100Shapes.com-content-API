from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page


class HomePage(Page):
    subpage_types = ['core.ContentPage', ]


class ContentPage(Page):
    subpage_types = ['core.ContentPage', ]

    subtitle = models.CharField(max_length=255)
    content = RichTextField()


ContentPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('subtitle', classname="full title"),
    FieldPanel('content', classname="full"),
]
