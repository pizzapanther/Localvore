# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_place_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='placetype',
            name='slug',
            field=models.CharField(default='monkey', max_length=64),
            preserve_default=False,
        ),
    ]
