# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0003_auto_20151108_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='area',
        ),
        migrations.RemoveField(
            model_name='details',
            name='doorno',
        ),
        migrations.RemoveField(
            model_name='details',
            name='street',
        ),
        migrations.AddField(
            model_name='details',
            name='address',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
