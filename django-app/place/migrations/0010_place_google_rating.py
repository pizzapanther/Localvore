# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0009_place_google_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='google_rating',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
