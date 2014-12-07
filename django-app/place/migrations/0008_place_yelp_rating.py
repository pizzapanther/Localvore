# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0007_auto_20141207_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='yelp_rating',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
