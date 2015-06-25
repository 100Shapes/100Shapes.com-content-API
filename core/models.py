from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, \
    PageChooserPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.wagtailsnippets.models import register_snippet


