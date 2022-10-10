from django.shortcuts import render, get_object_or_404
from blog.models import Post
# from django.utils import timezone
# Create your views here.
def blog_view(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = Post.objects.filter(status=1)
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


def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context =  { 'post': post}
    return render(request, 'test.html', context)
