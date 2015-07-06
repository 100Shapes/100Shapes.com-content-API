# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='related_posts',
            field=models.ManyToManyField(related_name='related_posts_rel_+', null=True, to='blog.BlogPost', blank=True),
        ),
    ]
