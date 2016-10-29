from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Genere(models.Model):
    genere = models.CharField(
        max_length=55,
        blank=False,
        null=False)

    def __str__(self):
        return self.genere


class Music(models.Model):
    genere = models.ForeignKey(
        Genere,
        blank=False,
        null=False)

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False)

    rating = models.IntegerField(
        blank=True,
        null=True)

    created_at = models.DateTimeField(
        auto_now_add=True)

    modified_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    music = models.ForeignKey(
        Music,
        related_name='music_track',
        default='',
        blank=False,
        null=False)

    user = models.ForeignKey(
        User,
        default='',
        blank=False,
        null=False)

    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        blank=True,
        null=True)

    created_at = models.DateTimeField(
        auto_now_add=True)

    modified_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return str(self.music.title)
