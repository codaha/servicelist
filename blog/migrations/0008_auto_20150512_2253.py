# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150512_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pozwolenie',
            name='department',
        ),
        migrations.AddField(
            model_name='pozwolenie',
            name='year_in_school',
            field=models.CharField(default='FR', choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], max_length=2),
        ),
    ]
