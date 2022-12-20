from django.urls import path
from . import views
from .views import AddPost

app_name = 'blog'

urlpatterns = [
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('', views.post_list, name="post_list"),
    path('<slug:post>/', views.post_detail, name="post_detail"),
    path('comment/reply/', views.reply_page, name="reply"),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_tag')
]