from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.conf import settings


###################

# BLOG CATEGORIES

class BlogCategory(models.Model):
    category = models.CharField(max_length=20)

    def __unicode__(self):
        return self.category

    class Meta:
        verbose_name_plural = "categories"

    api_fields = (
        'category',
    )



###################

# BLOG AUTHORS

class BlogAuthor(Page):
    email = models.EmailField()

    @property
    def name(self):
        return self.title
    
    panels = [
        FieldPanel('email', classname="full"),
    ]

    api_fields = (
        'name',
        'email',
    )
 

###################

# BLOG POSTS

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
    def get_thumbnail_url(self):
        return self.thumbnail_image.get_rendition('original').url

    @property
    def get_banner_url(self):
        return self.banner_image.get_rendition('original').url

    @property
    def get_category(self):
        return self.category.category

    @property
    def get_author(self):
        return self.posted_by.email
    
    
    
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('lead', classname="full"),
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
        'get_thumbnail_url',
        'get_banner_url',
        'body',
        'lead',
        'posted_at',
        'get_author',
        'get_category',
        'is_featured'
    )