# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_service_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('label', models.CharField(help_text=b'What\'s displayed in the nav? i.e. "Benefits"', max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('page', modelcluster.fields.ParentalKey(related_name='content_sections', to='services.Service')),
            ],
        ),
    ]
