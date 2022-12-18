from django.urls import path
from .views import home, RegisterView, profil

app_name = 'users'

urlpatterns = [
    path('users/', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profil, name='users-profile'),
]
