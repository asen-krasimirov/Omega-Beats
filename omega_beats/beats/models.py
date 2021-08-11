from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from validators.beat_validators import first_latter_capital, no_bad_words

from cloudinary import models as cloudinary_models


UserModel = get_user_model()


class BeatNotes(models.Model):
    """
    Data entity that stores the notes of the beat.
    """

    beat_notes = models.JSONField()


class Beat(models.Model):
    """
    The main data entity in the application.
    """

    title = models.CharField(
        max_length=30,
        null=True,
        validators=[
            MinLengthValidator(5),
            first_latter_capital,
            no_bad_words,
        ],
        unique=True,
    )

    description = models.TextField(
        max_length=500,
        null=True,
        validators=[
            no_bad_words
        ],
    )

    cover_image = cloudinary_models.CloudinaryField(
        resource_type='image',
        blank=True,
    )

    beat_notes = models.OneToOneField(
        BeatNotes,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.pk}, {self.title}'


class BeatPlay(models.Model):
    """
    Data entity which stores the notes of the beat.
    """

    beat = models.ForeignKey(
        Beat,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.beat.title} play, {self.pk}'
