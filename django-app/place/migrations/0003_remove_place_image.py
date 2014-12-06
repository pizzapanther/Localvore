# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20141206_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='image',
        ),
    ]
