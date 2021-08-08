from django.contrib.auth import get_user_model
from django.db import models
from omega_beats.beats.models import Beat


UserModel = get_user_model()


class Like(models.Model):
    liked_post = models.ForeignKey(
        Beat,
        on_delete=models.CASCADE,
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Comment(models.Model):
    content = models.CharField(
        max_length=85,
    )

    commented_post = models.ForeignKey(
        Beat,
        on_delete=models.CASCADE,
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
