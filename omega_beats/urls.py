from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('omega_beats.api.urls')),

    path('', include('omega_beats.common.urls')),
    path('beats/', include('omega_beats.beats.urls')),

]
