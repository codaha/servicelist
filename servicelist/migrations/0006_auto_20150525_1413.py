# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicelist', '0005_remove_service_order2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('service_file', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='service_file',
            field=models.ForeignKey(to='servicelist.ServiceFile'),
        ),
    ]
