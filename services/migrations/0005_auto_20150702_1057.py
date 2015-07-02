# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20150702_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
    ]
