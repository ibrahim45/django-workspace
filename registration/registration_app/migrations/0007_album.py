# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0006_foo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=100)),
                ('release', models.DateField()),
                ('order', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
