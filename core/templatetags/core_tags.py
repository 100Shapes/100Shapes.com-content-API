from django import template
from wagtail.wagtailcore.models import Page

from core.models import NavigationMenu

register = template.Library()


@register.inclusion_tag('core/tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=1)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


@register.inclusion_tag('core/tags/primary-nav.html', takes_context=True)
def primary_nav(context):
    return {
        'menu': NavigationMenu.objects.get(menu_name="Primary Nav"),
        'request': context['request'],
    }
