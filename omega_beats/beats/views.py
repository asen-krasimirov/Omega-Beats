import json
import os

from core.views import is_post_liked
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, ListView, TemplateView, DetailView
from omega_beats.beats.forms import RegisterBeatForm
from omega_beats.beats.models import Beat, BeatNotes, BeatPlay
from omega_beats.omega_beats_auth.models import Profile


class BrowserView(ListView):
    model = Beat
    context_object_name = 'beats'
    # ordering = ['-date_created']
    template_name = 'beats/browser.html'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('beat_name')

        if query:
            object_list = Beat.objects.filter(
                title__icontains=query,
            )
        else:
            object_list = Beat.objects.all()

        return object_list[::-1]


class PianoRecorder(LoginRequiredMixin, TemplateView):
    template_name = 'beats/piano_player.html'
    login_url = reverse_lazy('login user')

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner = self.object.owner

        context['owner_profile'] = Profile.objects.get(pk=owner.pk)

        return context


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

    def get_success_url(self):
        return reverse_lazy('beat details', args=(self.object.pk,))


class EditBeatView(UpdateView):
    model = Beat
    form_class = RegisterBeatForm
    template_name = 'beats/edit_beat.html'

    def get_success_url(self):
        return reverse('beat details', args=(self.object.pk,))


class BeatDetails(DetailView):
    model = Beat
    context_object_name = 'beat'
    template_name = 'beats/details_beat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        beat = self.object

        context['profile'] = Profile.objects.get(pk=beat.owner.pk)
        context['is_liked'] = is_post_liked(beat.like_set.all(), self.request.user)
        context['is_owner'] = beat.owner.pk == self.request.user.pk

        context['comments'] = []
        for comment in beat.comment_set.all()[::-1]:
            commenter_profile = Profile.objects.get(pk=comment.owner.pk)

            comment_info = {
                'commenter_info': commenter_profile,
                'content': comment.content,
            }

            context['comments'].append(comment_info)

        return context


def delete_beat(request, pk):
    beat = Beat.objects.get(pk=pk)
    beat_notes = beat.beat_notes

    if request.user.pk != beat.owner.pk:
        return redirect('beat details', beat.pk)

    if beat.cover_image:
        cover_image_url = os.path.join(settings.MEDIA_ROOT[:-1], beat.cover_image.url[len('/media/'):])
        if os.path.exists(cover_image_url):
            os.remove(cover_image_url)

    beat.delete()
    beat_notes.delete()

    return redirect('browser page')
