# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20150702_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='intro',
            field=models.TextField(),
        ),
    ]
