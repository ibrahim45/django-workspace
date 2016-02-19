from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=0)
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_descriptiion = 'ibrrahim'


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='question_choices')
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Rating(models.Model):
    rate = models.IntegerField()

    def __str__(self):
        return '%d' % self.id


class Book(models.Model):
    author = models.ForeignKey('Author')
    title = models.CharField(max_length=100)
    rate_book = models.ForeignKey('Rating')

    def __str__(self):
        return self.title

