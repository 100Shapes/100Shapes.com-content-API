# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='banner_image',
            field=modelcluster.fields.ParentalKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=modelcluster.fields.ParentalKey(related_name='categories', on_delete=django.db.models.deletion.PROTECT, to='blog.BlogCategory'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='posted_at',
            field=models.DateField(verbose_name=b'Post date'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='posted_by',
            field=modelcluster.fields.ParentalKey(related_name='posts', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail_image',
            field=modelcluster.fields.ParentalKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
    ]
