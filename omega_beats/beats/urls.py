from django.urls import path
from omega_beats.beats import views


urlpatterns = [
    path('', views.browser_page, name='browser page'),
    path('piano/', views.piano_page, name='piano page'),

]
