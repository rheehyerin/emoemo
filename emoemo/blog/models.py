import re
import os
import uuid
from django.conf import settings
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import MinLengthValidatior
from django.core.urlresolvers import reverse

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=150, validators=[MinLengthValidatior(6)])
    tag_set = models.CharField(max_length=20, blank=True)

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

class Tag(models.Model):
    name = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

