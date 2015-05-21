# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150512_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pozwolenie',
            old_name='year_in_school',
            new_name='Uprawnienia',
        ),
    ]
