from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from validators.beat_validators import first_latter_capital, no_bad_words

UserModel = get_user_model()


class BeatNotes(models.Model):
    beat_notes = models.JSONField()


class Beat(models.Model):
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

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.pk}, {self.title}'


class BeatPlay(models.Model):
    beat = models.ForeignKey(
        Beat,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.beat.title} play, {self.pk}'
