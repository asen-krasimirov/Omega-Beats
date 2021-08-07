from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('omega_beats.common.urls')),
    path('beats/', include('omega_beats.beats.urls')),
    path('auth/', include('omega_beats.omega_beats_auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
