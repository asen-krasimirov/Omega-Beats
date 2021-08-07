from django.urls import reverse
from omega_beats.beats.models import BeatNotes
from omega_beats.omega_beats_auth.models import Profile
from tests.base.mixins import BeatTestUtils, UserTestUtils, CommentTestUtils, LikeTestUtils
from tests.base.tests import OmegaBeatsTestCase


class BeatDetailsTests(OmegaBeatsTestCase, BeatTestUtils, UserTestUtils, CommentTestUtils, LikeTestUtils):

    def test_getBeatDetails_whenBeatDoesNotExists_shouldReturnStatus404(self):
        response = self.client.get(reverse('beat details', args=(100,)))

        self.assertEquals(404, response.status_code)

    def test_getBeatDetails_whenBeatExistsAndIsOwner_shouldReturnDetailsForOwner(self):
        beat = self.create_beat(
            title='Title...',
            description='Description...',
            cover_image='cover/images/image.png',
            beat_notes=BeatNotes.objects.create(beat_notes={'note': 'test'}),
            owner=self.user,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('beat details', args=(beat.pk,)))

        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])
        self.assertEqual(self.user.pk, response.context['profile'].pk)

    def test_getBeatDetails_whenBeatExistsAndIsNotOwnerAndNotLiked_shouldReturnDetailsForNotLikedListener(self):
        random_user = self.create_user(
            email='random@random.random',
            password='random'
        )

        beat = self.create_beat(
            title='Title...',
            description='Description...',
            cover_image='cover/images/image.png',
            beat_notes=BeatNotes.objects.create(beat_notes={'note': 'test'}),
            owner=random_user,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('beat details', args=(beat.pk,)))

        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])
        self.assertNotEqual(self.user.pk, response.context['profile'].pk)

    def test_getBeatDetails_whenBeatExistsAndIsNotOwnerAndIsLiked_shouldReturnDetailsForLikedListener(self):
        random_user = self.create_user(
            email='random@random.random',
            password='random'
        )

        beat = self.create_beat(
            title='Title...',
            description='Description...',
            cover_image='cover/images/image.png',
            beat_notes=BeatNotes.objects.create(beat_notes={'note': 'test'}),
            owner=random_user,
        )

        self.create_like(
            liked_post=beat,
            owner=self.user,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('beat details', args=(beat.pk,)))

        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])
        self.assertNotEqual(self.user.pk, response.context['profile'].pk)

    def test_getBeatDetails_whenBeatExistsAndIsOwnerAndHasNoComments_shouldReturnDetailsForOwner(self):
        beat = self.create_beat(
            title='Title...',
            description='Description...',
            cover_image='cover/images/image.png',
            beat_notes=BeatNotes.objects.create(beat_notes={'note': 'test'}),
            owner=self.user,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('beat details', args=(beat.pk,)))

        self.assertListEmpty(response.context['comments'])

    def test_getBeatDetails_whenBeatExistsAndIsOwnerAndHasComments_shouldReturnDetailsForOwner(self):
        beat = self.create_beat(
            title='Title...',
            description='Description...',
            cover_image='cover/images/image.png',
            beat_notes=BeatNotes.objects.create(beat_notes={'note': 'test'}),
            owner=self.user,
        )

        comment = self.create_comment(
            content='Hello...',
            commented_post=beat,
            owner=self.user,
        )

        commenter_profile = Profile.objects.get(pk=comment.owner.pk)

        comment_info = {
            'commenter_info': commenter_profile,
            'content': comment.content,
        }

        self.client.force_login(self.user)
        response = self.client.get(reverse('beat details', args=(beat.pk,)))

        self.assertListEqual([comment_info], response.context['comments'])
