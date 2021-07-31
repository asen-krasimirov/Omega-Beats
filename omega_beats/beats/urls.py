from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from omega_beats.beats import views


urlpatterns = [
    path('', views.BrowserView.as_view(), name='browser page'),
    path('<int:pk>/', views.BeatDetails.as_view(), name='beat details'),

    path('piano/', views.PianoRecorder.as_view(), name='piano page'),
    path('save/', views.save_beat_notes_page, name='save song'),
    path('create/<int:pk>', views.RegisterBeatView.as_view(), name='create beat'),
    path('play/<int:pk>', views.PianoPlayer.as_view(), name='play beat'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
