from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailapi.utils import get_base_url

from django.conf import settings


###################

# BLOG CATEGORIES

class BlogCategory(Page):
    description = models.TextField()

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    api_fields = (
        'title',
        'description',
    )

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

###################

# BLOG POSTS

import os

class BlogPost(Page):
    
    body = models.TextField()
    
    posted_at = models.DateField('Post date')
    
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        related_name="posts")
    
    category = models.ForeignKey('BlogCategory',
        on_delete=models.PROTECT,
        related_name="categories")
    
    lead = models.CharField(max_length=255)
    
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
        return os.path.join(get_base_url(), self.thumbnail_image.get_rendition('original').url.strip("/"))

    @property
    def banner_url(self):
        return os.path.join(get_base_url(), self.banner_image.get_rendition('original').url.strip("/"))

    @property
    def author(self):
        return self.posted_by.email

    @property
    def category_title(self):
        return self.category.title
    
    
    content_panels = Page.content_panels + [
        FieldPanel('lead', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('posted_by'),
        FieldPanel('posted_at'),
        FieldPanel('category'),
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
        'search_description',
        'slug',
        'lead',
        'posted_at',
        'author',
        'seo_title',
        'category_title',
        'category',
        'is_featured'
    )