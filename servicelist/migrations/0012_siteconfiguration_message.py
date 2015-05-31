# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0011_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='message',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
