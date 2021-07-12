from django.urls import path
from omega_beats.api import views


urlpatterns = [
    path('', views.apiOverview, name='api overview'),
    path('beat-list/', views.beatList, name='beat list'),
    path('beat-details/<str:pk>/', views.beatDetail, name='beat detail'),
    path('beat-create/', views.beatCreate, name='beat create'),
    path('beat-update/<str:pk>', views.beatUpdate, name='beat update'),
    path('beat-delete/<str:pk>', views.beatDelete, name='beat delete'),
]