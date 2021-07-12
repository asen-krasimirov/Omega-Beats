from django.urls import path

from omega_beats.common import views


urlpatterns = [
    path('', views.home_page, name='home page'),
    path('profile/<str:profile_id>', views.profile_page, name='profile page'),

]
