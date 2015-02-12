from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, \
    PageChooserPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.wagtailsnippets.models import register_snippet


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


# Navigation menu


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class NavigationMenuItem(Orderable, LinkFields):
    menu = ParentalKey(to='core.NavigationMenu', related_name='menu_items')
    menu_title = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="""Optional link title in this menu
            (defaults to page title if one exists)"""
    )
    css_class = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="CSS Class", help_text="Optional styling")

    @property
    def title(self):
        if self.menu_title:
            return self.menu_title

        if self.link_page:
            return self.link_page.title
        elif self.link_document:
            return self.link_document.title
        else:
            return self.link_external

    @property
    def url(self):
        return self.link

    def __unicode__(self):
        return self.title

    panels = [FieldPanel('menu_title'),
              FieldPanel('css_class')] + LinkFields.panels


class NavigationMenuManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(menu_name=name)


class NavigationMenu(models.Model):

    objects = NavigationMenuManager()
    menu_name = models.CharField(max_length=255, null=False, blank=False)

    def __unicode__(self):
        return self.menu_name


NavigationMenu.panels = [
    FieldPanel('menu_name', classname='full title'),
    InlinePanel(NavigationMenu, 'menu_items', label="Menu Items")
]

register_snippet(NavigationMenu)
