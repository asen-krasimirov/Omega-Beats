from django.urls import reverse
from django.views.generic import UpdateView
from omega_beats.beats.forms import RegisterBeatForm
from omega_beats.beats.models import Beat


class UpdateBeat(UpdateView):
    model = Beat
    form_class = RegisterBeatForm

    def get_success_url(self):
        return reverse('beat details', args=(self.object.pk,))


def is_post_liked(like_set, current_user):
    for like in like_set:
        if like.owner == current_user:
            return like
    return False
