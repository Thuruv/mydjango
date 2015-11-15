# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0006_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='current_url',
        ),
    ]
