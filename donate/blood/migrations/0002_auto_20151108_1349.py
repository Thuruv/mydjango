# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doorno', models.CharField(max_length=4)),
                ('street', models.CharField(max_length=55)),
                ('area', models.CharField(max_length=55)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='btype',
            field=models.CharField(blank=True, max_length=15, choices=[(b'O+', b'O-Positive'), (b'A+', b'A-Positive'), (b'O-', b'O-Negative'), (b'A-', b'A-Negative'), (b'B+', b'B-Positive'), (b'B-', b'B-Negative'), (b'AB+', b'AB-Positive'), (b'AB-', b'AB-Negative')]),
        ),
        migrations.AddField(
            model_name='details',
            name='address',
            field=models.ForeignKey(default=None, to='blood.Address'),
        ),
    ]
