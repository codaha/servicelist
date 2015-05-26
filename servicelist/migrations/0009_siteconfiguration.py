# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0008_auto_20150526_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('site_name', models.CharField(default='Project 2501', max_length=255)),
                ('allow_anonymous', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
    ]
