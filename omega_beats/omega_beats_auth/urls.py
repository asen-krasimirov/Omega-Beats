from django.urls import path
from omega_beats.omega_beats_auth import views
import omega_beats.omega_beats_auth.signals


urlpatterns = [
    path('profile/<int:pk>', views.ProfilePageView.as_view(), name='profile page'),
    path('register/', views.RegistrationUserView.as_view(), name='register user'),
    path('login/', views.LoginUserView.as_view(), name='login user'),
    path('logout/', views.logout_user, name='logout user'),
    path('update_profile/<int:pk>', views.ProfileUpdateView.as_view(), name='update profile'),
]
