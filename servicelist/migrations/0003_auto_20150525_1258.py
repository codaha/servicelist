# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0002_mysortableclass'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='service',
            name='order2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='order',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
        ),
    ]
