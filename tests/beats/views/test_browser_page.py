from django.urls import reverse
from omega_beats.beats.models import BeatNotes
from tests.base.mixins import BeatTestUtils
from tests.base.tests import OmegaBeatsTestCase


class BrowserPageTests(OmegaBeatsTestCase, BeatTestUtils):

    def test_getBrowserPage_withBeats(self):
        beat = self.create_beat(
            title='Title...',
            description='Description...',
            cover_image='cover/images/image.png',
            beat_notes=BeatNotes.objects.create(beat_notes={'note': 'test'}),
            owner=self.user,
        )

        response = self.client.get(reverse('browser page'))
        self.assertListEqual([beat], list(response.context['beats']))

    def test_getBrowserPage_withoutBeats(self):
        response = self.client.get(reverse('browser page'))
        self.assertListEmpty(list(response.context['beats']))

    def test_searchBrowserPage_withMatches(self):
        beat = self.create_beat(
            title='Title...',
            description='Description...',
            cover_image='cover/images/image.png',
            beat_notes=BeatNotes.objects.create(beat_notes={'note': 'test'}),
            owner=self.user,
        )

        response = self.client.get(f'{reverse("browser page")}?beat_name=title')
        self.assertListEqual([beat], list(response.context['beats']))

    def test_searchBrowserPage_withoutMatches(self):
        self.create_beat(
            title='Title...',
            description='Description...',
            cover_image='cover/images/image.png',
            beat_notes=BeatNotes.objects.create(beat_notes={'note': 'test'}),
            owner=self.user,
        )

        response = self.client.get(f'{reverse("browser page")}?beat_name=something_random')
        self.assertListEmpty(list(response.context['beats']))
