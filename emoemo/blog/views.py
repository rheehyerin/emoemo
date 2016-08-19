from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import PostForm

# def post_list(request):
#     post_list = Post.objects.all()
#     context = {"post_list":post_list}
#     return render(request, 'blog/index.html', context)

def base(request):
    return render(request, 'base.html', {})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, "Successfully Created")
            return redirect("blog:index")
    else:
        form = PostForm()

    context = {
        "form":form,
    }
    return render(request, 'blog/post_form.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        "post":post,
    }
    return render(request, 'blog/post_detail.html', context)

def comment_new(request):
    pass

def index(request):
    posts = Post.objects.order_by('pk').reverse()
    if request.method == 'POST' and request.is_ajax():
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #posts = Post.objects.order_by('pk').reverse()
            #return render(request, 'blog/index.html', {'posts': posts})
            return redirect('')
    else:
        form = PostForm()
    #posts = Post.objects.all()
    return render(request, 'blog/index.html',
        {'posts': posts,
         'form':form}
    )

def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.post = post
            instance.save()
            return redirect('blog:post_detail', post_id)
    else:
        form = CommentForm()

    context = {
        "form":form,
    }

    return render(request, 'blog/comment_form.html', context)

def comment_update(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST or None, request.FILES or None, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', post_id)
    else:
        form = CommentForm(instance=comment)
    context = {
        "form":form,
    }

    return render(request, 'blog/comment_form.html', context)

def comment_delete(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, "삭제 완료")
    return redirect("blog:post_detail", post_id)