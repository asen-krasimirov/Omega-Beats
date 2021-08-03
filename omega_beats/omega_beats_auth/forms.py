from core.forms import BootstrapForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from omega_beats.omega_beats_auth.models import Profile

UserModel = get_user_model()


class RegisterUserForm(BootstrapForm, UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class LoginUserForm(BootstrapForm, AuthenticationForm):
    username = forms.EmailField()


class ProfileForm(BootstrapForm, forms.ModelForm):
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
