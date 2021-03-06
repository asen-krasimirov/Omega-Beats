import cloudinary.uploader as uploader
from core.forms import BootstrapForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from omega_beats.omega_beats_auth.models import Profile


UserModel = get_user_model()


class RegisterUserForm(BootstrapForm, UserCreationForm):
    """
    Form used to get register the user.
    """

    class Meta:
        model = UserModel
        fields = ('email',)


class LoginUserForm(BootstrapForm, AuthenticationForm):
    """
    Form used to log in the user. The username is and EmailField.
    """

    username = forms.EmailField()


class ProfileForm(BootstrapForm, forms.ModelForm):
    """
    A form used to get user information for his profile.
    """

    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'avatar_image': forms.FileInput(
                attrs={
                    'class': 'main-button custom-field file',
                },
            )
        }

    def save(self, commit=True):
        """
        An extension to the default save() method which deletes the previous avatar image of the profile.
        """

        profile = Profile.objects.get(pk=self.instance.pk)
        files = self.files
        public_id = profile.avatar_image.public_id

        if commit and files and public_id:
            uploader.destroy(public_id)

        return super().save(commit)
