from django.urls import path
from . import views
from .views import AddPost, UserPostListView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('post/user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('', views.post_list, name="post_list"),
    path('<slug:post>/', views.post_detail, name="post_detail"),
    path('comment/reply/', views.reply_page, name="reply"),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_tag'),
    path('category/<category>', views.CatListView.as_view(), name='category'),
]