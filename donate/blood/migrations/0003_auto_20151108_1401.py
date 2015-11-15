# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0002_auto_20151108_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='address',
        ),
        migrations.AddField(
            model_name='details',
            name='area',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='details',
            name='city',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='details',
            name='doorno',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AddField(
            model_name='details',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='details',
            name='fb',
            field=models.CharField(default=None, max_length=35),
        ),
        migrations.AddField(
            model_name='details',
            name='state',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='details',
            name='street',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='details',
            name='twitter',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
