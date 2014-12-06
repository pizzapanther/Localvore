# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
        ('place', '0003_remove_place_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ForeignKey(related_name='+', blank=True, to='media.Image', null=True),
            preserve_default=True,
        ),
    ]
