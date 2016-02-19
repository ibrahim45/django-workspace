# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0004_recipe_recipeingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.ForeignKey(to='registration_app.Author')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Bucket',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='widget',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.DeleteModel(
            name='RecipeIngredient',
        ),
        migrations.DeleteModel(
            name='Widget',
        ),
    ]
