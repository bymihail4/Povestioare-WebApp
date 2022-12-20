"""Povestioare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views

from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView
from users.forms import LoginForm
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace="blog")),
    path('users/', include('users.urls', namespace='users')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('users/login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                                 authentication_form=LoginForm), name='login'),
    path('users/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('users/password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('users/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('users/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('users/password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
