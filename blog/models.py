from django.db import models
from django.contrib.auth.models import User
from next_prev import next_in_order, prev_in_order
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f' {self.title} - {self.id} '

    def view_increament(self):
        self.counted_views += 1
        self.save()


    def next_post(self):
        return prev_in_order(self)

    def previous_post(self):
        return next_in_order(self)

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f' {self.name} - {self.post} '

    # def next_post(self):
    #     np =  Post.objects.filter(id__gt = self.id)
    #     if np:
    #         return np.last()
    #     else:
    #         return False

    # def previous_post(self):
    #     pp =  Post.objects.filter(id__lt = self.id)
    #     if pp:
    #         return pp[0]
    #     else:
    #         return False

    # def snippets(self):
    #     return self.content[:100] + " ..."