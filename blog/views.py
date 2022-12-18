from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q
from .models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from django.urls import reverse_lazy
from taggit.models import Tag


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

class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['title', 'slug', 'author', 'image', 'tags', 'body', 'status']

    # success_url = reverse_lazy('users:users-home')