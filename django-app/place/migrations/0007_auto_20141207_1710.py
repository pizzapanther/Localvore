# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_place_yelp_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='placetypes',
        ),
        migrations.AddField(
            model_name='place',
            name='placetype',
            field=models.ForeignKey(blank=True, to='place.PlaceType', null=True),
            preserve_default=True,
        ),
    ]
