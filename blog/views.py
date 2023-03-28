from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.utils import timezone
# Create your views here.
def blog_view(request, **kwargs):
    # posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])  
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context =  { 'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    next = post.next_post()
    prev = post.previous_post()
    post.view_increament()
    context =  { 'post': post, 'next': next, 'prev': prev}
    return render(request, 'blog/blog-single.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context =  { 'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def test(request):
    return render(request, 'test.html')

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if s := request.GET.get('s'):
        posts = posts.filter(content__contains=s)
    context =  { 'posts': posts}
    return render(request, 'blog/blog-home.html', context)