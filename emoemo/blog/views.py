from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Post, Comment
from django.contrib import messages
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from accounts.models import *
from django.contrib.auth.decorators import login_required

# def post_list(request):
#     post_list = Post.objects.all()
#     context = {"post_list":post_list}
#     return render(request, 'blog/index.html', context)

def base(request):
    return render(request, 'base.html', {})

@login_required
def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, "Successfully Created")
            instance.add_tags(post_form.cleaned_data['tag_names'])
            return redirect("blog:index")
    else:
        post_form = PostForm()

    context = {
        "post_form":post_form,
    }
    return render(request, 'blog/index.html', context)

@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("/")
    else:
        form = PostForm(instance=post)

    context = {
        "form":form,
    }
    return render(request, 'blog/post_form.html', context)

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect("/")

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_count = Post.objects.get(pk=post_id).comment.set_all().count
    form = CommentForm()
    context = {
        "post":post,
        "form":form,
        "comment_count":comment_count,
    }
    return render(request, 'blog/post_detail.html', context)

@login_required
def comment_new(request):
    pass

@login_required
def index(request):
    follow_list = Follow.objects.filter(is_approved=True).filter(Q(to_user=request.user) | Q(from_user=request.user))
    friend_set = set()

    post_form = PostForm(request.POST, request.FILES)

    for follow in follow_list:
        friend_set.add(follow.to_user)
        friend_set.add(follow.from_user)

    post_list = Post.objects.filter(author__in=friend_set).annotate(comments_count=Count('comment'))

    context = {
                'post_list': post_list,
                'post_form': post_form,
    }

    return render(request, 'blog/index.html', context)

@login_required
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)


    if request.method == 'POST':
        form = CommentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.post = post
            instance.save()
            return redirect('/', post_id)
    else:
        form = CommentForm()

    context = {
        "form":form,
    }

    return render(request, 'blog/comment_form.html', context)

@login_required
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
            return redirect('/')
    else:
        form = CommentForm(instance=comment)
    context = {
        "form":form,
    }

    return render(request, 'blog/comment_form.html', context)

@login_required
def comment_delete(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, "삭제 완료")
    return redirect("/")