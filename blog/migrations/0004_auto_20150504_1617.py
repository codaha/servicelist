# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150428_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='usluga',
            name='kolejnosc',
            field=models.IntegerField(default='0000000'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usluga',
            name='adres',
            field=models.URLField(verbose_name='adres URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usluga',
            name='plik_service',
            field=models.CharField(verbose_name='nazwa pliku service', blank=True, max_length=100),
            preserve_default=True,
        ),
    ]
