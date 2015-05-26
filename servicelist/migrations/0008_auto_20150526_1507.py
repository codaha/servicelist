# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0007_auto_20150525_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
