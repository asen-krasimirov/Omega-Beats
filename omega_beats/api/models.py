from django.db import models
from django.contrib.postgres.fields import ArrayField


class Beat(models.Model):
    title = models.CharField(
        max_length=30,
    )
    description = models.TextField(
        max_length=300,
    )

    def __str__(self):
        return f'{self.pk}, {self.title}'


# class BeatNotes(models.Model):
    # notes = ArrayField(

    # )