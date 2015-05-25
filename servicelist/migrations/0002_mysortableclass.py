# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySortableClass',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'ordering': ['order'],
            },
        ),
    ]
