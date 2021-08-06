from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from omega_beats.omega_beats_auth.forms import RegisterUserForm, LoginUserForm, ProfileForm
from omega_beats.omega_beats_auth.models import Profile

UserModel = get_user_model()


class ProfilePageView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'common/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.pk == self.request.user.pk

        owner = UserModel.objects.get(pk=self.object.pk)
        context['beats'] = owner.beat_set.all()
        return context


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'common/edit_profile.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('profile page', args=(self.object.pk,))


class RegistrationUserView(CreateView):
    model = UserModel
    template_name = 'authentication/register.html'
    form_class = RegisterUserForm

    def get_success_url(self):
        return reverse_lazy('update profile', args=(self.object.pk,))

    # auto login after register:
    def form_valid(self, form):
        super().form_valid(form)
        form.save()

        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'], )
        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())


class LoginUserView(LoginView):
    template_name = 'authentication/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('browser page')


def logout_user(request):
    logout(request)
    return redirect('home page')
