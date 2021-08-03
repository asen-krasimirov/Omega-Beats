import json

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, TemplateView, DetailView
from omega_beats.api.models import BeatNotes, Beat, BeatPlay
from omega_beats.beats.forms import RegisterBeatForm
from omega_beats.omega_beats_auth.models import Profile


class BrowserView(ListView):
    model = Beat
    context_object_name = 'beats'
    # ordering = ['-date_created']
    template_name = 'beats/browser.html'


class PianoRecorder(LoginRequiredMixin, TemplateView):
    template_name = 'beats/piano_player.html'
    login_url = reverse_lazy('login user')

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def piano_beat_details_page(request, pk):
    song_details = requests.get(url=f'api/beat-details/{pk}/')

    context = {
        'beat': song_details,
    }

    return render(request, 'beats/piano_player.html', context)


def save_beat_notes_page(request):
    beat_notes_data = json.loads(request.POST['notesData'])

    new_beat_notes = BeatNotes(
        beat_notes=beat_notes_data,
    )

    new_beat_notes.save()

    Beat(
        beat_notes=new_beat_notes,
        owner=request.user,
    ).save()

    return redirect('create beat', pk=new_beat_notes.pk)


class RegisterBeatView(UpdateView):
    model = Beat
    form_class = RegisterBeatForm
    template_name = 'beats/create_beat.html'
    success_url = reverse_lazy('browser page')


class PianoPlayer(DetailView):
    model = Beat
    context_object_name = 'beat_info'
    template_name = 'beats/piano_player.html'

    def get(self, request, **kwargs):
        beat = Beat.objects.get(pk=kwargs['pk'])
        BeatPlay(
            beat=beat,
        ).save()
        return super().get(request, **kwargs)


class BeatDetails(DetailView):
    model = Beat
    context_object_name = 'beat'
    template_name = 'beats/details_beat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.object.owner.pk)
        return context
