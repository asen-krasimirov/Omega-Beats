from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from omega_beats.beats import views


urlpatterns = [
    path('', views.BrowserView.as_view(), name='browser page'),
    path('piano/', views.piano_page, name='piano page'),
    path('save/', views.save_beat_notes_page, name='save song'),
    path('create/<int:pk>', views.RegisterBeatView.as_view(), name='create beat'),
    # path('create/<int:pk>', views.register_beat_page, name='create beat'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
