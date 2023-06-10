from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_blog')
    blog_title = models.CharField(max_length=255)
    blog_content = models.TextField(verbose_name='What is Your mind ?')
    slug = models.SlugField(max_length=1000, unique=True)
    blog_image = models.ImageField(upload_to='blog_img')
    publish_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-publish_at']
    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField(verbose_name='Write Your Comment')
    comment_date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='like_blog')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='like_user')
