# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Published')),
                ('title', models.CharField(max_length=200)),
                ('instructions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient', models.CharField(max_length=255)),
                ('recipe', models.ForeignKey(related_name='ingredients', to='registration_app.Recipe')),
            ],
        ),
    ]
