# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0010_siteconfiguration_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.CharField(default='url', max_length=64),
        ),
    ]
