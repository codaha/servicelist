# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0009_siteconfiguration'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='mail',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
