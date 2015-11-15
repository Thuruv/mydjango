# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0005_auto_20151115_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
                ('current_url', models.URLField(max_length=4000, verbose_name='Current URL', blank=True)),
                ('message', models.TextField(max_length=4000, verbose_name='Message')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
    ]
