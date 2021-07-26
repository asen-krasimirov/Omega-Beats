import json

import requests
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView
from omega_beats.api.models import BeatNotes, Beat
from omega_beats.beats.forms import RegisterBeatForm


def browser_page(request):
    return render(request, 'beats/browser.html')


class BrowserView(ListView):
    model = Beat
    context_object_name = 'beats'
    # ordering = ['-date_created']
    template_name = 'beats/browser.html'


def piano_page(request):
    return render(request, 'beats/piano_player.html')


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
    ).save()

    # return render(request, '')
    return redirect('create beat', pk=new_beat_notes.pk)


# def register_beat_page(request, pk):
#     beat = Beat.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         print(request.POST)
#         print(request.FILES)
#         data = request.POST
#         files = request.FILES
#         # form = PythonCreateForm(data, files)
#         form = RegisterBeatForm(data, files, instance=beat)
#         if form.is_valid():
#             form.save()
#             # return redirect('beat details', pk=pk) Todo: redirect to beat details or beat player
#             return redirect('browser page')
#     else:
#         form = RegisterBeatForm(instance=beat)
#
#     context = {
#         'form': form,
#     }
#
#     # form = BeatForm(instance=beat)
#     # ... Todo: save beat information and redirect to player/profile
#     return render(request, 'beats/create_beat.html', context)


class RegisterBeatView(UpdateView):
    model = Beat
    form_class = RegisterBeatForm
    template_name = 'beats/create_beat.html'
    success_url = reverse_lazy('browser page')
