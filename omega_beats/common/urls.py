from django.urls import path

from omega_beats.common import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home page'),
    path('like-beat/<int:pk>/', views.like_beat, name='like beat'),
    path('comment-beat/<int:pk>/', views.comment_beat, name='comment beat'),
]
