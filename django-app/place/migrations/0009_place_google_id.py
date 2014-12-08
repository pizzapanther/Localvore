# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0008_place_yelp_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='google_id',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
    ]
