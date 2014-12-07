# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_placetype_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='yelp_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
