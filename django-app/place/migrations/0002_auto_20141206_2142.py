# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='source_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ManyToManyField(related_name='+', null=True, to='media.Image', blank=True),
            preserve_default=True,
        ),
    ]
