import cloudinary.uploader as uploader
from core.forms import BootstrapForm
from django import forms
from omega_beats.beats.models import Beat


class RegisterBeatForm(BootstrapForm, forms.ModelForm):
    """
    A form used to get user information for the registered beat.
    """

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
        """
        An extension to the default save() method which deletes the previous avatar image of the profile.
        """

        beat = Beat.objects.get(pk=self.instance.pk)
        files = self.files
        public_id = beat.cover_image.public_id

        if commit and files and public_id:
            uploader.destroy(public_id)

        return super().save(commit)
