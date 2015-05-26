# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0006_auto_20150525_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_file',
        ),
        migrations.AddField(
            model_name='servicefile',
            name='service',
            field=models.ForeignKey(to='servicelist.Service', default=3434),
            preserve_default=False,
        ),
    ]
