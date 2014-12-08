# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0008_place_yelp_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='images',
            field=models.ManyToManyField(to='media.Image', null=True, blank=True),
            preserve_default=True,
        ),
    ]
