from django.urls import reverse
from omega_beats.beats.models import BeatNotes
from tests.base.mixins import BeatTestUtils, UserTestUtils
from tests.base.tests import OmegaBeatsTestCase


class BeatDetailsTests(OmegaBeatsTestCase, BeatTestUtils, UserTestUtils):

    def test_deleteBeat_whenOwnerIsLoggedIn_Succeeds(self):
        beat = self.create_beat(
            title='Title...',
            description='Description...',
            cover_image='cover/images/image.png',
            beat_notes=BeatNotes.objects.create(beat_notes={'note': 'test'}),
            owner=self.user,
        )

        self.client.force_login(self.user)
        post_response = self.client.post(reverse('delete beat', args=(beat.pk,)))
        self.assertRedirects(post_response, reverse('browser page'), status_code=302)

    def test_deleteBeat_whenOwnerIsNotLoggedIn_GetsRedirected(self):
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
        response = self.client.post(reverse('delete beat', args=(beat.pk,)))
        self.assertRedirects(response, reverse('beat details', args=(beat.pk,)), status_code=302)
