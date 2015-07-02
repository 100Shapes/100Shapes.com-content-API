# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_servicesection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicesection',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='servicesection',
            name='sort_order',
            field=models.IntegerField(null=True, editable=False, blank=True),
        ),
    ]
