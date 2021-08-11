import json

import cloudinary.uploader as uploader
from core.views import is_post_liked, UpdateBeat
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, ListView, TemplateView, DetailView
from omega_beats.beats.models import Beat, BeatNotes, BeatPlay
from omega_beats.omega_beats_auth.models import Profile


class BrowserView(ListView):
    """
    A view that displays a list of all beats in the database.
    """

    model = Beat
    context_object_name = 'beats'
    template_name = 'beats/browser.html'
    paginate_by = 12

    def get_queryset(self):
        """
        If the search form is used displays only the beats
        with matching titles with the search form data.
        """

        query = self.request.GET.get('beat_name')

        if query:
            object_list = Beat.objects.filter(
                title__icontains=query,
            )
        else:
            object_list = Beat.objects.all()

        return object_list[::-1]


class PianoRecorder(LoginRequiredMixin, TemplateView):
    """
    A view that displays the virtual piano, used to record beats.
    """

    template_name = 'beats/piano_player.html'
    login_url = reverse_lazy('login user')


class PianoPlayer(DetailView):
    """
    A view that displays the virtual piano, loaded with notes of a selected beat.
    Here the beats can be played.
    """

    model = Beat
    context_object_name = 'beat_info'
    template_name = 'beats/piano_player.html'

    def get(self, request, **kwargs):
        """
        A beat play is saved every time the beat player is opened.
        """

        beat = Beat.objects.get(pk=kwargs['pk'])
        BeatPlay(
            beat=beat,
        ).save()

        return super().get(request, **kwargs)

    def get_context_data(self, **kwargs):
        """
        The user profile is added to the context to display its username
        and link to the profile.
        """

        context = super().get_context_data(**kwargs)
        owner = self.object.owner

        context['owner_profile'] = Profile.objects.get(pk=owner.pk)

        return context


def save_beat_notes_page(request):
    """
    A view that saves the beat's notes, creates a beat entity, and redirects to RegisterBeatView.
    """

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


class RegisterBeatView(UpdateBeat):
    """
    A view in which the user gives the beat title, description, and cover image.
    Redirects to the beat details upon submitting.
    """

    template_name = 'beats/create_beat.html'


class EditBeatView(UpdateBeat):
    """
    A view where the owner of the beat can edit the title, description, and cover of the beat.
    Redirects to the beat details upon submitting.
    """

    template_name = 'beats/edit_beat.html'


class BeatDetails(DetailView):
    """
    A view that displays the beat's details where the owner can edit and delete the beat.
    And other users can like, share, and comment on it.
    """

    model = Beat
    context_object_name = 'beat'
    template_name = 'beats/details_beat.html'

    def get_context_data(self, **kwargs):
        """
        The owner's profile is added to the context as well as if the user has liked the beat,
        and if he is the owner or not.
        Comments and the information of their owners are too added to the context.
        """

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
    """
    In this view, if the owner is authenticated when the beat gets deleted.
    """

    beat = Beat.objects.get(pk=pk)
    beat_notes = beat.beat_notes

    if request.user.pk != beat.owner.pk:
        return redirect('beat details', beat.pk)

    # if beat.cover_image:
    #     cover_image_url = os.path.join(settings.MEDIA_ROOT[:-1], beat.cover_image.url[len('/media/'):])
    #     if os.path.exists(cover_image_url):
    #         os.remove(cover_image_url)

    if beat.cover_image:
        uploader.destroy(beat.cover_image.public_id)

    beat.delete()
    beat_notes.delete()

    return redirect('browser page')
