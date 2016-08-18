from django.shortcuts import render
from .models import Post

def post_list(request):
    post_list = Post.objects.all()
    context = {"post_list":post_list}
    return render(request, 'blog/index.html', context)

