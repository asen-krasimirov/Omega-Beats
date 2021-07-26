from django.db import models


# from django.contrib.postgres.fields import ArrayField


class BeatNotes(models.Model):
    beat_notes = models.JSONField()


class Beat(models.Model):
    title = models.CharField(
        max_length=100,
        null=True,
    )
    description = models.TextField(
        max_length=500,
        null=True,
    )

    cover_image = models.ImageField(
        upload_to='images',
        blank=True,
    )

    beat_notes = models.OneToOneField(
        BeatNotes,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    # owner = Todo: add owner/profile system

    # views = Todo: add views and likes system

    def __str__(self):
        return f'{self.pk}, {self.title}'
