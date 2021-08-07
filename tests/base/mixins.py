from django.contrib.auth import get_user_model
from omega_beats.beats.models import Beat
from omega_beats.common.models import Comment, Like

UserModel = get_user_model()


class BeatTestUtils:

    @staticmethod
    def create_beat(**kwargs):
        return Beat.objects.create(**kwargs)


class UserTestUtils:

    @staticmethod
    def create_user(**kwargs):
        return UserModel.objects.create_user(**kwargs)


class CommentTestUtils:

    @staticmethod
    def create_comment(**kwargs):
        return Comment.objects.create(**kwargs)


class LikeTestUtils:

    @staticmethod
    def create_like(**kwargs):
        return Like.objects.create(**kwargs)
