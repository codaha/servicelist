# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150512_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pozwolenie',
            name='Uprawnienia',
            field=models.CharField(max_length=2, default='Us', choices=[('Ad', 'Admin'), ('Us', 'Uzytkownik')]),
        ),
    ]
