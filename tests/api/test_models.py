from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from omega_beats.api.models import Beat, BeatNotes

UserModel = get_user_model()


class BeatModelTests(TestCase):

    def setUp(self):
        self.beat = Beat(
            title='Correct',
            description='correct...',
        )

    def test_beatCreate_whenInvalidTitle_shouldRaise_1(self):
        self.beat.title = 'hello'

        with self.assertRaises(ValidationError) as error:
            self.beat.full_clean()
            self.beat.save()

        self.assertEquals(error.exception.messages[0], 'First latter must be upper!')

    def test_beatCreate_whenInvalidTitle_shouldRaise_2(self):
        self.beat.title = 'Hello, arse'

        with self.assertRaises(ValidationError) as error:
            self.beat.full_clean()
            self.beat.save()

        self.assertEquals(error.exception.messages[0], 'Do not use offensive words!')

    def test_beatCreate_whenInvalidDescription_shouldRaise(self):
        self.beat.description = 'arse...'

        with self.assertRaises(ValidationError) as error:
            self.beat.full_clean()
            self.beat.save()

        self.assertEquals(error.exception.messages[0], 'Do not use offensive words!')

    def test_beatCreate_whenValidTitleAndValidDescription_shouldCreateIt(self):
        beat_notes = BeatNotes(
            beat_notes={'note': 'test'}
        )

        owner = UserModel(
            email='test@test.test',
            password='TestAtTesting123',
        )

        beat_notes.save()
        owner.save()

        beat = Beat(
            title='Correct',
            description='correct...',
            beat_notes=beat_notes,
            owner=owner,
        )

        beat.full_clean()
        beat.save()

        self.assertIsNotNone(beat)
