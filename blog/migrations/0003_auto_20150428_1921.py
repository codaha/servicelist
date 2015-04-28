# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150428_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usluga',
            options={'verbose_name': 'usługa', 'verbose_name_plural': 'usługi'},
        ),
        migrations.AddField(
            model_name='usluga',
            name='plik_service',
            field=models.CharField(max_length=100, default='', verbose_name='nazwa pliku service'),
            preserve_default=False,
        ),
    ]
