from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Foo(models.Model):
    bar = models.DurationField()


class Album(models.Model):
    artist = models.CharField(max_length=75)
    name = models.CharField(max_length=100)
    release = models.DateField()
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.artist
