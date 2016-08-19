from django.conf import settings
from django.contrib.auth.models import User
from .models import Follow
from django.shortcuts import redirect, render
from .forms import SignupForm, FollowModelForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
        })

def index(request):
    user = User.objects.all()
    return render(request, 'accounts/index.html', {
        'user':user,
        })

@login_required
def follow(request):
    user_list = User.objects.all()

    if request.method == 'POST':
        follow_form = FollowModelForm(request.POST)
        if follow_form.is_valid():
            follow = follow_form.save(commit=False)
            follow.from_user = request.user
            follow.save()
            return redirect('/accounts/follow/')
    else:
        follow_form = FollowModelForm()
    return render(request, 'accounts/follow_form.html', {
        'form' : follow_form,
        'user_list': user_list,
        })

def request_list(request):
    follow_list = Follow.objects.filter(to_user=request.user)
    return render(request, 'accounts/follow_list.html',{
        'follow_list':follow_list,
        })

def friend_list(request):
    follower_list = Follow.objects.filter(to_user=request.user).filter(is_approved=True)
    following_list = Follow.objects.filter(from_user=request.user).filter(is_approved=True)
    return render(request, 'accounts/friend_list.html', {
        'follower_list':follower_list,
        'following_list':following_list,
        })

def aprv_request_list(request, pk):
    try:
        follow_request = Follow.objects.get(pk=pk)
    except follow_request.DoesNotExist:
        return redirect('accounts:request_list')
    else:
        follow_request.is_approved = True
        follow_request.save()
        return redirect('accounts:request_list')


def del_request_list(request, pk):
    try:
        follow_request = Follow.objects.get(pk=pk)
    except follow_request.DoesNotExist:
        return redirect('accounts:request_list')
    else:
        follow_request.delete()
    return redirect('accounts:request_list')

def search_follow(request):
    if request.method=="POST":
        form = FollowModelForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.from_user = request.user
            form.save()
    return redirect('accounts:follow')