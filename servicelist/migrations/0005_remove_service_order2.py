# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0004_delete_mysortableclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='order2',
        ),
    ]
