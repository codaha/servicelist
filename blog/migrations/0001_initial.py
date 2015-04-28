# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pozycja',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nazwa', models.CharField(max_length=100)),
                ('adres', models.URLField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
