from django.urls import path
from .views import home, RegisterView, profil
from . import views

app_name = 'users'

urlpatterns = [
    path('users/', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profil, name='users-profile'),
    path('favorite/<int:id>/', views.favorite_add, name='favorite_add'),
    path('post/user/favorites/', views.favorite_list, name='favorite_list'),
]
