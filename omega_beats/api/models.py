from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models


class BeatNotes(models.Model):
    beat_notes = models.JSONField()


class Beat(models.Model):
    title = models.CharField(
        max_length=30,
        null=True,
        validators=[
            MinLengthValidator(5),
        ],
    )
    description = models.TextField(
        max_length=500,
        null=True,
    )

    cover_image = models.ImageField(
        upload_to='covers',
        blank=True,
        # default=settings.BASE_DIR / 'static/images/default_cover.jpg',
    )

    beat_notes = models.OneToOneField(
        BeatNotes,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    # owner = Todo: add owner/profile system

    # likes = Todo: add views and likes system

    def __str__(self):
        return f'{self.pk}, {self.title}'


class BeatPlay(models.Model):
    beat = models.ForeignKey(
        Beat,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.beat.title} play, {self.pk}'
