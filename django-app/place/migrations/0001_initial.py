# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('media', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('geopoint', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('geomodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='place.GeoModel')),
            ],
            options={
            },
            bases=('place.geomodel',),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('geomodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='place.GeoModel')),
                ('address', models.CharField(max_length=128)),
                ('zipcode', models.CharField(max_length=16)),
                ('url', models.URLField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('city', models.ForeignKey(to='place.City')),
                ('image', models.ManyToManyField(related_name='+', to='media.Image')),
                ('images', models.ManyToManyField(to='media.Image')),
            ],
            options={
            },
            bases=('place.geomodel',),
        ),
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='place',
            name='placetypes',
            field=models.ManyToManyField(to='place.PlaceType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='source',
            field=models.ManyToManyField(to='place.Source'),
            preserve_default=True,
        ),
    ]
