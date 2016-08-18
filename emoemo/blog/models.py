from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    content = models.TextField(max_length=150)

    # fonts # 폰트 선택
    # pallete # 색깔 선택
    # tags # 최대 3개
    def __str__(self):
        return self.content

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    post = models.ForeignKey(Post)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    content = models.TextField(max_length=150)

    def __str__(self):
        return self.post

