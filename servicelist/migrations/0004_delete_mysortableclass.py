# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0003_auto_20150525_1258'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MySortableClass',
        ),
    ]
