import os

from core.forms import BootstrapForm
from django import forms
from django.conf import settings
from omega_beats.api.models import Beat


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

    def save(self, commit=True):
        beat_info = Beat.objects.get(pk=self.instance.pk)
        files = self.files

        try:
            cover_image_url = os.path.join(settings.MEDIA_ROOT[:-1], beat_info.cover_image.url[len('/media/'):])
            if commit and files:
                os.remove(cover_image_url)
        except (ValueError, FileNotFoundError):
            pass

        return super().save(commit)
