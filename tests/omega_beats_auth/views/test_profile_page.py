from django.urls import reverse
from omega_beats.beats.models import BeatNotes
from tests.base.mixins import BeatTestUtils, UserTestUtils
from tests.base.tests import OmegaBeatsTestCase


class ProfilePageTests(OmegaBeatsTestCase, BeatTestUtils, UserTestUtils):

    def test_getProfile_whenOwnerIsLoggedInWithoutBeats_shouldReturnOwnerData(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile page', args=(self.user.pk,)))

        self.assertTrue(response.context['is_owner'])
        self.assertListEmpty(list(response.context['beats']))

    def test_getProfile_whenOwnerIsLoggedInWithBeats_shouldReturnOwnerData(self):
        beat = self.create_beat(
            title='Title...',
            description='Description...',
            cover_image='cover/images/image.png',
            beat_notes=BeatNotes.objects.create(beat_notes={'note': 'test'}),
            owner=self.user,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('profile page', args=(self.user.pk,)))

        self.assertTrue(response.context['is_owner'])
        self.assertListEqual([beat], list(response.context['beats']))

    def test_getProfile_whenOwnerIsNotLoggedIn_shouldReturnListenerData(self):
        random_user = self.create_user(
            email='random@random.random',
            password='random'
        )

        self.client.force_login(random_user)
        response = self.client.get(reverse('profile page', args=(self.user.pk,)))

        self.assertFalse(response.context['is_owner'])
