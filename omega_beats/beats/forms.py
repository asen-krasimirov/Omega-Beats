from core.forms import BootstrapForm
from django import forms
from omega_beats.api.models import BeatNotes, Beat


class RegisterBeatForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Beat
        exclude = ('beat_notes',)
        widgets = {
            'title': forms.TextInput(
            ),
            'description': forms.Textarea(
            ),
            'cover_image': forms.FileInput(
                attrs={
                    'class': 'main-button custom-field file',
                },
            )
        }
