# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0002_initial_data'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0003_contentpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NavigationMenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name=b'External link', blank=True)),
                ('menu_title', models.CharField(help_text=b'Optional link title in this menu\n            (defaults to page title if one exists)', max_length=255, null=True, blank=True)),
                ('css_class', models.CharField(help_text=b'Optional styling', max_length=255, null=True, verbose_name=b'CSS Class', blank=True)),
                ('link_document', models.ForeignKey(related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
                ('link_page', models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', null=True)),
                ('menu', modelcluster.fields.ParentalKey(related_name='menu_items', to='core.NavigationMenu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
