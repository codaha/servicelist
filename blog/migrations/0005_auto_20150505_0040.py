# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150504_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='usluga',
            name='opis',
            field=models.CharField(verbose_name='opisik', default='', max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usluga',
            name='kolejnosc',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
