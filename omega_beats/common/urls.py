from django.urls import path

from omega_beats.common import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home page'),
]
