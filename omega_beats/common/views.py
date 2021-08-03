from core.views import is_post_liked
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import TemplateView
from omega_beats.api.models import Beat
from omega_beats.common.forms import CommentForm
from omega_beats.common.models import Like, Comment


class HomePageView(TemplateView):
    template_name = 'common/index.html'


@login_required
def like_beat(request, pk):
    beat = Beat.objects.get(pk=pk)

    is_liked = is_post_liked(beat.like_set.all(), request.user)

    if not is_liked:
        Like(
            liked_post=beat,
            owner=request.user,
        ).save()
    else:
        is_liked.delete()

    return redirect('beat details', pk)


@login_required
def comment_beat(request, pk):
    beat = Beat.objects.get(pk=pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        content = form.cleaned_data['content']
        Comment(
            content=content,
            commented_post=beat,
            owner=request.user,
        ).save()

    return redirect('beat details', pk)
