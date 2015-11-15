# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_auto_20151115_0452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='address',
        ),
        migrations.AddField(
            model_name='details',
            name='full_address',
            field=models.CharField(default=b'', max_length=256),
        ),
    ]
