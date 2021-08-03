from core.forms import BootstrapForm
from django import forms
from omega_beats.api.models import BeatNotes, Beat


class RegisterBeatForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Beat
        exclude = ('beat_notes', 'owner')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter 5-30 characters title...'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter 1-500 characters description...'
                }
            ),
            'cover_image': forms.FileInput(
                attrs={
                    'class': 'main-button custom-field file',
                },
            )
        }
