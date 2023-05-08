from django import template
from blog.models import Post, Category, Comment

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts
    
@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value, arg=20):
    return f"{value[:arg]}..."

@register.inclusion_tag('blog/blog-popular-post.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-tags.html')
def tags(post):
    tags = post.tags.all()
    return {'tags': tags}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}

@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid, approved=True).count()

@register.simple_tag(name='flt')
def function(x):
    posts = x.filter(title='test title')
    return posts