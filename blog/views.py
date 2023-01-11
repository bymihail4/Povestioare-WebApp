from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q
from .models import Post, Comment, Category
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from taggit.models import Tag
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import User

def post_list(request, tag_slug=None):
    posts = Post.published.all()

    # Tag
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    # Search
    query = request.GET.get("search")
    if query:
        posts = Post.published.filter(Q(title__icontains=query) | Q(tags__name__icontains=query)).distinct()


    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', {'posts': posts, page: 'pages', 'tag': tag})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')

    favorite = bool

    if post.favorites.filter(id=request.user.id).exists():
        favorite = True

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url() + '#' + str(new_comment.id))
    else:
        comment_form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]

    return render(request, 'post_detail.html', {'post': post,
                                                'favorite': favorite,
                                                'comments': comments,
                                                'comment_form': comment_form,
                                                'similar_posts': similar_posts})


def reply_page(request):
    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():
            post_id = request.POST.get('post_id')
            parent_id = request.POST.get('parent')
            post_url = request.POST.get('post_url')

            reply = form.save(commit=False)

            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()

            return redirect(post_url + '#' + str(reply.id))

        return redirect("/")

    # Add Post view with implict user as author
class AddPost(SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['title', 'slug', 'image', 'tags', 'category', 'body']
    success_message = "Thank you for your contribution. An editor will review your beautifull story in order to be published."

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(AddPost, self).form_valid(form)

    success_url = reverse_lazy("users:users-profile")

    # User Posts List
class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-created')

    # Updatarea postarilor utilizatorului


    # Option to a user to update his one posts
class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['title', 'slug', 'image', 'tags', 'body']
    success_message = "You successfully updated the post."


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    success_url = reverse_lazy('users:users-profile')


    # Option to users to delete his one posts.

class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_message = "You beautiful little story was successfully deleted."

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    success_url = reverse_lazy('users:users-profile')

class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(category__name__icontains=self.kwargs['category']).filter(status='published')



def category_list(request):
    category_list = Category.objects.exclude(name='default')

    context = {
        'category_list': category_list,
    }

    return context